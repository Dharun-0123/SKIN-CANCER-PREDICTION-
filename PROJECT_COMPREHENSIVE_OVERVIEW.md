# 🩺 SkinCare AI - Comprehensive Project Overview

## 📋 Table of Contents
1. [Abstract](#abstract)
2. [Synopsis](#synopsis)
3. [Problem Statement](#problem-statement)
4. [Objectives](#objectives)
5. [System Architecture](#system-architecture)
6. [Module Details](#module-details)
7. [Dataset Information](#dataset-information)
8. [Machine Learning Models](#machine-learning-models)
9. [Hardware Requirements](#hardware-requirements)
10. [Software Requirements](#software-requirements)
11. [Technology Stack](#technology-stack)
12. [Features & Functionality](#features--functionality)
13. [Database Schema](#database-schema)
14. [Security Implementation](#security-implementation)
15. [Future Enhancements](#future-enhancements)

---

## 📝 Abstract

**SkinCare AI** is an advanced web-based skin cancer detection system that leverages deep learning and convolutional neural networks (CNNs) to analyze dermoscopic images of skin lesions. The system provides instant, AI-powered classification of skin conditions, helping users identify potential skin abnormalities early for timely medical consultation.

The application employs a dual-model architecture combining EfficientNetB0 (trained on 25,331 images from the ISIC 2019 dataset) and a custom CNN model (trained on 3,297 images) to achieve robust and accurate predictions across 8 different skin condition categories. The system features intelligent model selection, confidence scoring, and legally-compliant result presentation to ensure responsible AI usage in healthcare contexts.

Built with Django framework and TensorFlow/Keras for deep learning, the platform offers a modern, responsive user interface with features including user authentication, analysis history tracking, PDF report generation, analytics dashboard, and an AI-powered chatbot assistant (DermaGenie) for skin health guidance.

**Keywords:** Skin Cancer Detection, Deep Learning, Convolutional Neural Networks, EfficientNetB0, Transfer Learning, Medical Image Analysis, Django, TensorFlow

---

## 📖 Synopsis

### Project Title
**SkinCare AI - AI-Powered Skin Lesion Classification System**

### Domain
Healthcare / Medical Imaging / Artificial Intelligence

### Project Type
Web Application with Machine Learning Backend

### Duration
Academic Year 2024-2025

### Brief Description
SkinCare AI is a comprehensive skin cancer detection platform that combines state-of-the-art deep learning models with a user-friendly web interface. The system allows users to upload images of skin lesions and receive instant AI-powered analysis, including:

- Classification into 8 skin condition categories
- Confidence scores for predictions
- Educational information about detected conditions
- Prevention and precautionary guidelines
- Historical tracking of all analyses
- PDF report generation for medical consultations
- AI chatbot for skin health queries

The project addresses the critical need for early skin cancer detection, which significantly improves treatment outcomes. By making preliminary screening accessible through a web application, SkinCare AI aims to encourage users to seek professional medical evaluation when potential concerns are identified.

---

## 🎯 Problem Statement

### Background
Skin cancer is one of the most common forms of cancer globally, with over 5 million cases diagnosed annually in the United States alone. Early detection is crucial for successful treatment, with melanoma survival rates exceeding 99% when detected early versus 27% for late-stage diagnosis.

### Challenges Addressed
1. **Limited Access to Dermatologists**: Many regions lack sufficient dermatological specialists
2. **Delayed Diagnosis**: Long wait times for specialist appointments can delay critical diagnoses
3. **Lack of Awareness**: Many people are unaware of warning signs for skin cancer
4. **Cost Barriers**: Professional skin screenings can be expensive and inaccessible
5. **Visual Similarity**: Different skin conditions can appear similar to untrained eyes

### Solution Approach
SkinCare AI provides an accessible, AI-powered preliminary screening tool that:
- Offers instant analysis of skin lesion images
- Educates users about various skin conditions
- Encourages professional medical consultation when concerns are identified
- Maintains analysis history for tracking changes over time

---

## 🎯 Objectives

### Primary Objectives
1. Develop an accurate deep learning model for skin lesion classification
2. Create a user-friendly web interface for image upload and analysis
3. Implement secure user authentication and data management
4. Provide educational information about skin conditions
5. Generate professional reports for medical consultations

### Secondary Objectives
1. Implement analytics dashboard for tracking analysis trends
2. Develop AI chatbot for skin health guidance
3. Enable comparison of multiple analyses
4. Ensure mobile responsiveness and accessibility
5. Maintain legal compliance with medical disclaimer requirements

---

## 🏗️ System Architecture

### High-Level Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   Browser   │  │   Mobile    │  │   Tablet    │              │
│  │  (Desktop)  │  │   Browser   │  │   Browser   │              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          └────────────────┼────────────────┘
                           │ HTTPS
┌──────────────────────────┼──────────────────────────────────────┐
│                    WEB SERVER LAYER                              │
│  ┌───────────────────────┴───────────────────────┐              │
│  │              Django Web Server                 │              │
│  │         (Views, Templates, Static)             │              │
│  └───────────────────────┬───────────────────────┘              │
└──────────────────────────┼──────────────────────────────────────┘
                           │
┌──────────────────────────┼──────────────────────────────────────┐
│                  APPLICATION LAYER                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │    User     │  │   Image     │  │    Email    │              │
│  │ Management  │  │  Processing │  │   Service   │              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
│         │                │                │                      │
│  ┌──────┴────────────────┴────────────────┴──────┐              │
│  │              Business Logic Layer              │              │
│  └───────────────────────┬───────────────────────┘              │
└──────────────────────────┼──────────────────────────────────────┘
                           │
┌──────────────────────────┼──────────────────────────────────────┐
│                    ML/AI LAYER                                   │
│  ┌─────────────────────────────────────────────┐                │
│  │           TensorFlow/Keras Engine            │                │
│  │  ┌─────────────────┐  ┌─────────────────┐   │                │
│  │  │  EfficientNetB0 │  │    CNN Model    │   │                │
│  │  │  (Primary)      │  │   (Secondary)   │   │                │
│  │  │  224x224 input  │  │   48x48 input   │   │                │
│  │  │  8 classes      │  │   8 classes     │   │                │
│  │  └─────────────────┘  └─────────────────┘   │                │
│  └───────────────────────┬─────────────────────┘                │
└──────────────────────────┼──────────────────────────────────────┘
                           │
┌──────────────────────────┼──────────────────────────────────────┐
│                    DATA LAYER                                    │
│  ┌─────────────────┐  ┌─────────────────┐                       │
│  │   SQLite DB     │  │   File Storage  │                       │
│  │  (User Data,    │  │  (Images,       │                       │
│  │   Predictions)  │  │   Models)       │                       │
│  └─────────────────┘  └─────────────────┘                       │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow Diagram
```
User Upload Image → Image Preprocessing → Model Selection →
→ Primary Model (EfficientNetB0) → Confidence Check →
→ [If Low Confidence] → Secondary Model (CNN) →
→ Result Formatting → Legal Compliance Check →
→ Display Results → Store in Database → Send Notification
```

---

## 📦 Module Details

### 1. User Authentication Module
**Purpose:** Secure user registration, login, and session management

**Components:**
- User Registration with email verification (OTP-based)
- Login/Logout functionality
- Password reset with OTP verification
- Session management
- Admin authentication (separate login)

**Files:**
- `views.py`: Register_2, Login_3, Admin_Login, verify_email
- `otp_utils.py`: OTP generation and verification
- `password_reset_utils.py`: Password reset functionality

### 2. Image Analysis Module
**Purpose:** Core skin lesion classification functionality

**Components:**
- Image upload and validation
- Image preprocessing (resizing, normalization)
- Dual-model prediction system
- Confidence scoring
- Result formatting with legal compliance

**Files:**
- `views.py`: Deploy_8, analysis_results
- `models.py`: predict function, UserPredictModel
- `result_formatter.py`: Legal-compliant result generation

### 3. User Profile Module
**Purpose:** User profile management and statistics

**Components:**
- Profile information management
- Profile picture upload
- Statistics tracking (total analyses, recent activity)
- Notification preferences

**Files:**
- `views.py`: Profile
- `models.py`: UserProfile
- `forms.py`: ProfileUpdateForm

### 4. Analytics Dashboard Module
**Purpose:** Data visualization and trend analysis

**Components:**
- Condition distribution charts
- Analysis trends over time
- Activity tracking
- Interactive Chart.js visualizations

**Files:**
- `views.py`: Analytics
- `analytics.html`: Dashboard template

### 5. History & Comparison Module
**Purpose:** Track and compare past analyses

**Components:**
- Analysis history listing
- Side-by-side comparison
- Filtering and sorting
- PDF export functionality

**Files:**
- `views.py`: Out_Database_9, Compare, CompareData
- `pdf_utils.py`: PDF generation

### 6. Admin Dashboard Module
**Purpose:** System administration and monitoring

**Components:**
- User management
- System statistics
- Analysis monitoring
- Staff-only access control

**Files:**
- `views.py`: AdminDashboard
- `admin_dashboard.html`: Admin interface

### 7. DermaGenie AI Assistant Module
**Purpose:** AI-powered chatbot for skin health queries

**Components:**
- Natural language processing
- Perplexity AI integration
- Conversation history
- Context-aware responses

**Files:**
- `views.py`: DermaGenie, DermaGenieChat
- `ai_assistant.py`: AI integration
- `dermagenie.html`: Chat interface

### 8. Email Notification Module
**Purpose:** Automated email communications

**Components:**
- Welcome emails
- Analysis notifications (first analysis only)
- Profile update notifications
- OTP delivery
- Resend API integration

**Files:**
- `email_utils.py`: Email sending functions
- `otp_utils.py`: OTP email delivery

---

## 📊 Dataset Information

### Primary Dataset: ISIC 2019 (International Skin Imaging Collaboration)

**Total Images:** 25,331 dermoscopic images

**Class Distribution:**
| Class | Full Name | Images | Percentage |
|-------|-----------|--------|------------|
| NV | Melanocytic Nevi | 12,875 | 50.8% |
| MEL | Melanoma | 4,522 | 17.9% |
| BCC | Basal Cell Carcinoma | 3,323 | 13.1% |
| BKL | Benign Keratosis-like Lesions | 2,624 | 10.4% |
| AK | Actinic Keratoses | 867 | 3.4% |
| SCC | Squamous Cell Carcinoma | 628 | 2.5% |
| VASC | Vascular Lesions | 253 | 1.0% |
| DF | Dermatofibroma | 239 | 0.9% |

**Image Specifications:**
- Format: JPEG
- Resolution: Variable (standardized to 224x224 for training)
- Color Space: RGB
- Source: Dermoscopic imaging devices

### Secondary Dataset: Modified HAM10000 Subset

**Base Source:** HAM10000 (Human Against Machine with 10000 training images)

**Original Publication:** Tschandl, P., Rosendahl, C. & Kittler, H. "The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions." *Sci Data* 5, 180161 (2018). https://doi.org/10.1038/sdata.2018.161

**Kaggle Source:** "Skin Cancer MNIST: HAM10000" dataset

**Total Images:** ~5,906 images (subset of original 10,015 HAM10000 images, ~59%)

**Modification:** This dataset is a curated subset of the original HAM10000 with an additional custom "not_skin_cancer" class added for negative classification capability.

**Class Distribution (from training notebook):**
| Class | Full Name | Images | Source |
|-------|-----------|--------|--------|
| nv | Melanocytic Nevi | 2,499 | HAM10000 |
| mel | Melanoma | 1,113 | HAM10000 |
| bkl | Benign Keratosis | 1,100 | HAM10000 |
| bcc | Basal Cell Carcinoma | 515 | HAM10000 |
| akiec | Actinic Keratoses | 328 | HAM10000 |
| vasc | Vascular Lesions | 142 | HAM10000 |
| df | Dermatofibroma | 116 | HAM10000 |
| not_skin_cancer | Not Skin Cancer | 93 | **Custom Addition** |

**Data Preprocessing:**
- Image resizing (48x48 for CNN, 224x224 for EfficientNetB0)
- Normalization (pixel values scaled to 0-1)
- Data augmentation (rotation, flipping, zoom)
- Train/Validation/Test split (70/15/15)

---

## 🤖 Machine Learning Models

### Primary Model: EfficientNetB0

**Architecture:**
- Base: EfficientNetB0 (pre-trained on ImageNet)
- Transfer Learning approach
- Custom classification head

**Specifications:**
| Parameter | Value |
|-----------|-------|
| Input Shape | 224 × 224 × 3 |
| Output Classes | 8 |
| Total Parameters | ~5.3M |
| Trainable Parameters | ~4.0M |
| Test Accuracy | 71.32% |
| Training Epochs | 50 |
| Batch Size | 32 |
| Optimizer | Adam |
| Learning Rate | 0.0001 |

**Model Layers:**
```
EfficientNetB0 (frozen base) →
GlobalAveragePooling2D →
Dense(256, ReLU) →
Dropout(0.5) →
Dense(8, Softmax)
```

### Secondary Model: Custom CNN

**Architecture:**
- Custom Convolutional Neural Network
- 3 Convolutional blocks
- Fully connected classifier

**Specifications:**
| Parameter | Value |
|-----------|-------|
| Input Shape | 48 × 48 × 3 |
| Output Classes | 8 |
| Total Parameters | ~1.2M |
| Test Accuracy | 94.1% |
| Training Epochs | 100 |
| Batch Size | 64 |
| Optimizer | Adam |
| Learning Rate | 0.001 |

**Model Layers:**
```
Conv2D(32, 3×3) → ReLU → MaxPool2D →
Conv2D(64, 3×3) → ReLU → MaxPool2D →
Conv2D(128, 3×3) → ReLU → MaxPool2D →
Flatten →
Dense(256, ReLU) → Dropout(0.5) →
Dense(8, Softmax)
```

### Model Selection Logic
```python
if user_preference == 'efficientnet':
    use EfficientNetB0
elif user_preference == 'cnn':
    use CNN
else:  # Auto mode
    try EfficientNetB0 first
    if confidence > 0.5:
        use EfficientNetB0 result
    else:
        fallback to CNN
```

---

## 💻 Hardware Requirements

### Minimum Requirements
| Component | Specification |
|-----------|---------------|
| Processor | Intel Core i5 / AMD Ryzen 5 |
| RAM | 8 GB |
| Storage | 10 GB free space |
| GPU | Not required (CPU inference) |
| Display | 1366 × 768 resolution |
| Network | Broadband internet connection |

### Recommended Requirements
| Component | Specification |
|-----------|---------------|
| Processor | Intel Core i7 / AMD Ryzen 7 |
| RAM | 16 GB |
| Storage | 20 GB SSD |
| GPU | NVIDIA GTX 1060 or better (for training) |
| Display | 1920 × 1080 resolution |
| Network | High-speed internet connection |

### Server Requirements (Production)
| Component | Specification |
|-----------|---------------|
| CPU | 4+ cores |
| RAM | 16 GB minimum |
| Storage | 50 GB SSD |
| GPU | Optional (NVIDIA T4 for faster inference) |
| OS | Ubuntu 20.04 LTS / Windows Server 2019 |

---

## 🛠️ Software Requirements

### Development Environment
| Software | Version | Purpose |
|----------|---------|---------|
| Python | 3.10+ | Primary programming language |
| pip | Latest | Package management |
| Git | 2.30+ | Version control |
| VS Code / PyCharm | Latest | IDE |
| Node.js | 16+ | Frontend tooling (optional) |

### Backend Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| Django | 4.2.1 | Web framework |
| TensorFlow | 2.13.0 | Deep learning framework |
| Keras | 2.13.1 | Neural network API |
| Pillow | 10.0.0 | Image processing |
| NumPy | 1.24.3 | Numerical computing |
| OpenCV | 4.8.0 | Computer vision |
| scikit-learn | 1.3.0 | Machine learning utilities |
| pandas | 2.0.3 | Data manipulation |
| matplotlib | 3.7.2 | Visualization |
| seaborn | 0.12.2 | Statistical visualization |
| python-dotenv | 1.0.0 | Environment variables |

### Frontend Technologies
| Technology | Purpose |
|------------|---------|
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript (ES6+) | Interactivity |
| Chart.js | Data visualization |
| Font Awesome | Icons |
| Google Fonts | Typography |

### External Services
| Service | Purpose |
|---------|---------|
| Resend | Email delivery |
| Perplexity AI | Chatbot responses |
| SQLite | Database (development) |
| PostgreSQL | Database (production) |

---

## 🔧 Technology Stack

### Backend
```
┌─────────────────────────────────────┐
│           Django 4.2.1              │
│  ┌─────────────────────────────┐   │
│  │    Django REST Framework    │   │
│  │    (API endpoints)          │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │    Django ORM               │   │
│  │    (Database abstraction)   │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

### Machine Learning
```
┌─────────────────────────────────────┐
│         TensorFlow 2.13.0           │
│  ┌─────────────────────────────┐   │
│  │         Keras 2.13.1        │   │
│  │  ┌───────────────────────┐  │   │
│  │  │    EfficientNetB0     │  │   │
│  │  │    Custom CNN         │  │   │
│  │  └───────────────────────┘  │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

### Frontend
```
┌─────────────────────────────────────┐
│     Modern Responsive UI            │
│  ┌─────────────────────────────┐   │
│  │  HTML5 + CSS3 + JavaScript  │   │
│  │  ┌───────────────────────┐  │   │
│  │  │  Chart.js (Charts)    │  │   │
│  │  │  Font Awesome (Icons) │  │   │
│  │  │  Custom Animations    │  │   │
│  │  └───────────────────────┘  │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

---

## ✨ Features & Functionality

### Core Features
| Feature | Description | Status |
|---------|-------------|--------|
| Skin Lesion Analysis | AI-powered classification of skin images | ✅ Complete |
| 8 Condition Detection | Identifies 8 different skin conditions | ✅ Complete |
| Dual Model System | EfficientNetB0 + CNN for robust predictions | ✅ Complete |
| Confidence Scoring | Displays prediction confidence percentage | ✅ Complete |
| User Authentication | Secure registration and login | ✅ Complete |
| Email Verification | OTP-based email verification | ✅ Complete |
| Password Reset | Secure password recovery | ✅ Complete |

### Advanced Features
| Feature | Description | Status |
|---------|-------------|--------|
| User Profiles | Personal info, profile pictures, stats | ✅ Complete |
| Analysis History | Track all past analyses | ✅ Complete |
| PDF Export | Generate professional reports | ✅ Complete |
| Comparison Tool | Compare multiple analyses | ✅ Complete |
| Analytics Dashboard | Charts and trend analysis | ✅ Complete |
| DermaGenie AI | AI chatbot for skin health | ✅ Complete |
| Admin Dashboard | System monitoring (staff only) | ✅ Complete |
| Email Notifications | Automated email alerts | ✅ Complete |

### UI/UX Features
| Feature | Description | Status |
|---------|-------------|--------|
| Dark Futuristic Theme | Modern, professional appearance | ✅ Complete |
| Responsive Design | Mobile, tablet, desktop support | ✅ Complete |
| Floating Video Background | Premium landing page effect | ✅ Complete |
| Tooltips & Guidance | Contextual help throughout | ✅ Complete |
| Legal Disclaimers | Compliant result presentation | ✅ Complete |

---

## 🗄️ Database Schema

### Entity Relationship Diagram
```
┌─────────────────┐       ┌─────────────────┐
│      User       │       │   UserProfile   │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │──1:1──│ id (PK)         │
│ username        │       │ user_id (FK)    │
│ email           │       │ bio             │
│ password        │       │ phone           │
│ is_staff        │       │ date_of_birth   │
│ is_superuser    │       │ profile_picture │
│ date_joined     │       │ email_verified  │
└────────┬────────┘       │ email_notifs    │
         │                │ first_email_sent│
         │                │ created_at      │
         │                │ updated_at      │
         │                └─────────────────┘
         │
         │ 1:N
         ▼
┌─────────────────┐       ┌─────────────────┐
│ UserPredictModel│       │  ChatConversation│
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ user_id (FK)    │       │ user_id (FK)    │
│ image           │       │ user_message    │
│ label           │       │ ai_response     │
│ model_preference│       │ tokens_used     │
│ model_used      │       │ model           │
│ confidence_score│       │ created_at      │
│ created_at      │       └─────────────────┘
└─────────────────┘
         │
         │ 1:1
         ▼
┌─────────────────┐       ┌─────────────────┐
│    EmailOTP     │       │PasswordResetOTP │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ user_id (FK)    │       │ user_id (FK)    │
│ otp             │       │ otp             │
│ created_at      │       │ created_at      │
│ is_verified     │       │ is_used         │
└─────────────────┘       └─────────────────┘
```

---

## 🔒 Security Implementation

### Authentication Security
- Password hashing using Django's PBKDF2 algorithm
- Session-based authentication with CSRF protection
- OTP-based email verification (6-digit, 10-minute expiry)
- Separate admin authentication flow
- Login attempt rate limiting

### Data Security
- HTTPS enforcement in production
- SQL injection prevention via Django ORM
- XSS protection through template escaping
- CSRF tokens on all forms
- Secure file upload handling
- Environment variables for sensitive data

### Privacy Compliance
- User data encryption at rest
- Secure image storage
- Data retention policies
- User consent for email notifications
- GDPR-compliant data handling

---

## 🚀 Future Enhancements

### Short-term (3-6 months)
1. **Mobile Application**: Native iOS/Android apps
2. **Multi-language Support**: Internationalization
3. **Enhanced Analytics**: More detailed trend analysis
4. **API Access**: RESTful API for third-party integration
5. **Batch Processing**: Multiple image analysis

### Medium-term (6-12 months)
1. **Model Improvements**: Higher accuracy models
2. **Real-time Analysis**: Webcam-based analysis
3. **Telemedicine Integration**: Connect with dermatologists
4. **Wearable Integration**: Smartwatch compatibility
5. **Offline Mode**: Local model inference

### Long-term (12+ months)
1. **3D Skin Mapping**: Full-body lesion tracking
2. **Predictive Analytics**: Risk assessment over time
3. **Clinical Integration**: EHR system connectivity
4. **Research Platform**: Data sharing for research
5. **AI Model Marketplace**: Custom model deployment

---

## 📚 References

1. ISIC Archive - International Skin Imaging Collaboration (Primary model dataset)
2. EfficientNet: Rethinking Model Scaling for CNNs (Tan & Le, 2019)
3. Django Documentation - https://docs.djangoproject.com/
4. TensorFlow Documentation - https://www.tensorflow.org/
5. Skin Cancer Foundation - https://www.skincancer.org/

---

## 📄 License & Disclaimer

### License
This project is developed for educational purposes.

### Medical Disclaimer
⚠️ **IMPORTANT**: SkinCare AI is designed for educational and informational purposes only. It does NOT provide medical diagnoses, treatment recommendations, or professional medical advice. Results are AI predictions based on image analysis and should NOT be used as a substitute for professional medical evaluation.

**Always consult a qualified dermatologist or healthcare provider for proper medical evaluation, diagnosis, and treatment of any skin concerns.**

---

## 👥 Project Team

**Project Title:** SkinCare AI - AI-Powered Skin Lesion Classification System

**Institution:** [Your Institution Name]

**Academic Year:** 2024-2025

---

*Document Version: 1.0*
*Last Updated: January 2026*