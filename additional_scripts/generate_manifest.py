#!/usr/bin/env python3
"""
Generate manifest.json for triadic judgment task
Usage: python generate_manifest.py [directory]
"""

import os
import json
import argparse
from pathlib import Path

def generate_manifest(directory='.', output_file='manifest.json', recursive=False):
    """
    Generate a manifest.json file listing all images in directory
    
    Args:
        directory: Directory to scan for images
        output_file: Name of output manifest file
        recursive: If True, scan subdirectories
    """
    
    # Supported image extensions
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg'}
    
    # Get all image files
    images = []
    dir_path = Path(directory)
    
    if recursive:
        # Recursively find images
        for ext in image_extensions:
            images.extend([str(p.relative_to(dir_path)) for p in dir_path.rglob(f'*{ext}')])
            images.extend([str(p.relative_to(dir_path)) for p in dir_path.rglob(f'*{ext.upper()}')])
    else:
        # Only current directory
        for filename in os.listdir(directory):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                images.append(filename)
    
    # Sort for consistency
    images = sorted(set(images))
    
    # Create manifest
    manifest = {
        "images": images,
        "metadata": {
            "total_images": len(images),
            "directory": str(dir_path),
            "recursive": recursive,
            "generated_by": "generate_manifest.py"
        }
    }
    
    # Save manifest
    output_path = os.path.join(directory, output_file)
    with open(output_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    return images, output_path

def main():
    parser = argparse.ArgumentParser(
        description='Generate manifest.json for image directories',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_manifest.py                    # Current directory
  python generate_manifest.py stimuli/animals2   # Specific directory
  python generate_manifest.py -r stimuli         # Recursive scan
        """
    )
    parser.add_argument('directory', nargs='?', default='.',
                       help='Directory to scan (default: current directory)')
    parser.add_argument('-o', '--output', default='manifest.json',
                       help='Output filename (default: manifest.json)')
    parser.add_argument('-r', '--recursive', action='store_true',
                       help='Scan subdirectories recursively')
    
    args = parser.parse_args()
    
    # Check if directory exists
    if not os.path.isdir(args.directory):
        print(f"Error: Directory '{args.directory}' not found")
        return 1
    
    # Generate manifest
    print(f"Scanning {'recursively' if args.recursive else 'directory'}: {args.directory}")
    images, output_path = generate_manifest(args.directory, args.output, args.recursive)
    
    # Print results
    print(f"\n✓ Generated {args.output} with {len(images)} images")
    print(f"  Saved to: {output_path}\n")
    
    # Show sample of images
    print("Images included:")
    for img in images[:20]:
        print(f"  - {img}")
    
    if len(images) > 20:
        print(f"  ... and {len(images) - 20} more")
    
    return 0

if __name__ == "__main__":
    exit(main())
