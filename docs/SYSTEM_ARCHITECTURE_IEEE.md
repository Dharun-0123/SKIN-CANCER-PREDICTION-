# System Architecture & Database Schema - IEEE Format

## High-Level System Architecture

```mermaid
graph TB
    subgraph Client["Client Layer"]
        Web[Web Browser]
        Mobile[Mobile Browser]
    end
    
    subgraph Presentation["Presentation Layer"]
        UI[Django Templates<br/>HTML/CSS/JavaScript]
        Static[Static Assets<br/>Images, CSS, JS]
    end
    
    subgraph Application["Application Layer"]
        Auth[Authentication<br/>Module]
        Upload[Image Upload<br/>Handler]
        Process[Image Processing<br/>Module]
        Predict[AI Prediction<br/>Engine]
        Report[Report Generator]
        Admin[Admin Dashboard]
    end
    
    subgraph AI["AI/ML Layer"]
        Model1[EfficientNetB0<br/>Model]
        Model2[DenseNet<br/>Model]
        Preprocess[Image<br/>Preprocessor]
        GradCAM[Grad-CAM<br/>Generator]
    end
    
    subgraph Data["Data Layer"]
        DB[(SQLite<br/>Database)]
        FileStore[(File Storage<br/>Images & Reports)]
        ModelStore[(Model Storage<br/>.h5 Files)]
    end
    
    subgraph External["External Services"]
        Email[Email Service<br/>Resend API]
        AIAssist[AI Assistant<br/>OpenAI/Perplexity]
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
    
    style Client fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Presentation fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Application fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style AI fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
    style Data fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style External fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 1. High-level system architecture showing the layered structure of the Skin Cancer Prediction System.

---

## Detailed Component Architecture

```mermaid
graph TB
    subgraph Frontend["Frontend Components"]
        Landing[Landing Page]
        Register[Registration]
        Login[Login]
        Dashboard[User Dashboard]
        Analyze[Analysis Page]
        Results[Results Page]
        History[History Page]
        Profile[Profile Page]
        AdminUI[Admin Dashboard]
    end
    
    subgraph Backend["Backend Services"]
        Django[Django Framework]
        Views[View Controllers]
        Models[Data Models]
        Forms[Form Handlers]
        Utils[Utility Functions]
    end
    
    subgraph Core["Core Modules"]
        AuthMod[Authentication<br/>- Login/Register<br/>- OTP Verification<br/>- Password Reset]
        
        ImageMod[Image Processing<br/>- Upload Handler<br/>- Validation<br/>- Preprocessing]
        
        AIMod[AI Engine<br/>- Model Selection<br/>- Prediction<br/>- Grad-CAM]
        
        ReportMod[Report Module<br/>- Result Formatting<br/>- PDF Generation<br/>- Email Sending]
        
        HistoryMod[History Module<br/>- Data Retrieval<br/>- Comparison<br/>- Export]
    end
    
    subgraph Storage["Storage Layer"]
        UserDB[(User Data)]
        AnalysisDB[(Analysis Data)]
        ImageFS[(Image Files)]
        ReportFS[(Report Files)]
        ModelFS[(AI Models)]
    end
    
    Frontend --> Django
    Django --> Views
    Views --> Models
    Views --> Forms
    Views --> Utils
    
    Views --> AuthMod
    Views --> ImageMod
    Views --> AIMod
    Views --> ReportMod
    Views --> HistoryMod
    
    AuthMod --> UserDB
    ImageMod --> ImageFS
    AIMod --> ModelFS
    AIMod --> AnalysisDB
    ReportMod --> ReportFS
    ReportMod --> AnalysisDB
    HistoryMod --> AnalysisDB
    
    style Frontend fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Backend fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Core fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style Storage fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 2. Detailed component architecture showing frontend, backend, core modules, and storage layers.

---

## Technology Stack Architecture

```mermaid
graph TB
    subgraph Frontend["Frontend Technologies"]
        HTML[HTML5]
        CSS[CSS3<br/>Bootstrap]
        JS[JavaScript<br/>jQuery]
    end
    
    subgraph Backend["Backend Framework"]
        Python[Python 3.x]
        Django[Django 4.x]
        DjangoORM[Django ORM]
    end
    
    subgraph AI["AI/ML Stack"]
        TF[TensorFlow 2.x]
        Keras[Keras API]
        NumPy[NumPy]
        OpenCV[OpenCV]
    end
    
    subgraph Database["Database"]
        SQLite[SQLite 3]
    end
    
    subgraph APIs["External APIs"]
        Resend[Resend Email API]
        OpenAI[OpenAI API]
        Perplexity[Perplexity API]
    end
    
    subgraph Deployment["Deployment"]
        Server[Web Server<br/>Gunicorn/uWSGI]
        Static[Static Files<br/>WhiteNoise]
    end
    
    Frontend --> Django
    Python --> Django
    Django --> DjangoORM
    DjangoORM --> SQLite
    
    Django --> TF
    TF --> Keras
    Keras --> NumPy
    Keras --> OpenCV
    
    Django --> Resend
    Django --> OpenAI
    Django --> Perplexity
    
    Django --> Server
    Django --> Static
    
    style Frontend fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Backend fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style AI fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style Database fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style APIs fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style Deployment fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 3. Technology stack showing frontend, backend, AI/ML, database, and deployment technologies.

---

## Entity-Relationship Diagram (ER Diagram)

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
        boolean is_staff
        boolean email_verified
        datetime last_login
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
        boolean is_first_analysis
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
        datetime created_at
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
    
    ADMIN_LOG ||--o{ USER : tracks
    ADMIN_LOG {
        int id PK
        int admin_id FK
        string action
        string target_user
        datetime timestamp
        string ip_address
    }
```

