# Layered System Architecture - IEEE Format

## Complete Layered Architecture (Based on Your Design)

```mermaid
graph TB
    subgraph ClientLayer["CLIENT LAYER"]
        Browser[Desktop Browser]
        Mobile[Mobile Browser]
        Tablet[Tablet Browser]
    end
    
    subgraph WebServerLayer["WEB SERVER LAYER"]
        Django[Django Web Server<br/>Views, Templates, Static]
    end
    
    subgraph ApplicationLayer["APPLICATION LAYER"]
        UserMgmt[User Management]
        ImageProc[Image Processing]
        EmailSvc[Email Service]
        BusinessLogic[Business Logic Layer]
    end
    
    subgraph MLAILayer["ML/AI LAYER"]
        TFEngine[TensorFlow/Keras Engine]
        
        subgraph Models["AI Models"]
            EfficientNet[EfficientNetB0<br/>Primary Model<br/>224×224 input<br/>8 classes]
            CNN[CNN Model<br/>Secondary<br/>48×48 input<br/>8 classes]
        end
    end
    
    subgraph DataLayer["DATA LAYER"]
        SQLite[(SQLite Database<br/>User Data, Predictions)]
        FileStorage[(File Storage<br/>Images, Models)]
    end
    
    Browser -->|HTTPS| Django
    Mobile -->|HTTPS| Django
    Tablet -->|HTTPS| Django
    
    Django --> UserMgmt
    Django --> ImageProc
    Django --> EmailSvc
    
    UserMgmt --> BusinessLogic
    ImageProc --> BusinessLogic
    EmailSvc --> BusinessLogic
    
    BusinessLogic --> TFEngine
    TFEngine --> EfficientNet
    TFEngine --> CNN
    
    BusinessLogic --> SQLite
    BusinessLogic --> FileStorage
    
    EfficientNet -.->|Load Model| FileStorage
    CNN -.->|Load Model| FileStorage
    
    style ClientLayer fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style WebServerLayer fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style ApplicationLayer fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style MLAILayer fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
    style DataLayer fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style Models fill:#c0c0c0,stroke:#333,stroke-width:1px,color:#000
    
    style Browser fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Mobile fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Tablet fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style Django fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style UserMgmt fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style ImageProc fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style EmailSvc fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style BusinessLogic fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style TFEngine fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style EfficientNet fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style CNN fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style SQLite fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style FileStorage fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 1. Five-layer system architecture showing client, web server, application, ML/AI, and data layers with dual AI model configuration.

---

## Simplified Layered View

```mermaid
graph TB
    Client["CLIENT LAYER<br/>━━━━━━━━━━━━━━━━<br/>Browser | Mobile | Tablet"]
    
    WebServer["WEB SERVER LAYER<br/>━━━━━━━━━━━━━━━━<br/>Django Web Server<br/>Views, Templates, Static"]
    
    Application["APPLICATION LAYER<br/>━━━━━━━━━━━━━━━━<br/>User Management<br/>Image Processing<br/>Email Service<br/>Business Logic"]
    
    MLAI["ML/AI LAYER<br/>━━━━━━━━━━━━━━━━<br/>TensorFlow/Keras Engine<br/>EfficientNetB0 (224×224, 8 classes)<br/>CNN Model (48×48, 8 classes)"]
    
    Data["DATA LAYER<br/>━━━━━━━━━━━━━━━━<br/>SQLite Database<br/>File Storage"]
    
    Client -->|HTTPS| WebServer
    WebServer --> Application
    Application --> MLAI
    MLAI --> Data
    Application --> Data
    
    style Client fill:#f0f0f0,stroke:#333,stroke-width:3px,color:#000
    style WebServer fill:#ffffff,stroke:#333,stroke-width:3px,color:#000
    style Application fill:#e8e8e8,stroke:#333,stroke-width:3px,color:#000
    style MLAI fill:#d0d0d0,stroke:#333,stroke-width:3px,color:#000
    style Data fill:#e8e8e8,stroke:#333,stroke-width:3px,color:#000
