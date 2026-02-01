# EfficientNetB0 Architecture - Mermaid Diagrams

## Complete Architecture Flowchart

```mermaid
flowchart TD
    Start([Input Image<br/>224×224×3]) --> Input[Input Layer<br/>224×224×3]
    
    Input --> Base[EfficientNetB0 Base<br/>Pre-trained on ImageNet<br/>Frozen during initial training]
    
    Base --> Details{EfficientNetB0<br/>Internal Structure}
    
    Details --> Stem[Stem Block<br/>Conv2D + BN + Swish]
    Stem --> MB1[MBConv Blocks<br/>Stage 1-7]
    MB1 --> Head[Head Conv<br/>1×1 Conv2D]
    
    Head --> GAP[Global Average Pooling 2D<br/>Spatial Dimensions → 1×1]
    
    GAP --> BN1[Batch Normalization<br/>Normalize activations]
    
    BN1 --> Drop1[Dropout 0.3<br/>Regularization]
    
    Drop1 --> Dense1[Dense Layer<br/>256 units<br/>ReLU activation]
    
    Dense1 --> BN2[Batch Normalization<br/>Normalize activations]
    
    BN2 --> Drop2[Dropout 0.2<br/>Regularization]
    
    Drop2 --> Output[Output Layer<br/>8 units<br/>Softmax activation]
    
    Output --> Classes([8 Classes:<br/>MEL, NV, BCC, AK<br/>BKL, DF, VASC, SCC])
    
    style Start fill:#e1f5ff
    style Input fill:#bbdefb
    style Base fill:#c8e6c9
    style GAP fill:#fff9c4
    style BN1 fill:#ffccbc
    style Drop1 fill:#f5f5f5
    style Dense1 fill:#c8e6c9
    style BN2 fill:#ffccbc
    style Drop2 fill:#f5f5f5
    style Output fill:#bbdefb
    style Classes fill:#e1f5ff
    style Details fill:#ffe0b2
```

## Detailed Layer-by-Layer Architecture

```mermaid
graph TB
    subgraph Input["Input Stage"]
        I1[Input Layer<br/>Shape: 224×224×3<br/>Type: RGB Image]
    end
    
    subgraph EfficientNetB0["EfficientNetB0 Backbone (Pre-trained)"]
        direction TB
        
        subgraph Stem["Stem Block"]
            S1[Conv2D 3×3<br/>Filters: 32<br/>Stride: 2]
            S2[Batch Normalization]
            S3[Swish Activation]
            S1 --> S2 --> S3
        end
        
        subgraph Stage1["Stage 1: MBConv1"]
            MB1_1[MBConv1, k3×3<br/>Filters: 16<br/>Repeat: 1×]
        end
        
        subgraph Stage2["Stage 2: MBConv6"]
            MB2_1[MBConv6, k3×3<br/>Filters: 24<br/>Repeat: 2×]
        end
        
        subgraph Stage3["Stage 3: MBConv6"]
            MB3_1[MBConv6, k5×5<br/>Filters: 40<br/>Repeat: 2×]
        end
        
        subgraph Stage4["Stage 4: MBConv6"]
            MB4_1[MBConv6, k3×3<br/>Filters: 80<br/>Repeat: 3×]
        end
        
        subgraph Stage5["Stage 5: MBConv6"]
            MB5_1[MBConv6, k5×5<br/>Filters: 112<br/>Repeat: 3×]
        end
        
        subgraph Stage6["Stage 6: MBConv6"]
            MB6_1[MBConv6, k5×5<br/>Filters: 192<br/>Repeat: 4×]
        end
        
        subgraph Stage7["Stage 7: MBConv6"]
            MB7_1[MBConv6, k3×3<br/>Filters: 320<br/>Repeat: 1×]
        end
        
        subgraph HeadBlock["Head Block"]
            H1[Conv2D 1×1<br/>Filters: 1280]
            H2[Batch Normalization]
            H3[Swish Activation]
            H1 --> H2 --> H3
        end
        
        Stem --> Stage1 --> Stage2 --> Stage3 --> Stage4
        Stage4 --> Stage5 --> Stage5 --> Stage6 --> Stage7
        Stage7 --> HeadBlock
    end
    
    subgraph Custom["Custom Classification Head"]
        direction TB
        
        C1[Global Average Pooling 2D<br/>Output: 1280 features]
        C2[Batch Normalization<br/>Normalize features]
        C3[Dropout 0.3<br/>Prevent overfitting]
        C4[Dense Layer<br/>256 units, ReLU<br/>Learnable features]
        C5[Batch Normalization<br/>Normalize features]
        C6[Dropout 0.2<br/>Final regularization]
        C7[Dense Layer<br/>8 units, Softmax<br/>Class probabilities]
        
        C1 --> C2 --> C3 --> C4 --> C5 --> C6 --> C7
    end
    
    subgraph Output["Output"]
        O1[8 Class Probabilities<br/>MEL, NV, BCC, AK<br/>BKL, DF, VASC, SCC]
    end
    
    I1 --> Stem
    HeadBlock --> C1
    C7 --> O1
    
    style Input fill:#e3f2fd
    style EfficientNetB0 fill:#e8f5e9
    style Custom fill:#fff3e0
    style Output fill:#fce4ec
```