**Caption:** Fig. 4. Entity-Relationship diagram showing database schema and relationships between entities.

---

## Database Schema (Detailed)

```mermaid
erDiagram
    AUTH_USER {
        INTEGER id PK "Primary Key"
        VARCHAR username "Unique, Max 150"
        VARCHAR email "Unique, Max 254"
        VARCHAR password "Hashed, Max 128"
        VARCHAR first_name "Max 150"
        VARCHAR last_name "Max 150"
        DATETIME date_joined "Auto Now Add"
        BOOLEAN is_active "Default True"
        BOOLEAN is_staff "Default False"
        BOOLEAN is_superuser "Default False"
        DATETIME last_login "Nullable"
    }
    
    USER_PROFILE {
        INTEGER id PK
        INTEGER user_id FK "One-to-One"
        BOOLEAN email_verified "Default False"
        DATETIME email_verified_at "Nullable"
        BOOLEAN first_analysis_email_sent "Default False"
        TEXT profile_picture "Nullable"
        TEXT bio "Nullable"
    }
    
    SKIN_ANALYSIS {
        INTEGER id PK
        INTEGER user_id FK
        VARCHAR image_path "Max 500"
        VARCHAR model_used "Max 50"
        DATETIME analysis_date "Auto Now Add"
        VARCHAR status "Max 20"
        FLOAT processing_time "Nullable"
        BOOLEAN is_first_analysis "Default False"
        TEXT notes "Nullable"
    }
    
    ANALYSIS_RESULT {
        INTEGER id PK
        INTEGER analysis_id FK "One-to-One"
        VARCHAR predicted_class "Max 50"
        FLOAT confidence_score "0-1 Range"
        JSON class_probabilities "All 8 Classes"
        VARCHAR gradcam_path "Max 500"
        VARCHAR report_path "Max 500"
        JSON ai_recommendations "Nullable"
        TEXT risk_assessment "Nullable"
        DATETIME created_at "Auto Now Add"
        DATETIME updated_at "Auto Now"
    }
    
    OTP_VERIFICATION {
        INTEGER id PK
        INTEGER user_id FK
        VARCHAR otp_code "6 Digits"
        VARCHAR purpose "Max 50"
        DATETIME created_at "Auto Now Add"
        DATETIME expires_at "5 Min Expiry"
        BOOLEAN is_used "Default False"
        VARCHAR ip_address "Max 45"
    }
    
    ADMIN_ACTIVITY_LOG {
        INTEGER id PK
        INTEGER admin_id FK
        VARCHAR action "Max 100"
        VARCHAR target_user "Max 150"
        DATETIME timestamp "Auto Now Add"
        VARCHAR ip_address "Max 45"
        TEXT details "JSON Format"
    }
    
    AUTH_USER ||--|| USER_PROFILE : has
    AUTH_USER ||--o{ SKIN_ANALYSIS : performs
    AUTH_USER ||--o{ OTP_VERIFICATION : receives
    AUTH_USER ||--o{ ADMIN_ACTIVITY_LOG : creates
    SKIN_ANALYSIS ||--|| ANALYSIS_RESULT : generates
```

**Caption:** Fig. 5. Detailed database schema with field types, constraints, and relationships.

---

## Data Flow Architecture