```

**Caption:** Fig. 2. Simplified five-layer architecture with clear separation of concerns.

---

## Horizontal Layer Diagram

```mermaid
graph LR
    subgraph Layer1["Layer 1<br/>CLIENT"]
        C1[Browser]
        C2[Mobile]
        C3[Tablet]
    end
    
    subgraph Layer2["Layer 2<br/>WEB SERVER"]
        W1[Django<br/>Server]
    end
    
    subgraph Layer3["Layer 3<br/>APPLICATION"]
        A1[User Mgmt]
        A2[Image Proc]
        A3[Email Svc]
        A4[Business<br/>Logic]
    end
    
    subgraph Layer4["Layer 4<br/>ML/AI"]
        M1[TensorFlow]
        M2[EfficientNetB0<br/>224×224]
        M3[CNN Model<br/>48×48]
    end
    
    subgraph Layer5["Layer 5<br/>DATA"]
        D1[(SQLite)]
        D2[(Files)]
    end
    
    C1 --> W1
    C2 --> W1
    C3 --> W1
    W1 --> A1
    W1 --> A2
    W1 --> A3
    A1 --> A4
    A2 --> A4
    A3 --> A4
    A4 --> M1
    M1 --> M2
    M1 --> M3
    A4 --> D1
    A4 --> D2
    M2 -.-> D2
    M3 -.-> D2
    
    style Layer1 fill:#f0f0f0,stroke:#333,stroke-width:2px
    style Layer2 fill:#ffffff,stroke:#333,stroke-width:2px
    style Layer3 fill:#e8e8e8,stroke:#333,stroke-width:2px
    style Layer4 fill:#d0d0d0,stroke:#333,stroke-width:2px
    style Layer5 fill:#e8e8e8,stroke:#333,stroke-width:2px
    
    style C1 fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style C2 fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style C3 fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style W1 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style A1 fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style A2 fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style A3 fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style A4 fill:#e0e0e0,stroke:#333,stroke-width:1px,color:#000
    style M1 fill:#e0e0e0,stroke:#333,stroke-width:1px,color:#000
    style M2 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style M3 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style D1 fill:#f0f0f0,stroke:#333,stroke-width:1px,color:#000
    style D2 fill:#f0f0f0,stroke:#333,stroke-width:1px,color:#000
```

**Caption:** Fig. 3. Horizontal view of the five-layer architecture showing component interactions.

---

## Detailed Component Breakdown

```mermaid
graph TB
    subgraph L1["LAYER 1: CLIENT"]
        direction LR
        Desktop[Desktop Browser<br/>Chrome, Firefox, Safari]
        Mobile[Mobile Browser<br/>iOS, Android]
        Tablet[Tablet Browser<br/>iPad, Android Tablet]
    end
    
    subgraph L2["LAYER 2: WEB SERVER"]
        Django[Django Web Server]
        Views[Views Controllers]
        Templates[HTML Templates]
        Static[Static Assets<br/>CSS, JS, Images]
    end
    
    subgraph L3["LAYER 3: APPLICATION"]
        Auth[User Management<br/>• Login/Register<br/>• Authentication<br/>• Authorization]
        
        ImgProc[Image Processing<br/>• Upload Handler<br/>• Validation<br/>• Preprocessing]
        
        Email[Email Service<br/>• OTP Verification<br/>• Notifications<br/>• Reports]
        
        BizLogic[Business Logic<br/>• Workflow Control<br/>• Data Validation<br/>• API Integration]
    end
    
    subgraph L4["LAYER 4: ML/AI"]
        TF[TensorFlow/Keras Engine]
        
        Model1[EfficientNetB0<br/>━━━━━━━━━━━<br/>Input: 224×224×3<br/>Output: 8 classes<br/>Primary Model]
        
        Model2[CNN Model<br/>━━━━━━━━━━━<br/>Input: 48×48×3<br/>Output: 8 classes<br/>Secondary Model]
    end
    
    subgraph L5["LAYER 5: DATA"]
        DB[(SQLite Database<br/>━━━━━━━━━━━<br/>• User Data<br/>• Predictions<br/>• Analysis History)]
        
        FS[(File Storage<br/>━━━━━━━━━━━<br/>• Uploaded Images<br/>• AI Models (.h5)<br/>• Generated Reports)]
    end
    
    Desktop --> Django
    Mobile --> Django
    Tablet --> Django
    
    Django --> Views
    Django --> Templates
    Django --> Static
    
    Views --> Auth
    Views --> ImgProc
    Views --> Email
    
    Auth --> BizLogic
    ImgProc --> BizLogic
    Email --> BizLogic
    
    BizLogic --> TF
    TF --> Model1
    TF --> Model2
    
    BizLogic --> DB
    BizLogic --> FS
    Model1 -.->|Load| FS
    Model2 -.->|Load| FS
    
    style L1 fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style L2 fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    style L3 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    style L4 fill:#d0d0d0,stroke:#333,stroke-width:2px,color:#000
    style L5 fill:#e8e8e8,stroke:#333,stroke-width:2px,color:#000
    
    style Desktop fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style Mobile fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style Tablet fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style Django fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style Views fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style Templates fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style Static fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style Auth fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style ImgProc fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style Email fill:#ffffff,stroke:#333,stroke-width:1px,color:#000
    style BizLogic fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style TF fill:#e0e0e0,stroke:#333,stroke-width:2px,color:#000
    style Model1 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style Model2 fill:#f5f5f5,stroke:#333,stroke-width:1px,color:#000
    style DB fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
    style FS fill:#f0f0f0,stroke:#333,stroke-width:2px,color:#000