## MBConv Block Detail

```mermaid
graph TB
    subgraph MBConv["MBConv Block (Mobile Inverted Bottleneck)"]
        direction TB
        
        Input[Input Tensor] --> Expand{Expansion<br/>Needed?}
        
        Expand -->|Yes| PW1[Pointwise Conv 1×1<br/>Expand channels<br/>Factor: 1 or 6]
        Expand -->|No| DW
        
        PW1 --> BN1[Batch Normalization]
        BN1 --> Act1[Swish Activation]
        
        Act1 --> DW[Depthwise Conv<br/>3×3 or 5×5<br/>Spatial filtering]
        
        DW --> BN2[Batch Normalization]
        BN2 --> Act2[Swish Activation]
        
        Act2 --> SE{Squeeze &<br/>Excitation?}
        
        SE -->|Yes| SEBlock[SE Block<br/>Channel attention]
        SE -->|No| PW2
        
        SEBlock --> PW2[Pointwise Conv 1×1<br/>Project back]
        
        PW2 --> BN3[Batch Normalization]
        
        BN3 --> Skip{Skip<br/>Connection?}
        
        Skip -->|Same dims| Add[Add with Input<br/>Residual connection]
        Skip -->|Different| Output[Output Tensor]
        
        Add --> Output
    end
    
    style Input fill:#e1f5ff
    style Expand fill:#fff9c4
    style SE fill:#fff9c4
    style Skip fill:#fff9c4
    style Output fill:#e1f5ff
    style SEBlock fill:#ffccbc
```

## Training Strategy Flowchart

```mermaid
flowchart TD
    Start([Start Training]) --> Phase1{Phase 1:<br/>Transfer Learning}
    
    Phase1 --> Freeze[Freeze EfficientNetB0 Base<br/>trainable = False]
    
    Freeze --> Train1[Train Custom Head Only<br/>15 epochs<br/>LR: 1e-4<br/>Optimizer: Adam]
    
    Train1 --> Save1[Save Best Model<br/>Based on val_accuracy]
    
    Save1 --> Phase2{Phase 2:<br/>Fine-Tuning}
    
    Phase2 --> Unfreeze[Unfreeze Last 30 Layers<br/>of EfficientNetB0]
    
    Unfreeze --> Train2[Fine-tune Entire Model<br/>35 epochs<br/>LR: 1e-5<br/>Optimizer: Adam]
    
    Train2 --> Callbacks{Callbacks Active}
    
    Callbacks --> CB1[Early Stopping<br/>patience: 10]
    Callbacks --> CB2[Reduce LR on Plateau<br/>patience: 5, factor: 0.5]
    Callbacks --> CB3[Model Checkpoint<br/>save_best_only: True]
    
    CB1 --> Save2[Save Final Model]
    CB2 --> Save2
    CB3 --> Save2
    
    Save2 --> End([Training Complete<br/>Model Ready])
    
    style Start fill:#c8e6c9
    style Phase1 fill:#fff9c4
    style Phase2 fill:#fff9c4
    style End fill:#c8e6c9
    style Freeze fill:#ffccbc
    style Unfreeze fill:#bbdefb
```

