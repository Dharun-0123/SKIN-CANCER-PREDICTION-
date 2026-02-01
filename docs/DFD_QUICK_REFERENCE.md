# DFD Quick Reference - Copy & Paste

## Level 0 - Context Diagram (RECOMMENDED FOR OVERVIEW)

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

---

## Level 1 - Major Processes

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

---

## Quick Export Steps

1. Copy diagram code above
2. Go to https://mermaid.live/
3. Paste code
4. Export as SVG or PNG (300 DPI)
5. Use in your IEEE paper

---

## Figure Captions (IEEE Style)

**Level 0:**
> Fig. 1. Context diagram of the Skin Cancer Prediction System showing external entities and their interactions with the system.

**Level 1:**
> Fig. 2. Level 1 DFD showing major processes including user authentication, image processing, AI prediction, result analysis, history management, and admin dashboard.

**Level 2 (Image Processing):**
> Fig. 3. Detailed DFD of image processing and AI prediction processes showing data transformation from raw image upload to final classification results.

---

## DFD Symbols

- **( )** = External Entity (User, Admin)
- **(( ))** = Main System
- **[ ]** = Process
- **[( )]** = Data Store
- **→** = Data Flow
- **-.->** = Data Store Access

---

**All diagrams use IEEE-compliant grayscale colors!** ✓
