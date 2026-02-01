# Data Flow Diagrams (DFD) - Skin Cancer Prediction System

## Level 0: Context Diagram

```mermaid
graph TB
    User([User/Patient]) -->|Skin Image + Info| System((Skin Cancer<br/>Prediction<br/>System))
    System -->|Diagnosis Report| User
    
    Admin([Administrator]) -->|Manage System| System
    System -->|Analytics Data| Admin
    
    System -->|Store Data| DB[(Database)]
    DB -->|Retrieve Data| System
    
    System -->|Send Notifications| Email[Email Service]
    
    style User fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Admin fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style System fill:#d0d0d0,stroke:#333,stroke-width:3px,color:#000
    style DB fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style Email fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 1. Level 0 DFD - Context diagram showing the Skin Cancer Prediction System and its external entities.

---

## Level 1: Major Processes

```mermaid
graph TB
    User([User]) -->|Login Credentials| P1[1.0<br/>User<br/>Authentication]
    P1 -->|Auth Token| User
    
    User -->|Skin Image| P2[2.0<br/>Image<br/>Processing]
    P2 -->|Preprocessed Image| P3[3.0<br/>AI Model<br/>Prediction]
    
    P3 -->|Prediction Results| P4[4.0<br/>Result<br/>Analysis]
    P4 -->|Diagnosis Report| User
    
    User -->|View Request| P5[5.0<br/>History<br/>Management]
    P5 -->|Historical Data| User
    
    Admin([Admin]) -->|Access Request| P6[6.0<br/>Admin<br/>Dashboard]
    P6 -->|Analytics & Reports| Admin
    
    P1 -.->|User Data| D1[(User<br/>Database)]
    D1 -.->|User Info| P1
    
    P2 -.->|Image Data| D2[(Image<br/>Storage)]
    
    P3 -.->|Model Data| D3[(Model<br/>Storage)]
    
    P4 -.->|Results| D4[(Analysis<br/>Database)]
    D4 -.->|History| P5
    
    P6 -.->|Query| D4
    D4 -.->|Statistics| P6
    
    P4 -->|Email Data| Email[Email<br/>Service]
    
    style User fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Admin fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style P1 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P2 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P3 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style P4 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P5 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P6 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style D1 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style D2 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style D3 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style D4 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style Email fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 2. Level 1 DFD - Major processes in the Skin Cancer Prediction System showing data flows between processes and data stores.

---

## Level 2: Detailed Process Breakdown

### Level 2.0 - Image Processing & Prediction (Process 2.0 & 3.0)

```mermaid
graph TB
    User([User]) -->|Raw Image| P21[2.1<br/>Image<br/>Upload]
    
    P21 -->|Uploaded Image| P22[2.2<br/>Image<br/>Validation]
    
    P22 -->|Valid Image| P23[2.3<br/>Image<br/>Preprocessing]
    P22 -->|Invalid| Error1[Error<br/>Handler]
    Error1 -->|Error Message| User
    
    P23 -->|Resized Image<br/>224x224| P24[2.4<br/>Normalization]
    
    P24 -->|Normalized Data| P31[3.1<br/>Model<br/>Selection]
    
    P31 -->|Selected Model| P32[3.2<br/>Feature<br/>Extraction]
    
    P32 -->|Features| P33[3.3<br/>Classification]
    
    P33 -->|Raw Predictions| P34[3.4<br/>Confidence<br/>Calculation]
    
    P34 -->|Results| P35[3.5<br/>Grad-CAM<br/>Generation]
    
    P35 -->|Complete Results| P4[4.0<br/>Result<br/>Analysis]
    
    P21 -.->|Store| D2[(Image<br/>Storage)]
    P31 -.->|Load| D3[(Model<br/>Storage)]
    P35 -.->|Save| D4[(Results<br/>Database)]
    
    style User fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style P21 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P22 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P23 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P24 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P31 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style P32 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style P33 fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
    style P34 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style P35 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style P4 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Error1 fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style D2 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style D3 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style D4 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 3. Level 2 DFD - Detailed breakdown of image processing and AI prediction processes.

---

### Level 2.1 - User Authentication (Process 1.0)

```mermaid
graph TB
    User([User]) -->|Credentials| P11[1.1<br/>Login<br/>Validation]
    
    P11 -->|Valid| P12[1.2<br/>Session<br/>Creation]
    P11 -->|Invalid| P13[1.3<br/>Error<br/>Response]
    
    P12 -->|Session Token| P14[1.4<br/>Access<br/>Control]
    
    P14 -->|Authorized| User
    P13 -->|Error Message| User
    
    User -->|Registration Data| P15[1.5<br/>User<br/>Registration]
    
    P15 -->|New User| P16[1.6<br/>Email<br/>Verification]
    
    P16 -->|OTP| Email[Email<br/>Service]
    Email -->|Verification Code| User
    
    User -->|OTP Code| P17[1.7<br/>Verify<br/>OTP]
    
    P17 -->|Verified| P12
    P17 -->|Failed| P13
    
    P11 -.->|Query| D1[(User<br/>Database)]
    P15 -.->|Store| D1
    P12 -.->|Update| D1
    
    style User fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style P11 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P12 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P13 fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style P14 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P15 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P16 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P17 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style D1 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style Email fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 4. Level 2 DFD - User authentication process including registration and email verification.

---

### Level 2.2 - Result Analysis & Reporting (Process 4.0)

