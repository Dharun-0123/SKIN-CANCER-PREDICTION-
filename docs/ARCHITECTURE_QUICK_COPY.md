# Architecture Diagrams - Quick Copy

## High-Level System Architecture (RECOMMENDED)

```mermaid
graph TB
    subgraph Client["Client Layer"]
        Web[Web Browser]
        Mobile[Mobile Browser]
    end
    
    subgraph Presentation["Presentation Layer"]
        UI[Django Templates<br/>HTML/CSS/JavaScript]
        Static[Static Assets]
    end
    
    subgraph Application["Application Layer"]
        Auth[Authentication]
        Upload[Image Upload]
        Process[Image Processing]
        Predict[AI Prediction]
        Report[Report Generator]
        Admin[Admin Dashboard]
    end
    
    subgraph AI["AI/ML Layer"]
        Model1[EfficientNetB0]
        Model2[DenseNet]
        Preprocess[Preprocessor]
        GradCAM[Grad-CAM]
    end
    
    subgraph Data["Data Layer"]
        DB[(Database)]
        FileStore[(File Storage)]
        ModelStore[(Model Storage)]
    end
    
    subgraph External["External Services"]
        Email[Email Service]
        AIAssist[AI Assistant]
    end
    
    Web --> UI
    Mobile --> UI
    UI --> Auth
    UI --> Upload
    UI --> Admin
    Auth --> DB
    Upload --> Process
    Process --> Preprocess
    Preprocess --> Predict
    Predict --> Model1
    Predict --> Model2
    Model1 --> ModelStore
    Model2 --> ModelStore
    Predict --> GradCAM
    GradCAM --> Report
    Report --> FileStore
    Report --> DB
    Report --> Email
    Report --> AIAssist
    Admin --> DB
    Admin --> FileStore
    Upload --> FileStore
    
    style Client fill:#f0f0f0,stroke:#333,stroke-width:2px
    style Presentation fill:#ffffff,stroke:#333,stroke-width:2px
    style Application fill:#e8e8e8,stroke:#333,stroke-width:2px
    style AI fill:#d0d0d0,stroke:#333,stroke-width:2px
    style Data fill:#e8e8e8,stroke:#333,stroke-width:2px
    style External fill:#f5f5f5,stroke:#333,stroke-width:2px
```

---

## ER Diagram (Database Schema)

```mermaid
erDiagram
    USER ||--o{ ANALYSIS : performs
    USER ||--o{ OTP : receives
    USER {
        int id PK
        string username UK
        string email UK
        string password
        string first_name
        string last_name
        datetime date_joined
        boolean is_active
        boolean email_verified
    }
    
    ANALYSIS ||--|| RESULT : generates
    ANALYSIS {
        int id PK
        int user_id FK
        string image_path
        string model_used
        datetime analysis_date
        string status
        float processing_time
    }
    
    RESULT {
        int id PK
        int analysis_id FK
        string predicted_class
        float confidence_score
        json class_probabilities
        string gradcam_path
        string report_path
        json ai_recommendations
    }
    
    OTP {
        int id PK
        int user_id FK
        string otp_code
        string purpose
        datetime created_at
        datetime expires_at
        boolean is_used
    }
```

---

## Technology Stack

```mermaid
graph TB
    subgraph Frontend
        HTML[HTML5]
        CSS[CSS3/Bootstrap]
        JS[JavaScript/jQuery]
    end
    
    subgraph Backend
        Python[Python 3.x]
        Django[Django 4.x]
        DjangoORM[Django ORM]
    end
    
    subgraph AI
        TF[TensorFlow 2.x]
        Keras[Keras API]
        NumPy[NumPy]
        OpenCV[OpenCV]
    end
    
    subgraph Database
        SQLite[SQLite 3]
    end
    
    Frontend --> Django
    Python --> Django
    Django --> DjangoORM
    DjangoORM --> SQLite
    Django --> TF
    TF --> Keras
    
    style Frontend fill:#f0f0f0,stroke:#333,stroke-width:2px
    style Backend fill:#ffffff,stroke:#333,stroke-width:2px
    style AI fill:#e0e0e0,stroke:#333,stroke-width:2px
    style Database fill:#e8e8e8,stroke:#333,stroke-width:2px
```

---

## Quick Export

1. Copy diagram code
2. Go to https://mermaid.live/
3. Export as SVG or PNG (300 DPI)
4. Insert in IEEE paper

---

## Figure Captions

**System Architecture:**
> Fig. 1. High-level system architecture showing layered structure with client, presentation, application, AI/ML, data, and external service layers.

**ER Diagram:**
> Fig. 2. Entity-Relationship diagram illustrating database schema with USER, ANALYSIS, RESULT, and OTP entities and their relationships.

**Technology Stack:**
> Fig. 3. Technology stack architecture showing frontend, backend, AI/ML, and database technologies used in the system.

---

**All diagrams use IEEE-compliant grayscale!** ✓
