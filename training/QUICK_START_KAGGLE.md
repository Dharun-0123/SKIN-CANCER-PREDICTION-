# Quick Start: Kaggle EfficientNetB3 Training

## 🚀 5-Minute Setup

### Step 1: Create Kaggle Notebook
1. Go to [Kaggle](https://www.kaggle.com/)
2. Click **"New Notebook"**
3. Enable **GPU** (Settings → Accelerator → GPU T4 x2)

### Step 2: Add Dataset
1. Click **"+ Add Data"** in right panel
2. Search: **"ISIC 2019 skin lesion"**
3. Add dataset: `salviohexia/isic-2019-skin-lesion-images-for-classification`

### Step 3: Copy Training Code
1. Open `training/kaggle_efficientnetb3_isic.py`
2. Copy **entire file content**
3. Paste into Kaggle notebook
4. (Optional) Split into cells at `# CELL X:` comments

### Step 4: Run Training
1. Click **"Run All"** or run cells sequentially
2. Wait 2-4 hours for training to complete
3. Monitor progress in output

### Step 5: Download Model
1. Training completes → Check **"Output"** tab (right panel)
2. Find `efficientnetb3_isic.h5` (~50-60 MB)
3. Click download icon
4. Save to your `webapp/models/` directory

## 📊 What You'll Get

### Trained Model
- `efficientnetb3_isic.h5` - Ready-to-deploy model

### Visualizations
- Class distribution charts
- Augmented sample images
- Training history curves
- Confusion matrices
- ROC curves
- Grad-CAM heatmaps

### Evaluation Reports
- Classification report (precision, recall, F1)
- Predictions CSV with confidence scores
- Model metadata JSON

## ⚙️ Configuration (Optional)

Edit these in **Cell 5** if needed:

```python
class Config:
    BATCH_SIZE = 32        # Reduce to 16 or 8 if OOM
    EPOCHS = 50            # Reduce to 30 for faster testing
    LEARNING_RATE = 1e-4   # Default works well
```

## 🎯 Expected Results

- **Training Time:** 2-4 hours (GPU)
- **Validation Accuracy:** 75-85%
- **Model Size:** ~50-60 MB
- **Classes:** 8 skin lesion types

## 🔧 Troubleshooting

### "Dataset not found"
→ Ensure ISIC dataset is added (Step 2)
→ Check Cell 5 output for detected path

### "Out of memory"
→ Reduce `BATCH_SIZE` to 16 or 8
→ Reduce `max_images_per_class` in Cell 6

### "Training too slow"
→ Verify GPU is enabled (Settings)
→ Reduce `EPOCHS` for testing

### "Low accuracy"
→ Train longer (increase `EPOCHS`)
→ Check Cell 24 for improvement tips

## 📝 Using the Model

After downloading `efficientnetb3_isic.h5`:

```python
import tensorflow as tf
import numpy as np
import cv2

# Load model
model = tf.keras.models.load_model('efficientnetb3_isic.h5')

# Preprocess image
img = cv2.imread('skin_lesion.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (300, 300))
img = img / 255.0
img = np.expand_dims(img, axis=0)

# Predict
predictions = model.predict(img)
class_names = ['MEL', 'NV', 'BCC', 'AK', 'BKL', 'DF', 'VASC', 'SCC']
predicted_class = class_names[np.argmax(predictions)]
confidence = np.max(predictions)

print(f"Predicted: {predicted_class} ({confidence:.2%})")
```

## 📚 Files Reference

- `kaggle_efficientnetb3_isic.py` - Complete training script (24 cells)
- `KAGGLE_NOTEBOOK_COMPLETE.md` - Detailed documentation
- `README_TRAINING.md` - Training guide
- `train_efficientnetb3_isic.py` - Reference implementation

## 🎓 What's Included

### 24 Cells Covering:
1. ✓ Environment setup & dependency check
2. ✓ Library imports & version info
3. ✓ Hardware detection (GPU/TPU/CPU)
4. ✓ Reproducibility (seed setting)
5. ✓ Dataset auto-detection
6. ✓ Data loading with progress
7. ✓ Stratified train/val split
8. ✓ Class weight computation
9. ✓ Data augmentation pipeline
10. ✓ Model architecture (EfficientNetB3)
11. ✓ Training callbacks
12. ✓ Phase 1: Transfer learning
13. ✓ Phase 2: Fine-tuning
14. ✓ Training history plots
15. ✓ Model evaluation
16. ✓ Confusion matrix
17. ✓ Classification report
18. ✓ ROC curves & AUC
19. ✓ Grad-CAM visualization
20. ✓ Predictions export
21. ✓ Test-time augmentation
22. ✓ Single image inference
23. ✓ Model summary & export
24. ✓ Tips for improvement

## 💡 Pro Tips

1. **First Run:** Use smaller dataset (`max_images_per_class=1000`) to test
2. **Production:** Remove limit and train on full dataset
3. **Better Results:** Follow tips in Cell 24
4. **Ensemble:** Train multiple models with different seeds
5. **TTA:** Use test-time augmentation for critical predictions

## 🔗 Resources

- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [ISIC 2019 Challenge](https://challenge2019.isic-archive.com/)
- [Kaggle Docs](https://www.kaggle.com/docs)

---

**Ready to train?** Follow the 5 steps above and you'll have a production-ready model in a few hours! 🚀
