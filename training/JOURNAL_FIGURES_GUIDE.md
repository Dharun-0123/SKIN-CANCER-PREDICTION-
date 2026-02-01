# Journal Figure Generation Guide - EfficientNetB0

## Overview

This script generates **9 publication-quality figures** for academic journals using EfficientNetB0 model for skin lesion classification. All figures are generated at **300 DPI** in both **PNG** and **PDF** formats.

## Quick Start

### In Kaggle

1. **Create new notebook**
2. **Add your model** as dataset input
3. **Add ISIC 2019 dataset**
4. **Copy entire script** from `journal_figures_efficientnetb0.py`
5. **Run all cells**
6. **Download figures** from `/kaggle/working/journal_figures/`

### Locally

```bash
python training/journal_figures_efficientnetb0.py
```

## Generated Figures

### Figure 1: Model Architecture Diagram
**File:** `fig1_architecture.png` / `.pdf`

Visual representation of the EfficientNetB0 architecture showing:
- Input layer (224×224×3)
- EfficientNetB0 base (pre-trained)
- Global Average Pooling
- Batch Normalization layers
- Dropout layers (0.3, 0.2)
- Dense layers (256 units)
- Output layer (8 classes)
- Total parameter count

**Use in paper:** Methods section - Model Architecture

---

### Figure 2: Sample Predictions with Confidence
**File:** `fig2_predictions.png` / `.pdf`

Grid of 8 sample images showing:
- Original lesion images
- True labels
- Predicted labels
- Confidence scores
- Color-coded correctness (green=correct, red=incorrect)

**Use in paper:** Results section - Model Performance Examples

---

### Figure 3: Grad-CAM Visualization
**File:** `fig3_gradcam.png` / `.pdf`

6 samples × 3 columns showing:
- Original images
- Grad-CAM heatmaps
- Overlay visualizations
- Predictions with confidence

Demonstrates where the model focuses attention for classification decisions.

**Use in paper:** Results section - Model Interpretability / Discussion

---

### Figure 4: Confusion Matrix
**File:** `fig4_confusion_matrix.png` / `.pdf`

Two heatmaps side-by-side:
- **Left:** Absolute counts
- **Right:** Normalized proportions

Shows classification performance across all 8 classes (MEL, NV, BCC, AK, BKL, DF, VASC, SCC).

**Use in paper:** Results section - Classification Performance

---

### Figure 5: ROC Curves
**File:** `fig5_roc_curves.png` / `.pdf`

Multi-class ROC analysis showing:
- Per-class ROC curves with AUC scores
- Micro-average ROC (AUC)
- Macro-average ROC (AUC)
- Random classifier baseline

**Use in paper:** Results section - Diagnostic Performance

---

### Figure 6: Precision-Recall Curves
**File:** `fig6_precision_recall.png` / `.pdf`

Per-class precision-recall curves with AUC scores for all 8 classes.

**Use in paper:** Results section - Model Performance Metrics

---

### Figure 7: Class Performance Analysis
**File:** `fig7_class_performance.png` / `.pdf`

Four subplots showing:
1. **Class Distribution:** Sample counts per class
2. **Precision by Class:** Bar chart with mean line
3. **Recall by Class:** Bar chart with mean line
4. **F1-Score by Class:** Bar chart with mean line

**Use in paper:** Results section - Per-Class Performance Analysis

---

### Figure 8: Confidence Distribution
**File:** `fig8_confidence_distribution.png` / `.pdf`

Four subplots analyzing prediction confidence:
1. **Overall Distribution:** Histogram of all confidence scores
2. **Correct vs Incorrect:** Comparative histograms
3. **By Class:** Box plots showing confidence distribution per class
4. **Accuracy vs Threshold:** Dual-axis plot showing accuracy and sample count at different confidence thresholds

**Use in paper:** Results/Discussion - Model Reliability Analysis

---

### Figure 9: Feature Map Visualization
**File:** `fig9_feature_maps.png` / `.pdf`

Visualization of intermediate feature maps through network layers:
- Original input image
- Feature maps from 5 representative layers
- 8 channels per layer
- Shows hierarchical feature learning

**Use in paper:** Methods/Results - Feature Learning Visualization

---

## Configuration

Edit the `Config` class to customize:

```python
class Config:
    # Paths
    DATA_ROOT = './data/isic-2019'
    OUTPUT_DIR = './journal_figures'
    MODEL_PATH = 'webapp/models/EfficientNetB0_skin-cancer.h5'
    
    # Model parameters
    IMG_SIZE = (224, 224)
    CLASS_NAMES = ['MEL', 'NV', 'BCC', 'AK', 'BKL', 'DF', 'VASC', 'SCC']
    
    # Figure quality
    DPI = 300  # Publication quality
    FIGSIZE_SINGLE = (8, 6)
    FIGSIZE_DOUBLE = (16, 6)
    FIGSIZE_LARGE = (12, 10)
```

## Output Structure

