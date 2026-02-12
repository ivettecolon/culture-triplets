/**
 * VALIDATION TRIPLETS CONFIGURATION
 * 
 * This file contains the hardcoded validation triplets for consistent testing.
 * Copy the validationTriplets array into the CONFIG object in index.html
 * 
 * Format:
 * {
 *   stimulus: "filename.png",    // Target image (top)
 *   choice1: "filename.png",     // Left choice
 *   choice2: "filename.png"      // Right choice
 * }
 * 
 * Notes:
 * - Do NOT include the directory path - just the filename
 * - The script will automatically prepend CONFIG.imageDirectory
 * - Ensure filenames match exactly (case-sensitive)
 */

const validationTriplets = [
    // Example triplets - replace with your actual validation set
    {
        stimulus: "rural_day_old_big_church_1.png",
        choice1: "rural_day_old_small_vehicle_1.png",
        choice2: "urban_eve_old_small_furniture_1.png"
    },
    {
        stimulus: "urban_day_old_small_furniture_1.png",
        choice1: "urban_eve_new_big_church_1.png",
        choice2: "urban_eve_old_black_man_1.png"
    },
    {
        stimulus: "urban_eve_old_black_man_1.png",
        choice1: "urban_eve_new_small_church_1.png",
        choice2: "urban_eve_new_small_vehicle_1.png"
    },
    {
        stimulus: "urban_eve_old_black_woman_1.png",
        choice1: "urban_eve_old_small_church_1.png",
        choice2: "urban_eve_new_big_furniture_1.png"
    },
    {
        stimulus: "rural_eve_young_white_man_1.png",
        choice1: "urban_day_old_big_house_1.png",
        choice2: "urban_day_new_small_furniture_1.png"
    },
    {
        stimulus: "urban_eve_new_small_house_1.png",
        choice1: "urban_eve_young_black_woman_1.png",
        choice2: "urban_eve_old_small_vehicle_1.png"
    },
    {
        stimulus: "urban_eve_new_small_vehicle_1.png",
        choice1: "rural_eve_old_small_church_1.png",
        choice2: "rural_day_young_black_man_1.png"
    },
    {
        stimulus: "urban_eve_young_white_woman_1.png",
        choice1: "rural_eve_old_big_vehicle_1.png",
        choice2: "rural_day_new_big_church_1.png"
    }
    // Add remaining 42 triplets here to reach 50 total
    // ...
];

/**
 * USAGE IN index.html:
 * 
 * Copy the array above and paste it into the CONFIG object:
 * 
 * const CONFIG = {
 *     // ... other settings ...
 *     
 *     validationTriplets: [
 *         // Paste the triplets here
 *     ],
 *     
 *     // ... more settings ...
 * };
 */

/**
 * ALTERNATIVE: Generate from CSV
 * 
 * If you have validation triplets in a CSV file, use this Python script:
 */

const pythonScript = `
import csv
import json

def csv_to_validation_triplets(csv_file, output_file='validation_triplets.json'):
    """
    Convert CSV of validation triplets to JavaScript array
    
    CSV format:
    stimulus,choice1,choice2
    image1.png,image2.png,image3.png
    """
    triplets = []
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            triplets.append({
                'stimulus': row['stimulus'],
                'choice1': row['choice1'],
                'choice2': row['choice2']
            })
    
    # Save as JSON
    with open(output_file, 'w') as f:
        json.dump(triplets, f, indent=2)
    
    # Also print as JavaScript
    print("validationTriplets: [")
    for i, t in enumerate(triplets):
        comma = "," if i < len(triplets) - 1 else ""
        print(f"  {{stimulus: \\"{t['stimulus']}\\", choice1: \\"{t['choice1']}\\", choice2: \\"{t['choice2']}\\"}}{{comma}}")
    print("]")
    
    return triplets

if __name__ == "__main__":
    csv_to_validation_triplets('validation_triplets.csv')
`;
