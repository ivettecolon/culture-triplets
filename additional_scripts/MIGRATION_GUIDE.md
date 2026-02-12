# Migration Guide: Original → Flexible Version

## Key Differences

### 1. Image Loading

**Original (Hardcoded):**
```javascript
const imagePaths = [
  "stimuli/rural_day_new_big_church_1.png",
  "stimuli/rural_day_new_big_furniture_1.png",
  // ... 150+ more lines
];
```

**New (Dynamic):**
```javascript
// Option A: Manifest file (recommended)
const CONFIG = {
    imageDirectory: "stimuli/animals2/",
    useManifest: true
};

// Option B: Manual list (still better than original)
const CONFIG = {
    imageDirectory: "stimuli/animals2/",
    useManifest: false,
    manualImageList: ["image1.png", "image2.png", "image3.png"]
};
```

### 2. Validation Triplets

**Original (Random each time):**
```javascript
const validationTrials = [
  {
    type: "validation",
    stimulus: "stimuli/rural_day_old_big_church_1.png",
    choice1: "stimuli/rural_day_old_small_vehicle_1.png",
    choice2: "stimuli/urban_eve_old_small_furniture_1.png"
  },
  // ... 49 more
];

// Random sampling
const selectedValidation = jsPsych.randomization.sampleWithoutReplacement(
    validationTrials, 
    numValidation
);
```

**New (Stable & Configurable):**
```javascript
// Option A: Hardcoded validation (stable across participants)
const CONFIG = {
    validationTriplets: [
        {
            stimulus: "image1.png",  // No path prefix needed!
            choice1: "image2.png",
            choice2: "image3.png"
        }
        // Add all validation triplets here
    ]
};

// Option B: Random validation (like original)
const CONFIG = {
    validationTriplets: null  // Will generate random
};
```

### 3. Configuration

**Original (Scattered throughout code):**
```javascript
// Line 35
const filename = `fpo_mixed_domain_fullSet_${secret_code}.csv`;

// Line 44
const n_main_trials = 620;

// Line 51
experiment_id: "FywDeGGEu5T3",

// Line 648
timeline_variables: createTrialSequence(550, 20, 50),

// Line 716
output = output + "<strong> Here is your secret code: C119H2OR </strong><br>";
```

**New (Centralized CONFIG object):**
```javascript
const CONFIG = {
    // Images
    imageDirectory: "stimuli/animals2/",
    useManifest: true,
    
    // Trials
    numRandomTrials: 550,
    numCheckTrials: 20,
    numValidationTrials: 50,
    
    // Validation
    validationTriplets: [...],
    
    // Data
    experimentId: "FywDeGGEu5T3",
    filenamePrefix: "fpo_mixed_domain_fullSet",
    
    // SONA
    sonaExperimentId: "2226",
    sonaCreditToken: "a9411967764b499caa53a0ecccabe0a1",
    
    // Other
    speedThreshold: 900,
    consentImage: "kc_lab_consent_prolific.png",
    secretCode: "C119H2OR"
};
```

### 4. File Structure

**Original:**
```
your-repo/
├── index.html (contains hardcoded image paths)
├── stimuli/
│   ├── rural_day_new_big_church_1.png
│   ├── rural_day_new_big_furniture_1.png
│   └── ... (150+ images)
└── kc_lab_consent_prolific.png
```

**New:**
```
your-repo/
├── index.html (flexible, configurable)
├── manifest.json (optional - sample)
├── generate_manifest.py (helper script)
├── README.md (full documentation)
├── stimuli/
│   ├── animals2/
│   │   ├── manifest.json
│   │   ├── image1.png
│   │   └── ...
│   └── objects/
│       ├── manifest.json
│       └── ...
└── kc_lab_consent_prolific.png
```

## Benefits of New Version

1. **Easy to switch datasets**: Just change `imageDirectory`
2. **No hardcoding**: No need to manually list 150+ image paths
3. **Stable validation**: Use same validation triplets across participants
4. **Better organization**: All settings in one CONFIG object
5. **GitHub Pages ready**: Works perfectly with static hosting
6. **Reusable**: Same code works for different experiments

## Quick Start Checklist

- [ ] Create image directory (e.g., `stimuli/animals2/`)
- [ ] Add images to directory
- [ ] Generate manifest.json using Python script
- [ ] Update CONFIG.imageDirectory
- [ ] Add validation triplets to CONFIG.validationTriplets
- [ ] Update experiment settings (IDs, codes, etc.)
- [ ] Test locally
- [ ] Push to GitHub
- [ ] Enable GitHub Pages
- [ ] Test live version

## Common Tasks

### Change image set
```javascript
// From
imageDirectory: "stimuli/animals2/",

// To
imageDirectory: "stimuli/objects/",
```

### Change number of trials
```javascript
numRandomTrials: 550,    // Change this
numCheckTrials: 20,       // Change this
numValidationTrials: 50,  // Change this
```

### Use different validation set
```javascript
// Hardcoded
validationTriplets: [...],  // Add your triplets

// Random
validationTriplets: null,   // Null for random
```

### Update SONA settings
```javascript
sonaExperimentId: "2226",
sonaCreditToken: "a9411967764b499caa53a0ecccabe0a1",
```

## Testing

### Local testing
```bash
# Start local server
python -m http.server 8000

# Open browser
http://localhost:8000
```

### GitHub Pages testing
```
https://yourusername.github.io/your-repo/
```

## Troubleshooting

### "No images loaded"
- Check CONFIG.imageDirectory path
- Ensure manifest.json exists (if useManifest: true)
- Check manifest.json is valid JSON
- Verify image files exist

### Validation triplets not working
- Don't include directory path in validation triplets
- Use filename only (e.g., "image1.png" not "stimuli/animals2/image1.png")
- Check filenames match exactly (case-sensitive)

### GitHub Pages 404 errors
- Ensure all paths are relative (no leading `/`)
- Check file and folder names match exactly
- Wait a few minutes after pushing changes

## Support

If you encounter issues:
1. Check browser console (F12) for error messages
2. Verify all files are in correct locations
3. Test manifest.json loads correctly
4. Confirm image paths are relative