```
journal_figures/
├── fig1_architecture.png
├── fig1_architecture.pdf
├── fig2_predictions.png
├── fig2_predictions.pdf
├── fig3_gradcam.png
├── fig3_gradcam.pdf
├── fig4_confusion_matrix.png
├── fig4_confusion_matrix.pdf
├── fig5_roc_curves.png
├── fig5_roc_curves.pdf
├── fig6_precision_recall.png
├── fig6_precision_recall.pdf
├── fig7_class_performance.png
├── fig7_class_performance.pdf
├── fig8_confidence_distribution.png
├── fig8_confidence_distribution.pdf
├── fig9_feature_maps.png
└── fig9_feature_maps.pdf
```

## Requirements

```python
tensorflow>=2.10.0
keras>=2.10.0
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
opencv-python>=4.5.0
scikit-learn>=1.0.0
```

## Usage in Academic Papers

### Recommended Figure Placement

**Introduction/Background:**
- None (use literature review figures)

**Methods:**
- Figure 1: Model Architecture

**Results:**
- Figure 2: Sample Predictions
- Figure 4: Confusion Matrix
- Figure 5: ROC Curves
- Figure 7: Class Performance Analysis

**Discussion:**
- Figure 3: Grad-CAM (Interpretability)
- Figure 8: Confidence Distribution (Reliability)

**Supplementary Materials:**
- Figure 6: Precision-Recall Curves
- Figure 9: Feature Maps

### Figure Captions (Templates)

**Figure 1:**
> "Architecture of the EfficientNetB0-based deep learning model for skin lesion classification. The model consists of a pre-trained EfficientNetB0 backbone followed by global average pooling, batch normalization, dropout layers, and fully connected layers, culminating in an 8-class softmax output layer."

**Figure 2:**
> "Representative predictions from the EfficientNetB0 model on test images. Each panel shows the original lesion image, true label, predicted label, and confidence score. Green titles indicate correct predictions, while red titles indicate misclassifications."

**Figure 3:**
> "Gradient-weighted Class Activation Mapping (Grad-CAM) visualizations showing model attention. For each sample, the original image (left), Grad-CAM heatmap (center), and overlay (right) are displayed, revealing which regions the model focuses on for classification."

**Figure 4:**
> "Confusion matrices showing classification performance across all eight skin lesion classes. (A) Absolute counts. (B) Normalized proportions. Diagonal elements represent correct classifications."

**Figure 5:**
> "Receiver Operating Characteristic (ROC) curves for multi-class classification. Individual curves for each class are shown along with micro-average and macro-average curves. AUC values are reported in the legend."

**Figure 6:**
> "Precision-Recall curves for all eight skin lesion classes. Area Under the Curve (AUC) values are provided for each class."

**Figure 7:**
> "Per-class performance analysis. (A) Class distribution in the dataset. (B) Precision by class. (C) Recall by class. (D) F1-score by class. Red dashed lines indicate mean values."

**Figure 8:**
> "Analysis of prediction confidence scores. (A) Overall confidence distribution. (B) Confidence comparison between correct and incorrect predictions. (C) Confidence distribution by class. (D) Accuracy and sample retention at different confidence thresholds."

**Figure 9:**
> "Visualization of learned feature representations through network layers. The top row shows the original input image, while subsequent rows display feature maps from progressively deeper layers, illustrating hierarchical feature learning."

## Customization

### Change Number of Samples

```python
# In load_sample_images function
X_samples, y_samples, sample_paths = load_sample_images(
    config.DATA_ROOT, 
    num_samples_per_class=20  # Change this
)
```

### Modify Figure Style

```python
# Change matplotlib style
plt.style.use('seaborn-v0_8-whitegrid')  # or 'ggplot', 'bmh', etc.

# Adjust colors
colors = plt.cm.Pastel1(np.linspace(0, 1, config.NUM_CLASSES))
```

### Add Watermark

```python
# Add to any figure
plt.text(0.5, 0.5, 'DRAFT', transform=ax.transAxes,
        fontsize=50, color='gray', alpha=0.3,
        ha='center', va='center', rotation=30)
```

## Troubleshooting

### Model Not Found
```python
# The script will create a demo model if yours isn't found
# Or specify correct path in Config class
MODEL_PATH = '/path/to/your/model.h5'
```

### Dataset Not Found
```python
# Script generates dummy data for demonstration
# Or specify correct path
DATA_ROOT = '/path/to/isic-2019'
```

### Out of Memory
```python
# Reduce number of samples
num_samples_per_class=5  # Instead of 10

# Or reduce batch size
model.predict(X_samples, batch_size=16, verbose=0)
```

### Low Quality Figures
```python
# Increase DPI (warning: larger file sizes)
DPI = 600  # Instead of 300
```

## Best Practices

1. **Always use 300 DPI** for journal submissions
2. **Provide both PNG and PDF** formats
3. **Use consistent color schemes** across figures
4. **Include scale bars** where appropriate
5. **Label all axes** clearly
6. **Use vector formats (PDF)** when possible
7. **Check journal requirements** for figure specifications
8. **Maintain aspect ratios** for proper display

## Citation

If you use these figures in your publication, please cite:

```bibtex
@article{your_paper,
  title={Deep Learning for Skin Lesion Classification using EfficientNetB0},
  author={Your Name et al.},
  journal={Journal Name},
  year={2026}
}
```

## License

This code is provided for academic and research purposes.

---

**Generated:** 2026-01-26  
**Version:** 1.0  
**Contact:** Your research team
