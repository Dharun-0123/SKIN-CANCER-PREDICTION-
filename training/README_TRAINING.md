# EfficientNetB3 ISIC 2019 Training Guide

This guide explains how to train an EfficientNetB3 model on the ISIC 2019 dataset for skin lesion classification.

## 📋 Requirements

```bash
pip install tensorflow scikit-learn matplotlib seaborn opencv-python pandas
```

## 🗂️ Data Structure

Your data should be organized in one of two ways:

### Option 1: Folder Structure (Recommended)
```
data/
├── MEL/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── NV/
│   ├── image1.jpg
│   └── ...
├── BCC/
├── AK/
├── BKL/
├── DF/
├── VASC/
└── SCC/
```

### Option 2: CSV Format
- CSV file with columns: `image_name`, `label`
- All images in a single directory

## 🚀 Quick Start

### 1. Update Configuration

Edit the `Config` class in the script:

```python
class Config:
    DATA_ROOT = '/path/to/your/isic/data'  # Update this!
    OUTPUT_DIR = 'output'
    MODEL_SAVE_PATH = 'webapp/models/efficientnetb3_isic.h5'
    
    IMG_SIZE = (300, 300)
    BATCH_SIZE = 32
    EPOCHS = 50
    LEARNING_RATE = 1e-4
```

### 2. Run Training

```bash
python train_efficientnetb3_isic.py
```

Or in Kaggle/Jupyter:
```python
%run train_efficientnetb3_isic.py
```

## 📊 What the Script Does

### Phase 1: Transfer Learning (15 epochs)
- Loads EfficientNetB3 with ImageNet weights
- Freezes base model
- Trains only the custom classifier head
- Uses class weights to handle imbalance

### Phase 2: Fine-tuning (35 epochs)
- Unfreezes last 30 layers of base model
- Continues training with lower learning rate (1e-5)
- Uses early stopping and learning rate reduction

## 📈 Outputs

The script generates:

### Models
- `webapp/models/efficientnetb3_isic.h5` - Best model (ready for deployment)

### Visualizations
- `output/training_history.png` - Loss and accuracy curves
- `output/confusion_matrix.png` - Confusion matrix
- `output/confusion_matrix_normalized.png` - Normalized confusion matrix
- `output/roc_curves.png` - ROC curves for all classes
- `output/precision_recall_curves.png` - PR curves
- `output/gradcam_visualization.png` - Grad-CAM heatmaps
- `output/augmented_samples.png` - Augmented training samples

### Reports
- `output/classification_report.csv` - Detailed metrics per class
- `output/predictions.csv` - All validation predictions
- `output/training_log.csv` - Training history

## 🎯 Key Features

### 1. Data Augmentation
- Rotation (±30°)
- Width/height shifts (20%)
- Zoom (20%)
- Brightness variation (80-120%)
- Horizontal and vertical flips

### 2. Class Imbalance Handling
- Automatic class weight computation
- Balanced sampling during training

### 3. Callbacks
- **ModelCheckpoint**: Saves best model based on validation accuracy
- **EarlyStopping**: Stops if no improvement for 10 epochs
- **ReduceLROnPlateau**: Reduces learning rate when plateauing
- **TensorBoard**: Logs for visualization
- **CSVLogger**: Saves training metrics

### 4. Evaluation Metrics
- Accuracy, Precision, Recall, F1-score
- ROC-AUC (micro, macro, per-class)
- Confusion matrices
- Precision-recall curves

### 5. Explainability
- Grad-CAM visualizations
- Shows which regions the model focuses on
- Helps validate model decisions

### 6. Test-Time Augmentation (TTA)
- Improves prediction robustness
- Averages predictions from multiple augmented versions

## 🔧 Customization

### Change Model Architecture

```python
# Use different EfficientNet variant
from tensorflow.keras.applications import EfficientNetB4

base_model = EfficientNetB4(
    include_top=False,
    weights='imagenet',
    input_shape=(380, 380, 3)  # B4 uses 380x380
)
```

### Adjust Training Parameters

```python
config.BATCH_SIZE = 16  # Reduce if out of memory
config.EPOCHS = 100     # Train longer
config.LEARNING_RATE = 5e-5  # Lower learning rate
```

### Add Focal Loss

```python
import tensorflow_addons as tfa

model.compile(
    optimizer=optimizers.Adam(learning_rate=config.LEARNING_RATE),
    loss=tfa.losses.SigmoidFocalCrossEntropy(),
    metrics=['accuracy']
)
```

## 📝 Tips for Better Accuracy

1. **More Data**: Use data from multiple ISIC challenges
2. **Ensemble**: Train multiple models and average predictions
3. **Advanced Augmentation**: Add hair removal, color normalization
4. **Larger Models**: Try EfficientNetB5 or B6
5. **Progressive Unfreezing**: Gradually unfreeze more layers
6. **Hyperparameter Tuning**: Use Keras Tuner or Optuna

## 🐛 Troubleshooting

### Out of Memory
```python
config.BATCH_SIZE = 16  # or 8
# Enable mixed precision
tf.keras.mixed_precision.set_global_policy('mixed_float16')
```

### Slow Training
```python
# Use smaller image size
config.IMG_SIZE = (224, 224)

# Reduce augmentation
config.ROTATION_RANGE = 15
```

### Poor Validation Accuracy
- Check data quality and labels
- Increase training epochs
- Try different learning rates
- Add more augmentation
- Use class weights

## 📚 References

- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [ISIC 2019 Challenge](https://challenge.isic-archive.com/landing/2019/)
- [Grad-CAM Paper](https://arxiv.org/abs/1610.02391)

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the inline comments in the script
3. Consult TensorFlow documentation

## 📄 License

This training script is provided as-is for educational and research purposes.
