# Quick Copy - Mermaid Diagrams for IEEE Paper

## 📋 Copy-Paste Ready Diagrams

### Diagram 1: Main Architecture (RECOMMENDED)

```mermaid
flowchart TD
    Start([Input Image<br/>224×224×3]) --> Input[Input Layer<br/>224×224×3]
    Input --> Base[EfficientNetB0 Base<br/>Pre-trained on ImageNet]
    Base --> GAP[Global Average Pooling 2D]
    GAP --> BN1[Batch Normalization]
    BN1 --> Drop1[Dropout 0.3]
    Drop1 --> Dense1[Dense Layer<br/>256 units, ReLU]
    Dense1 --> BN2[Batch Normalization]
    BN2 --> Drop2[Dropout 0.2]
    Drop2 --> Output[Output Layer<br/>8 units, Softmax]
    Output --> Classes([Classification Output<br/>MEL, NV, BCC, AK<br/>BKL, DF, VASC, SCC])
    
    style Start fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Input fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Base fill:#e0e0e0,stroke:#333,stroke-width:3px,color:#000
    style GAP fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style BN1 fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style Drop1 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Dense1 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style BN2 fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style Drop2 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Output fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
    style Classes fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 1. Proposed EfficientNetB0-based architecture for skin lesion classification.

---

### Diagram 2: Training Strategy

```mermaid
flowchart TD
    Start([Start Training]) --> Phase1[Phase 1: Transfer Learning]
    Phase1 --> Freeze[Freeze EfficientNetB0 Base]
    Freeze --> Train1[Train Custom Head<br/>15 epochs, LR: 1e-4]
    Train1 --> Phase2[Phase 2: Fine-Tuning]
    Phase2 --> Unfreeze[Unfreeze Last 30 Layers]
    Unfreeze --> Train2[Fine-tune Model<br/>35 epochs, LR: 1e-5]
    Train2 --> End([Training Complete])
    
    style Start fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Phase1 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style Freeze fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Train1 fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
    style Phase2 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style Unfreeze fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Train2 fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
    style End fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 2. Two-phase training strategy for model optimization.

---

## 🎯 How to Use

### Step 1: Copy Diagram Code
Copy the entire code block including the ` ```mermaid ` tags.

### Step 2: Export as Image
1. Go to [Mermaid Live Editor](https://mermaid.live/)
2. Paste the code
3. Click "Export" → Choose SVG (vector) or PNG (high DPI)

### Step 3: Insert in Paper
- **LaTeX**: Use `\includegraphics{}`
- **Word**: Insert → Picture
- **Markdown**: Paste code directly

---

## ✅ IEEE Compliance Checklist

- [x] Grayscale colors (print-friendly)
- [x] High contrast (readable)
- [x] Simple design (professional)
- [x] Clear labels (no ambiguity)
- [x] Vector export (scalable)
- [x] Standard fonts (compatible)

---

## 📝 Quick Tips

1. **Always export as SVG** for best quality
2. **Use 300+ DPI** if exporting PNG
3. **Test grayscale** before submission
4. **Keep captions concise** (IEEE style)
5. **Reference in text** as "Fig. 1"

---

**Ready to use in your IEEE paper!** 🚀