## Data Flow Through Network

```mermaid
sequenceDiagram
    participant Input as Input Image<br/>224×224×3
    participant Stem as Stem Block<br/>112×112×32
    participant Stage1 as Stage 1<br/>112×112×16
    participant Stage2 as Stage 2<br/>56×56×24
    participant Stage3 as Stage 3<br/>28×28×40
    participant Stage4 as Stage 4<br/>14×14×80
    participant Stage5 as Stage 5<br/>14×14×112
    participant Stage6 as Stage 6<br/>7×7×192
    participant Stage7 as Stage 7<br/>7×7×320
    participant Head as Head<br/>7×7×1280
    participant GAP as Global Pool<br/>1×1×1280
    participant Dense as Dense Layers<br/>256 → 8
    participant Output as Output<br/>8 Classes
    
    Input->>Stem: Forward Pass
    Stem->>Stage1: Downsample 2×
    Stage1->>Stage2: Downsample 2×
    Stage2->>Stage3: Downsample 2×
    Stage3->>Stage4: Downsample 2×
    Stage4->>Stage5: Same size
    Stage5->>Stage6: Downsample 2×
    Stage6->>Stage7: Same size
    Stage7->>Head: 1×1 Conv
    Head->>GAP: Spatial pooling
    GAP->>Dense: Flatten
    Dense->>Output: Softmax
    Output-->>Input: Prediction
```

## Model Parameters Breakdown

```mermaid
pie title Model Parameters Distribution
    "EfficientNetB0 Base" : 4000000
    "Custom Dense 256" : 328000
    "Output Layer 8" : 2048
    "Batch Norm Layers" : 10000
```

## Compound Scaling (EfficientNet Concept)

```mermaid
graph LR
    subgraph Scaling["EfficientNet Compound Scaling"]
        Base[Base Model<br/>B0] --> Width[Width Scaling<br/>Channels ×α]
        Base --> Depth[Depth Scaling<br/>Layers ×β]
        Base --> Resolution[Resolution Scaling<br/>Input size ×γ]
        
        Width --> B1[EfficientNetB1]
        Depth --> B1
        Resolution --> B1
        
        B1 --> B2[EfficientNetB2]
        B2 --> B3[EfficientNetB3]
        B3 --> Dots[...]
        Dots --> B7[EfficientNetB7]
    end
    
    style Base fill:#c8e6c9
    style B1 fill:#bbdefb
    style B3 fill:#fff9c4
    style B7 fill:#ffccbc
```

## Usage Instructions

### In Markdown/Documentation
Simply copy the code blocks above and paste them into any Markdown file. They will render automatically on platforms that support Mermaid (GitHub, GitLab, Notion, etc.).

### In Jupyter Notebook
```python
from IPython.display import display, Markdown

mermaid_code = """
```mermaid
[paste mermaid code here]
```
"""

display(Markdown(mermaid_code))
```

### Online Rendering
Visit [Mermaid Live Editor](https://mermaid.live/) and paste any diagram code to render and export as PNG/SVG.

### In HTML
```html
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>

<div class="mermaid">
[paste mermaid code here]
</div>
```

---

**Note:** All diagrams represent the EfficientNetB0 architecture as implemented in your skin lesion classification model with custom classification head.
