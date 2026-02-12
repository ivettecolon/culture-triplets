# Triadic Judgment Task - GitHub Pages Setup Guide

This is a flexible version of the triadic judgment task designed to work seamlessly with GitHub Pages.

## Key Improvements

1. **Dynamic Image Loading**: Images are loaded from a configurable directory instead of hardcoded paths
2. **Stable Validation Triplets**: Option to use hardcoded validation triplets for consistency across participants
3. **Easy Configuration**: All settings in one place at the top of the file
4. **GitHub Pages Ready**: Works perfectly with static hosting

## Setup Instructions

### Option 1: Using Manifest File (Recommended)

1. **Create your image directory structure**:
   ```
   your-repo/
   ├── index.html
   ├── stimuli/
   │   └── animals2/
   │       ├── manifest.json
   │       ├── image1.png
   │       ├── image2.png
   │       └── ...
   └── kc_lab_consent_prolific.png
   ```

2. **Generate manifest.json**:
   Create a `manifest.json` file in your image directory listing all images:
   ```json
   {
     "images": [
       "image1.png",
       "image2.png",
       "image3.png"
     ]
   }
   ```

3. **Update CONFIG in index.html**:
   ```javascript
   const CONFIG = {
       imageDirectory: "stimuli/animals2/",
       useManifest: true,
       // ... other settings
   };
   ```

### Option 2: Manual Image List

If you prefer not to use a manifest file:

1. Set `useManifest: false` in CONFIG
2. Add all filenames to `manualImageList`:
   ```javascript
   const CONFIG = {
       imageDirectory: "stimuli/animals2/",
       useManifest: false,
       manualImageList: [
           "image1.png",
           "image2.png",
           "image3.png"
       ]
   };
   ```

## Configuration Options

Edit the `CONFIG` object at the top of `index.html`:

### Image Settings
- `imageDirectory`: Path to your image folder (relative to index.html)
- `imageExtension`: File extension for images (e.g., ".png", ".jpg")
- `useManifest`: true/false - whether to load from manifest.json
- `manualImageList`: Array of filenames (if useManifest is false)

### Trial Configuration
- `numRandomTrials`: Number of random triplets (default: 550)
- `numCheckTrials`: Number of attention check trials (default: 20)
- `numValidationTrials`: Number of validation trials (default: 50)

### Validation Triplets
Set `validationTriplets` to an array of hardcoded triplets for consistency:

```javascript
validationTriplets: [
    {
        stimulus: "image1.png",
        choice1: "image2.png",
        choice2: "image3.png"
    },
    // Add all validation triplets here
]
```

Set to `null` to generate random validation trials instead.

### Other Settings
- `experimentId`: Your Pipe experiment ID
- `filenamePrefix`: Prefix for saved data files
- `speedThreshold`: RT threshold for speed warnings (ms)
- `consentImage`: Path to consent form image
- `secretCode`: Completion code for participants
- SONA settings: `sonaExperimentId` and `sonaCreditToken`

## GitHub Pages Deployment

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Add triadic judgment task"
   git push origin main
   ```

2. **Enable GitHub Pages**:
   - Go to Settings → Pages
   - Source: Deploy from branch
   - Branch: main, folder: / (root)
   - Save

3. **Access your experiment**:
   - Your experiment will be available at: `https://yourusername.github.io/your-repo/`

## Python Script to Generate Manifest

Save this as `generate_manifest.py` in your image directory:

```python
import os
import json

def generate_manifest(directory, output_file='manifest.json'):
    """Generate a manifest.json file listing all images in directory"""
    
    # Supported image extensions
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}
    
    # Get all image files
    images = []
    for filename in sorted(os.listdir(directory)):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            images.append(filename)
    
    # Create manifest
    manifest = {
        "images": images,
        "metadata": {
            "total_images": len(images),
            "generated": "auto"
        }
    }
    
    # Save manifest
    output_path = os.path.join(directory, output_file)
    with open(output_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Generated {output_file} with {len(images)} images")
    return images

if __name__ == "__main__":
    # Run from the image directory
    images = generate_manifest('.')
    print("Images included:")
    for img in images[:10]:  # Print first 10
        print(f"  - {img}")
    if len(images) > 10:
        print(f"  ... and {len(images) - 10} more")
```

Run it from your image directory:
```bash
cd stimuli/animals2/
python generate_manifest.py
```

## Troubleshooting

### Images not loading
1. Check that `imageDirectory` path is correct (relative to index.html)
2. Verify manifest.json exists and is formatted correctly
3. Check browser console for errors (F12)
4. Ensure image files match names in manifest.json exactly (case-sensitive)

### Validation triplets not found
1. Ensure filenames in `validationTriplets` match exactly (don't include directory path)
2. The script automatically prepends `imageDirectory` to each filename

### CORS errors on local testing
GitHub Pages handles this automatically. For local testing:
1. Use a local server: `python -m http.server 8000`
2. Navigate to: `http://localhost:8000`

## Directory Structure Example

```
my-experiment/
├── index.html                          # Main experiment file
├── kc_lab_consent_prolific.png        # Consent form
├── stimuli/
│   ├── animals2/
│   │   ├── manifest.json              # Image list
│   │   ├── cat1.png
│   │   ├── dog1.png
│   │   └── ...
│   └── objects/
│       ├── manifest.json
│       └── ...
└── README.md
```

## Switching Between Image Sets

To run experiments with different image sets, simply update CONFIG:

```javascript
// Experiment 1: Animals
imageDirectory: "stimuli/animals2/"

// Experiment 2: Objects
imageDirectory: "stimuli/objects/"
```

Each directory should have its own manifest.json.

## Notes

- The script automatically handles image paths
- Validation triplets use consistent, hardcoded sets for reliability
- All configuration is centralized for easy modification
- The system is fully compatible with GitHub Pages static hosting
- No backend server required - everything runs client-side
