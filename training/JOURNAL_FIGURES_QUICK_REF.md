# Journal Figures - Quick Reference Card

## 🚀 One-Command Execution

```bash
python training/journal_figures_efficientnetb0.py
```

## 📊 9 Figures Generated

| # | Figure | File | Use In Paper |
|---|--------|------|--------------|
| 1 | Model Architecture | `fig1_architecture` | Methods |
| 2 | Sample Predictions | `fig2_predictions` | Results |
| 3 | Grad-CAM | `fig3_gradcam` | Discussion |
| 4 | Confusion Matrix | `fig4_confusion_matrix` | Results |
| 5 | ROC Curves | `fig5_roc_curves` | Results |
| 6 | Precision-Recall | `fig6_precision_recall` | Supplementary |
| 7 | Class Performance | `fig7_class_performance` | Results |
| 8 | Confidence Analysis | `fig8_confidence_distribution` | Discussion |
| 9 | Feature Maps | `fig9_feature_maps` | Supplementary |

## 📁 Output

```
journal_figures/
├── fig1_architecture.png (+ .pdf)
├── fig2_predictions.png (+ .pdf)
├── fig3_gradcam.png (+ .pdf)
├── fig4_confusion_matrix.png (+ .pdf)
├── fig5_roc_curves.png (+ .pdf)
├── fig6_precision_recall.png (+ .pdf)
├── fig7_class_performance.png (+ .pdf)
├── fig8_confidence_distribution.png (+ .pdf)
└── fig9_feature_maps.png (+ .pdf)
```

**Total:** 18 files (9 PNG + 9 PDF)  
**Quality:** 300 DPI (publication-ready)

## ⚙️ Quick Config

```python
class Config:
    MODEL_PATH = 'path/to/model.h5'
    DATA_ROOT = 'path/to/data'
    OUTPUT_DIR = './journal_figures'
    DPI = 300  # Publication quality
    IMG_SIZE = (224, 224)
    CLASS_NAMES = ['MEL', 'NV', 'BCC', 'AK', 'BKL', 'DF', 'VASC', 'SCC']
```

## 🎯 Kaggle Usage

1. Create notebook
2. Add model + dataset
3. Copy script
4. Run
5. Download from `/kaggle/working/journal_figures/`

## 📝 Figure Descriptions

### Fig 1: Architecture
- Visual model diagram
- Layer-by-layer breakdown
- Parameter counts

### Fig 2: Predictions
- 8 sample images
- True vs predicted labels
- Confidence scores
- Color-coded accuracy

### Fig 3: Grad-CAM
- 6 samples
- Attention heatmaps
- Overlay visualizations
- Model interpretability

### Fig 4: Confusion Matrix
- Absolute counts
- Normalized proportions
- 8×8 class matrix

### Fig 5: ROC Curves
- Per-class curves
- Micro/macro averages
- AUC scores
- Random baseline

### Fig 6: Precision-Recall
- Per-class curves
- AUC scores
- Performance trade-offs

### Fig 7: Class Performance
- Class distribution
- Precision bars
- Recall bars
- F1-score bars

### Fig 8: Confidence
- Overall distribution
- Correct vs incorrect
- By-class box plots
- Threshold analysis

### Fig 9: Feature Maps
- Layer-by-layer features
- 8 channels per layer
- Hierarchical learning

## 🔧 Common Customizations

### More Samples
```python
num_samples_per_class=20  # Default: 10
```

### Higher Quality
```python
DPI = 600  # Default: 300
```

### Different Style
```python
plt.style.use('ggplot')  # Default: seaborn-paper
```

### Custom Colors
```python
colors = plt.cm.Set2(np.linspace(0, 1, 8))
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not found | Script creates demo model |
| Data not found | Script generates dummy data |
| Out of memory | Reduce `num_samples_per_class` |
| Low quality | Increase `DPI` |
| Wrong size | Adjust `FIGSIZE_*` |

## 📚 Requirements

```
tensorflow>=2.10.0
numpy, pandas, matplotlib
seaborn, opencv-python
scikit-learn
```

## ⏱️ Execution Time

- **With GPU:** ~2-5 minutes
- **With CPU:** ~5-10 minutes
- **Depends on:** Sample count, model size

## 💡 Pro Tips

✓ Use PDF for vector graphics  
✓ PNG for raster images  
✓ 300 DPI minimum for journals  
✓ Check journal figure requirements  
✓ Maintain consistent styling  
✓ Label all axes clearly  
✓ Include scale bars  
✓ Provide high contrast  

## 📖 Documentation

- **Full Guide:** `JOURNAL_FIGURES_GUIDE.md`
- **Script:** `journal_figures_efficientnetb0.py`

## 🎓 Citation Template

```bibtex
@article{yourpaper2026,
  title={Skin Lesion Classification using EfficientNetB0},
  author={Your Name},
  journal={Journal Name},
  year={2026}
}
```

---

**Quick Start:** Copy script → Run → Get 18 publication-ready figures! 🚀