```

**Caption:** Fig. 4. Detailed component breakdown showing all modules and their interactions across five layers.

---

## Layer Responsibilities

### Layer 1: Client Layer
**Purpose:** User interface and interaction
- Desktop browsers (Chrome, Firefox, Safari)
- Mobile browsers (iOS, Android)
- Tablet browsers
- **Communication:** HTTPS to Web Server

### Layer 2: Web Server Layer
**Purpose:** Request handling and routing
- Django web framework
- View controllers
- Template rendering
- Static file serving
- **Communication:** HTTP/HTTPS

### Layer 3: Application Layer
**Purpose:** Business logic and services
- **User Management:** Authentication, authorization, session management
- **Image Processing:** Upload handling, validation, preprocessing
- **Email Service:** OTP verification, notifications, report delivery
- **Business Logic:** Workflow orchestration, data validation
- **Communication:** Internal function calls

### Layer 4: ML/AI Layer
**Purpose:** Artificial intelligence and prediction
- **TensorFlow/Keras Engine:** Model loading and inference
- **EfficientNetB0:** Primary model (224×224 input, 8 classes)
- **CNN Model:** Secondary model (48×48 input, 8 classes)
- **Communication:** Model API calls

### Layer 5: Data Layer
**Purpose:** Persistent storage
- **SQLite Database:** User data, predictions, analysis history
- **File Storage:** Images, AI models (.h5 files), reports
- **Communication:** Database queries, file I/O

---

## Data Flow Through Layers

```mermaid
sequenceDiagram
    participant C as Client Layer
    participant W as Web Server
    participant A as Application
    participant M as ML/AI Layer
    participant D as Data Layer
    
    C->>W: HTTPS Request<br/>(Upload Image)
    W->>A: Route to Handler
    A->>A: Validate Image
    A->>D: Store Image
    D-->>A: File Path
    A->>M: Preprocess & Predict
    M->>D: Load Model
    D-->>M: Model Data
    M->>M: Run Inference
    M-->>A: Prediction Results
    A->>D: Save Results
    A->>A: Generate Report
    A->>D: Store Report
    A-->>W: Response Data
    W-->>C: HTTPS Response<br/>(Results Page)
```

**Caption:** Fig. 5. Sequence diagram showing data flow through all five layers during image analysis.

---

## Layer Communication Matrix

| From Layer | To Layer | Protocol | Data Type |
|------------|----------|----------|-----------|
| Client | Web Server | HTTPS | HTTP Requests |
| Web Server | Application | Function Calls | Python Objects |
| Application | ML/AI | API Calls | NumPy Arrays |
| Application | Data | SQL/File I/O | Queries/Files |
| ML/AI | Data | File I/O | Model Files |

---

## Technology Stack by Layer

| Layer | Technologies |
|-------|-------------|
| **Client** | HTML5, CSS3, JavaScript, Bootstrap |
| **Web Server** | Django 4.x, Python 3.x, Gunicorn |
| **Application** | Django ORM, Python Libraries |
| **ML/AI** | TensorFlow 2.x, Keras, NumPy, OpenCV |
| **Data** | SQLite 3, File System |

---

## Scalability Considerations

### Horizontal Scaling
- **Client Layer:** Load balancer distribution
- **Web Server:** Multiple Django instances
- **Application:** Stateless service design
- **ML/AI:** Model serving with TensorFlow Serving
- **Data:** Database replication, distributed storage

### Vertical Scaling
- Increase server resources (CPU, RAM, GPU)
- Optimize database queries
- Cache frequently accessed data
- Compress static assets

---

**All diagrams use IEEE-compliant grayscale colors for professional publication.**

**Color Scheme:**
- Client Layer: #f0f0f0 (Light gray)
- Web Server: #ffffff (White)
- Application: #e8e8e8 (Medium light gray)
- ML/AI: #d0d0d0 (Medium gray)
- Data: #e8e8e8 (Medium light gray)