```mermaid
graph TB
    P3[3.0<br/>AI Prediction] -->|Raw Results| P41[4.1<br/>Result<br/>Formatting]
    
    P41 -->|Formatted Data| P42[4.2<br/>Risk<br/>Assessment]
    
    P42 -->|Risk Level| P43[4.3<br/>Recommendation<br/>Generation]
    
    P43 -->|Recommendations| P44[4.4<br/>Report<br/>Generation]
    
    P44 -->|PDF Report| P45[4.5<br/>Report<br/>Storage]
    
    P45 -->|Report Link| P46[4.6<br/>Email<br/>Notification]
    
    P46 -->|Email Data| Email[Email<br/>Service]
    Email -->|Notification| User([User])
    
    P44 -->|Display Data| User
    
    P41 -.->|Store| D4[(Analysis<br/>Database)]
    P45 -.->|Save| D5[(Report<br/>Storage)]
    
    P42 -->|AI Query| AI[AI Assistant<br/>Service]
    AI -->|Insights| P43
    
    style P3 fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style P41 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P42 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P43 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P44 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P45 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P46 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style User fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style D4 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style D5 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style Email fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style AI fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 5. Level 2 DFD - Result analysis and reporting process with AI-powered recommendations.

---

### Level 2.3 - Admin Dashboard (Process 6.0)

```mermaid
graph TB
    Admin([Admin]) -->|Login| P61[6.1<br/>Admin<br/>Authentication]
    
    P61 -->|Authorized| P62[6.2<br/>Dashboard<br/>View]
    
    P62 -->|Request| P63[6.3<br/>Analytics<br/>Generation]
    
    P63 -->|Statistics| P64[6.4<br/>Data<br/>Visualization]
    
    P64 -->|Charts & Graphs| Admin
    
    Admin -->|Export Request| P65[6.5<br/>Report<br/>Export]
    
    P65 -->|CSV/PDF| Admin
    
    Admin -->|User Query| P66[6.6<br/>User<br/>Management]
    
    P66 -->|User List| Admin
    
    Admin -->|Model Query| P67[6.7<br/>Model<br/>Performance]
    
    P67 -->|Metrics| Admin
    
    P61 -.->|Verify| D1[(User<br/>Database)]
    P63 -.->|Query| D4[(Analysis<br/>Database)]
    P66 -.->|Query| D1
    P67 -.->|Query| D4
    P67 -.->|Load| D3[(Model<br/>Storage)]
    
    style Admin fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style P61 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P62 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P63 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P64 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P65 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P66 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style P67 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style D1 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style D3 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style D4 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 6. Level 2 DFD - Admin dashboard processes for system management and analytics.

---

## Data Dictionary

### External Entities

| Entity | Description |
|--------|-------------|
| **User/Patient** | End user who uploads skin images for diagnosis |
| **Administrator** | System admin who manages users and monitors system |

### Processes

| Process | Name | Description |
|---------|------|-------------|
| **1.0** | User Authentication | Handles login, registration, and access control |
| **2.0** | Image Processing | Validates and preprocesses uploaded images |
| **3.0** | AI Model Prediction | Performs classification using EfficientNetB0 |
| **4.0** | Result Analysis | Analyzes predictions and generates reports |
| **5.0** | History Management | Manages user's analysis history |
| **6.0** | Admin Dashboard | Provides system analytics and management |

### Data Stores

| Store | Name | Contents |
|-------|------|----------|
| **D1** | User Database | User credentials, profiles, sessions |
| **D2** | Image Storage | Uploaded skin lesion images |
| **D3** | Model Storage | Trained AI models (EfficientNetB0, DenseNet) |
| **D4** | Analysis Database | Prediction results, history, reports |
| **D5** | Report Storage | Generated PDF reports |

### Data Flows

| Flow | Description | Data Elements |
|------|-------------|---------------|
| **Skin Image** | User uploads image | Image file, metadata |
| **Preprocessed Image** | Normalized image data | 224×224×3 tensor |
| **Prediction Results** | AI model output | Class probabilities, confidence |
| **Diagnosis Report** | Final analysis | Classification, risk, recommendations |
| **Auth Token** | Session authentication | JWT token, user ID |

---

## Usage Instructions

### Export for IEEE Paper

1. **Visit** [Mermaid Live Editor](https://mermaid.live/)
2. **Copy** any diagram code above
3. **Paste** into editor
4. **Export** as SVG (vector) or PNG (300+ DPI)
5. **Insert** into your paper

### LaTeX Example

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.9\textwidth]{dfd_level0.pdf}
    \caption{Level 0 DFD showing system context.}
    \label{fig:dfd0}
\end{figure}
```

---

## DFD Notation Guide

| Symbol | Meaning | Representation |
|--------|---------|----------------|
| **Circle** | Process | Transforms data |
| **Rectangle** | External Entity | Source/destination of data |
| **Parallel Lines** | Data Store | Repository of data |
| **Arrow** | Data Flow | Movement of data |
| **Dashed Arrow** | Data Store Access | Read/write operations |

---

**Color Scheme:** Professional grayscale (IEEE compliant)
- Entities: Light gray (#f0f0f0)
- Processes: White to medium gray (#ffffff - #e0e0e0)
- Data Stores: Light gray (#e8e8e8)
- AI Processes: Medium gray (#d0d0d0)

**Optimized for:** IEEE journal submission, print, digital viewing