```mermaid
graph LR
    subgraph Input["Input Layer"]
        User[User Input]
        Image[Skin Image]
    end
    
    subgraph Processing["Processing Pipeline"]
        Validate[Validation]
        Resize[Resize 224x224]
        Normalize[Normalization]
        Augment[Augmentation]
    end
    
    subgraph AI["AI Processing"]
        ModelSelect[Model Selection]
        Inference[Inference]
        PostProcess[Post-Processing]
    end
    
    subgraph Output["Output Layer"]
        Results[Classification]
        Confidence[Confidence Score]
        Visualization[Grad-CAM]
        Report[PDF Report]
    end
    
    subgraph Storage["Persistent Storage"]
        DB[(Database)]
        Files[(File System)]
    end
    
    User --> Validate
    Image --> Validate
    Validate --> Resize
    Resize --> Normalize
    Normalize --> Augment
    Augment --> ModelSelect
    ModelSelect --> Inference
    Inference --> PostProcess
    PostProcess --> Results
    PostProcess --> Confidence
    PostProcess --> Visualization
    Results --> Report
    Confidence --> Report
    Visualization --> Report
    
    Report --> DB
    Report --> Files
    Image --> Files
    
    style Input fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Processing fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style AI fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style Output fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Storage fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 6. Data flow architecture showing the complete processing pipeline from input to output.

---

## Deployment Architecture

```mermaid
graph TB
    subgraph Internet["Internet"]
        Users[End Users]
    end
    
    subgraph WebServer["Web Server Layer"]
        Nginx[Nginx<br/>Reverse Proxy]
        SSL[SSL/TLS<br/>Certificate]
    end
    
    subgraph AppServer["Application Server"]
        Gunicorn[Gunicorn<br/>WSGI Server]
        Django[Django<br/>Application]
    end
    
    subgraph Services["Services"]
        Static[Static Files<br/>WhiteNoise]
        Media[Media Files<br/>Storage]
        Cache[Cache<br/>Optional]
    end
    
    subgraph Database["Database Layer"]
        SQLite[(SQLite<br/>Database)]
        Backup[(Backup<br/>Storage)]
    end
    
    subgraph External["External Services"]
        Email[Email API<br/>Resend]
        AI[AI APIs<br/>OpenAI/Perplexity]
        CDN[CDN<br/>Optional]
    end
    
    Users --> Nginx
    Nginx --> SSL
    SSL --> Gunicorn
    Gunicorn --> Django
    
    Django --> Static
    Django --> Media
    Django --> Cache
    Django --> SQLite
    
    SQLite --> Backup
    
    Django --> Email
    Django --> AI
    Static --> CDN
    
    style Internet fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style WebServer fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style AppServer fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style Services fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style Database fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
    style External fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 7. Deployment architecture showing web server, application server, services, and external integrations.

---

## Security Architecture

```mermaid
graph TB
    subgraph User["User Layer"]
        Browser[Web Browser]
    end
    
    subgraph Security["Security Layer"]
        HTTPS[HTTPS/TLS<br/>Encryption]
        CSRF[CSRF<br/>Protection]
        XSS[XSS<br/>Prevention]
        Auth[Authentication<br/>JWT/Session]
    end
    
    subgraph Application["Application Layer"]
        Input[Input<br/>Validation]
        Sanitize[Data<br/>Sanitization]
        Authorize[Authorization<br/>Checks]
        Encrypt[Password<br/>Hashing]
    end
    
    subgraph Data["Data Layer"]
        DB[(Encrypted<br/>Database)]
        Files[(Secure<br/>File Storage)]
    end
    
    Browser --> HTTPS
    HTTPS --> CSRF
    CSRF --> XSS
    XSS --> Auth
    
    Auth --> Input
    Input --> Sanitize
    Sanitize --> Authorize
    Authorize --> Encrypt
    
    Encrypt --> DB
    Authorize --> Files
    
    style User fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style Security fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style Application fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Data fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 8. Security architecture showing multiple layers of protection including encryption, authentication, and data validation.

---

## Database Tables Summary

| Table | Purpose | Key Fields | Relationships |
|-------|---------|------------|---------------|
| **AUTH_USER** | User authentication | id, username, email, password | → USER_PROFILE, SKIN_ANALYSIS |
| **USER_PROFILE** | Extended user info | user_id, email_verified | ← AUTH_USER |
| **SKIN_ANALYSIS** | Analysis records | id, user_id, image_path, model_used | ← AUTH_USER, → ANALYSIS_RESULT |
| **ANALYSIS_RESULT** | Prediction results | analysis_id, predicted_class, confidence | ← SKIN_ANALYSIS |
| **OTP_VERIFICATION** | Email verification | user_id, otp_code, expires_at | ← AUTH_USER |
| **ADMIN_ACTIVITY_LOG** | Admin actions | admin_id, action, timestamp | ← AUTH_USER |

---

## System Specifications

### Performance Metrics
- **Response Time:** < 3 seconds for prediction
- **Concurrent Users:** Up to 100 simultaneous
- **Image Processing:** 224×224 RGB images
- **Model Inference:** ~500ms per image
- **Database:** SQLite (upgradable to PostgreSQL)

### Scalability
- **Horizontal:** Load balancer + multiple app servers
- **Vertical:** Increase server resources
- **Database:** Migration path to PostgreSQL/MySQL
- **Storage:** Cloud storage integration (S3, Azure)

### Security Features
- HTTPS/TLS encryption
- CSRF protection
- XSS prevention
- SQL injection protection
- Password hashing (PBKDF2)
- OTP-based email verification
- Session management
- Input validation

---

**All diagrams use IEEE-compliant grayscale colors for professional publication.**
