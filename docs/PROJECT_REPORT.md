# SKINCARE AI: AN AI-POWERED SKIN LESION CLASSIFICATION SYSTEM USING DEEP LEARNING

---

## A PROJECT REPORT

Submitted in partial fulfillment of the requirements for the award of the degree of

**MASTER OF COMPUTER APPLICATIONS (MCA)**

Submitted by

**[Student Name]**
**[Registration Number]**

Under the guidance of

**[Guide Name]**
**[Designation]**

---

**DEPARTMENT OF COMPUTER APPLICATIONS**
**[INSTITUTION NAME]**
**[UNIVERSITY NAME]**
**[CITY, STATE]**

**ACADEMIC YEAR 2024-2025**

---

<!-- PAGE BREAK -->

## CERTIFICATE

This is to certify that the project report entitled **"SKINCARE AI: AN AI-POWERED SKIN LESION CLASSIFICATION SYSTEM USING DEEP LEARNING"** submitted by **[Student Name]** bearing Registration Number **[Registration Number]** in partial fulfillment of the requirements for the award of the degree of **Master of Computer Applications** is a bonafide record of work carried out under my guidance and supervision.

This project report has not been submitted to any other university or institution for the award of any degree or diploma.

&nbsp;

**Date:**

**Place:**

&nbsp;

**[Guide Name]**
**[Designation]**
**Department of Computer Applications**

&nbsp;

**[Head of Department Name]**
**Head of Department**
**Department of Computer Applications**

---

<!-- PAGE BREAK -->

## DECLARATION

I hereby declare that the project report entitled **"SKINCARE AI: AN AI-POWERED SKIN LESION CLASSIFICATION SYSTEM USING DEEP LEARNING"** submitted to **[University Name]** in partial fulfillment of the requirements for the award of the degree of **Master of Computer Applications** is a record of original work done by me under the guidance of **[Guide Name]**, **[Designation]**, Department of Computer Applications, **[Institution Name]**.

I further declare that this project report has not been submitted to any other university or institution for the award of any degree or diploma.

&nbsp;

**Date:**

**Place:**

&nbsp;

**[Student Name]**
**[Registration Number]**

---

<!-- PAGE BREAK -->

## ACKNOWLEDGEMENT

I would like to express my sincere gratitude to all those who have contributed to the successful completion of this project work.

First and foremost, I express my heartfelt thanks to the Almighty for blessing me with the strength, wisdom, and perseverance to complete this project successfully.

I am deeply indebted to my project guide, **[Guide Name]**, **[Designation]**, Department of Computer Applications, for the valuable guidance, constant encouragement, and constructive suggestions throughout the course of this project. The technical expertise and professional approach demonstrated by my guide have been instrumental in shaping this project.

I extend my sincere thanks to **[Head of Department Name]**, Head of the Department of Computer Applications, for providing the necessary facilities and support for the successful completion of this project.

I am grateful to **[Principal Name]**, Principal, **[Institution Name]**, for providing an excellent academic environment and infrastructure that facilitated the completion of this project.

I would like to thank all the faculty members of the Department of Computer Applications for their valuable suggestions and support during the project development phase.

I express my gratitude to the non-teaching staff of the department for their cooperation and assistance in various administrative matters.

I am thankful to my classmates and friends for their moral support, encouragement, and valuable discussions that helped me overcome various challenges during the project development.

Finally, I express my deepest gratitude to my parents and family members for their unconditional love, support, and encouragement throughout my academic journey. Their sacrifices and blessings have been the driving force behind all my achievements.

&nbsp;

**[Student Name]**

---

<!-- PAGE BREAK -->

## ABSTRACT

Skin cancer represents one of the most prevalent forms of cancer worldwide, with millions of new cases diagnosed annually. Early detection of skin cancer significantly improves treatment outcomes and survival rates, with melanoma survival rates exceeding ninety-nine percent when detected at early stages compared to merely twenty-seven percent for late-stage diagnoses. However, access to dermatological expertise remains limited in many regions, creating a critical need for accessible preliminary screening tools.

This project presents SkinCare AI, a comprehensive web-based skin lesion classification system that leverages advanced deep learning techniques to analyze dermoscopic images and provide preliminary assessments of skin conditions. The system employs a dual-model architecture combining EfficientNetB0, a state-of-the-art convolutional neural network pre-trained on ImageNet and fine-tuned on the ISIC 2019 dataset comprising 25,331 dermoscopic images, with a custom Convolutional Neural Network trained on a modified HAM10000 dataset containing 5,906 images.

The proposed system classifies skin lesions into eight distinct categories: Melanocytic Nevi, Melanoma, Basal Cell Carcinoma, Benign Keratosis-like Lesions, Actinic Keratoses, Squamous Cell Carcinoma, Vascular Lesions, and Dermatofibroma. The intelligent model selection mechanism automatically chooses the most appropriate model based on confidence thresholds, ensuring robust predictions across diverse image qualities and conditions.

The web application is developed using the Django framework with Python as the primary programming language, TensorFlow and Keras for deep learning implementation, and SQLite for database management. The system incorporates comprehensive features including secure user authentication with OTP-based email verification, analysis history tracking, PDF report generation, analytics dashboard with interactive visualizations, and an AI-powered chatbot named DermaGenie for skin health guidance.

Experimental results demonstrate that the custom CNN model achieves a test accuracy of 94.1 percent on the secondary dataset, while the EfficientNetB0 model achieves 71.32 percent accuracy on the larger ISIC 2019 dataset. The dual-model approach provides a balance between accuracy and robustness, with the system automatically falling back to the secondary model when primary model confidence is below the threshold.

The system emphasizes responsible AI usage in healthcare contexts by incorporating legally-compliant result presentation, clear medical disclaimers, and recommendations for professional medical consultation. SkinCare AI serves as an educational and preliminary screening tool, encouraging users to seek professional dermatological evaluation when potential concerns are identified.

**Keywords:** Skin Cancer Detection, Deep Learning, Convolutional Neural Networks, EfficientNetB0, Transfer Learning, Medical Image Analysis, Django, TensorFlow, Healthcare AI

---

<!-- PAGE BREAK -->

## TABLE OF CONTENTS

| Chapter | Title | Page No. |
|---------|-------|----------|
| | Certificate | ii |
| | Declaration | iii |
| | Acknowledgement | iv |
| | Abstract | v |
| | Table of Contents | vi |
| | List of Tables | ix |
| | List of Figures | x |
| **1** | **INTRODUCTION** | **1** |
| 1.1 | Introduction Overview | 1 |
| 1.2 | Salient Features of the System | 4 |
| 1.3 | Project Motivation | 7 |
| 1.4 | Scope of the Project | 10 |
| 1.5 | Organization of the Report | 13 |
| **2** | **SYSTEM STUDY AND ANALYSIS** | **15** |
| 2.1 | Problem Statement | 15 |
| 2.2 | Existing System | 18 |
| 2.2.1 | Drawbacks of Existing System | 21 |
| 2.3 | Proposed System | 24 |
| 2.3.1 | Advantages of Proposed System | 27 |
| 2.4 | Feasibility Analysis | 30 |
| 2.4.1 | Technical Feasibility | 30 |
| 2.4.2 | Economic Feasibility | 33 |
| 2.4.3 | Operational Feasibility | 35 |
| **3** | **DEVELOPMENT ENVIRONMENT** | **38** |
| 3.1 | Hardware Requirements | 38 |
| 3.2 | Software Requirements | 41 |
| 3.3 | Software Description | 44 |
| 3.3.1 | About Python | 44 |
| 3.3.2 | About Google Colab | 48 |
| 3.3.3 | About Django | 51 |
| 3.3.4 | About TensorFlow | 55 |
| 3.3.5 | About Database Technology | 59 |
| **4** | **SYSTEM DESIGN** | **63** |
| 4.1 | Module Description | 63 |
| 4.1.1 | User Authentication Module | 63 |
| 4.1.2 | Image Analysis Module | 66 |
| 4.1.3 | User Profile Module | 69 |
| 4.1.4 | Analytics Dashboard Module | 72 |
| 4.1.5 | History and Comparison Module | 75 |
| 4.1.6 | Admin Module | 78 |
| 4.1.7 | AI Chatbot Module | 81 |
| 4.1.8 | Email Notification Module | 84 |
| 4.2 | Methodology | 87 |
| 4.3 | Input Design | 91 |
| 4.4 | Output Design | 94 |
| 4.5 | Data Flow Diagram | 97 |
| 4.6 | Architecture Diagram | 102 |
| 4.7 | Database Design | 107 |
| 4.7.1 | ER Diagram | 107 |
| 4.7.2 | Table Description | 111 |
| **5** | **SYSTEM IMPLEMENTATION** | **116** |
| 5.1 | Frontend Implementation | 116 |
| 5.2 | Backend Implementation | 120 |
| 5.3 | Machine Learning Model Implementation | 124 |
| 5.4 | Model Training Process | 128 |
| 5.5 | Model Evaluation Metrics | 132 |
| 5.6 | Security Implementation | 136 |
| **6** | **SYSTEM TESTING** | **140** |
| 6.1 | Testing Strategy | 140 |
| 6.2 | Unit Testing | 143 |
| 6.3 | Integration Testing | 146 |
| 6.4 | Validation Testing | 149 |
| 6.5 | Test Case Design | 152 |
| 6.6 | Sample Test Cases | 155 |
| **7** | **RESULTS AND DISCUSSION** | **160** |
| 7.1 | Experimental Results | 160 |
| 7.2 | Performance Analysis | 164 |
| 7.3 | Accuracy Analysis | 168 |
| 7.4 | Comparison with Existing Systems | 172 |
| **8** | **CONCLUSION AND FUTURE ENHANCEMENT** | **176** |
| 8.1 | Conclusion | 176 |
| 8.2 | Future Enhancements | 179 |
| **9** | **BIBLIOGRAPHY AND REFERENCES** | **183** |
| **10** | **APPENDICES** | **187** |
| | Appendix A - Output Screens | 187 |
| | Appendix B - Sample Code Snippets | 195 |
| | Appendix C - User Manual | 205 |

---

<!-- PAGE BREAK -->

## LIST OF TABLES

| Table No. | Title | Page No. |
|-----------|-------|----------|
| 2.1 | Comparison of Existing and Proposed System | 29 |
| 3.1 | Minimum Hardware Requirements | 39 |
| 3.2 | Recommended Hardware Requirements | 40 |
| 3.3 | Software Requirements | 42 |
| 3.4 | Python Libraries and Dependencies | 47 |
| 4.1 | User Table Structure | 112 |
| 4.2 | UserProfile Table Structure | 113 |
| 4.3 | UserPredictModel Table Structure | 114 |
| 4.4 | EmailOTP Table Structure | 115 |
| 5.1 | EfficientNetB0 Model Specifications | 125 |
| 5.2 | Custom CNN Model Specifications | 126 |
| 5.3 | ISIC 2019 Dataset Distribution | 129 |
| 5.4 | HAM10000 Subset Distribution | 130 |
| 6.1 | User Authentication Test Cases | 156 |
| 6.2 | Image Analysis Test Cases | 157 |
| 6.3 | Profile Management Test Cases | 158 |
| 6.4 | System Integration Test Cases | 159 |
| 7.1 | Model Performance Comparison | 165 |
| 7.2 | Class-wise Accuracy Analysis | 169 |
| 7.3 | Comparison with Related Works | 173 |

---

<!-- PAGE BREAK -->

## LIST OF FIGURES

| Figure No. | Title | Page No. |
|------------|-------|----------|
| 4.1 | System Architecture Diagram | 103 |
| 4.2 | Data Flow Diagram Level 0 | 98 |
| 4.3 | Data Flow Diagram Level 1 | 100 |
| 4.4 | Entity Relationship Diagram | 108 |
| 4.5 | ML Workflow Diagram | 105 |
| 4.6 | Deployment Architecture Diagram | 106 |
| 5.1 | EfficientNetB0 Architecture | 127 |
| 5.2 | Custom CNN Architecture | 127 |
| 5.3 | Training Loss Curve | 131 |
| 5.4 | Training Accuracy Curve | 131 |
| 7.1 | Confusion Matrix - EfficientNetB0 | 166 |
| 7.2 | Confusion Matrix - Custom CNN | 167 |
| 7.3 | ROC Curve Analysis | 170 |
| 7.4 | Precision-Recall Curve | 171 |
| A.1 | Landing Page | 187 |
| A.2 | User Registration Page | 188 |
| A.3 | Login Page | 189 |
| A.4 | Home Dashboard | 190 |
| A.5 | Image Analysis Page | 191 |
| A.6 | Analysis Results Page | 192 |
| A.7 | User Profile Page | 193 |
| A.8 | Analytics Dashboard | 194 |

---

<!-- PAGE BREAK -->

## CHAPTER 1: INTRODUCTION

### 1.1 Introduction Overview

The field of medical imaging has witnessed remarkable advancements in recent years, particularly with the integration of artificial intelligence and deep learning technologies. Among the various applications of these technologies in healthcare, skin cancer detection has emerged as a critical area where automated systems can significantly impact patient outcomes. Skin cancer, characterized by the abnormal growth of skin cells, represents one of the most common forms of cancer globally, affecting millions of individuals each year. The World Health Organization estimates that between two and three million non-melanoma skin cancers and approximately 132,000 melanoma skin cancers occur globally each year. These statistics underscore the urgent need for effective screening and early detection mechanisms.

The human skin, being the largest organ of the body, serves as the primary barrier against environmental hazards and plays a crucial role in maintaining overall health. However, prolonged exposure to ultraviolet radiation from the sun, genetic predisposition, and various environmental factors can lead to the development of

## CHAPTER 1: INTRODUCTION

### 1.1 Introduction Overview

The field of medical imaging has witnessed remarkable advancements in recent years, particularly with the integration of artificial intelligence and deep learning technologies. Among the various applications of these technologies in healthcare, skin cancer detection has emerged as a critical area where automated systems can significantly impact patient outcomes. Skin cancer, characterized by the abnormal growth of skin cells, represents one of the most common forms of cancer globally, affecting millions of individuals each year. The World Health Organization estimates that between two and three million non-melanoma skin cancers and approximately 132,000 melanoma skin cancers occur globally each year.

The human skin, being the largest organ of the body, serves as the primary barrier against environmental hazards and plays a crucial role in maintaining overall health. However, prolonged exposure to ultraviolet radiation from the sun, genetic predisposition, and various environmental factors can lead to the development of abnormal skin growths that may potentially become cancerous. The early identification of these abnormal growths is paramount for successful treatment and improved patient outcomes.

Traditional methods of skin cancer diagnosis rely heavily on visual examination by trained dermatologists, followed by dermoscopic analysis and histopathological examination of biopsied tissue samples. While these methods remain the gold standard for diagnosis, they present several challenges including limited availability of dermatological expertise in rural and underserved areas, subjective interpretation that may vary among practitioners, and the time-consuming nature of the diagnostic process. These limitations have created a pressing need for automated screening tools that can assist in the preliminary assessment of skin lesions.

The advent of deep learning, particularly Convolutional Neural Networks, has revolutionized the field of medical image analysis. These sophisticated algorithms can learn complex patterns and features from large datasets of medical images, enabling them to identify subtle characteristics that may be indicative of malignancy. Research has demonstrated that well-trained deep learning models can achieve diagnostic accuracy comparable to, and in some cases exceeding, that of experienced dermatologists.

SkinCare AI represents a comprehensive solution that harnesses the power of deep learning to provide accessible, preliminary skin lesion screening. The system is designed as a web-based application that allows users to upload images of skin lesions and receive instant AI-powered analysis. By combining state-of-the-art neural network architectures with a user-friendly interface, SkinCare AI aims to bridge the gap between advanced medical technology and everyday users who may benefit from early screening.

The system employs a dual-model architecture that combines the strengths of two distinct neural network models. The primary model utilizes EfficientNetB0, a highly efficient convolutional neural network architecture that has demonstrated excellent performance on image classification tasks while maintaining computational efficiency. This model has been pre-trained on the ImageNet dataset and subsequently fine-tuned on the ISIC 2019 dataset, which comprises over 25,000 dermoscopic images representing various skin conditions.

The secondary model is a custom-designed Convolutional Neural Network that has been trained on a modified version of the HAM10000 dataset. This dataset, originally published by Tschandl and colleagues in 2018, contains dermoscopic images of common pigmented skin lesions and has become a benchmark dataset for skin lesion classification research. The custom CNN model provides an alternative classification pathway that can be utilized when the primary model exhibits low confidence in its predictions.

The intelligent model selection mechanism implemented in SkinCare AI automatically evaluates the confidence of predictions from the primary model and determines whether to utilize the secondary model for improved accuracy. This approach ensures that users receive the most reliable predictions possible, regardless of variations in image quality or lesion characteristics.

Beyond the core classification functionality, SkinCare AI incorporates a comprehensive suite of features designed to enhance the user experience and provide valuable insights. These features include secure user authentication with email verification, detailed analysis history tracking, professional PDF report generation for medical consultations, an interactive analytics dashboard for visualizing trends, and an AI-powered chatbot named DermaGenie that provides guidance on skin health topics.

The development of SkinCare AI has been guided by principles of responsible AI usage in healthcare contexts. The system incorporates clear medical disclaimers, emphasizes that results are for educational purposes only, and consistently encourages users to seek professional medical evaluation for any concerns. This approach ensures that the technology serves as a complement to, rather than a replacement for, professional dermatological care.



### 1.2 Salient Features of the System

SkinCare AI incorporates a comprehensive array of features that distinguish it from conventional skin analysis applications and establish it as a sophisticated healthcare technology solution. The system has been designed with careful consideration of user needs, technical requirements, and the sensitive nature of medical information processing. This section provides a detailed examination of the key features that define the SkinCare AI platform.

The dual-model architecture represents one of the most significant technical innovations implemented in SkinCare AI. Unlike traditional single-model systems that may struggle with certain image types or conditions, the dual-model approach provides redundancy and improved accuracy across a wider range of scenarios. The primary model, based on the EfficientNetB0 architecture, has been trained on the extensive ISIC 2019 dataset comprising over 25,000 dermoscopic images. This model excels at identifying subtle patterns and features in high-quality dermoscopic images. The secondary model, a custom-designed Convolutional Neural Network trained on a modified HAM10000 dataset, provides an alternative classification pathway that can be particularly effective for images that may not conform to typical dermoscopic standards.

The intelligent model selection mechanism automatically evaluates the confidence level of predictions from the primary model and determines whether to utilize the secondary model for potentially improved accuracy. This approach ensures that users receive the most reliable predictions possible, regardless of variations in image quality, lighting conditions, or lesion characteristics. The system can operate in three modes: automatic selection, where the system chooses the most appropriate model based on confidence thresholds; EfficientNetB0-only mode, where users specifically request analysis using the primary model; and CNN-only mode, where users prefer the secondary model for their analysis.

The classification capability of SkinCare AI extends to eight distinct categories of skin conditions, providing comprehensive coverage of the most common skin lesions encountered in clinical practice. These categories include Melanocytic Nevi, which are commonly known as moles and represent benign proliferations of melanocytes; Melanoma, the most dangerous form of skin cancer that develops from melanocytes; Basal Cell Carcinoma, the most common type of skin cancer that rarely metastasizes but can cause significant local tissue destruction; Benign Keratosis-like Lesions, which include seborrheic keratoses and other benign growths; Actinic Keratoses, precancerous lesions that can develop into squamous cell carcinoma; Squamous Cell Carcinoma, the second most common form of skin cancer; Vascular Lesions, which include various blood vessel-related skin conditions; and Dermatofibroma, benign fibrous nodules commonly found on the lower extremities.


The user authentication and security framework implemented in SkinCare AI ensures that sensitive health information remains protected while providing a seamless user experience. The registration process incorporates email verification using One-Time Passwords, ensuring that users provide valid email addresses and preventing unauthorized account creation. The OTP system generates secure six-digit codes that expire after ten minutes, balancing security requirements with user convenience. Password management follows industry best practices, with passwords being hashed using Django's PBKDF2 algorithm before storage, ensuring that even in the unlikely event of a database breach, user credentials remain protected.

The analysis history and tracking functionality enables users to maintain a comprehensive record of all their skin analyses over time. This feature is particularly valuable for monitoring changes in existing lesions or tracking the appearance of new skin conditions. Each analysis record includes the original uploaded image, the classification result, confidence scores, the model used for analysis, and the timestamp of the analysis. Users can easily access their complete history through an intuitive interface that supports filtering and sorting by various criteria including date, condition type, and confidence level.

The PDF report generation capability allows users to create professional, printable reports of their analysis results that can be shared with healthcare providers during medical consultations. These reports include all relevant information from the analysis, presented in a clear and professional format that facilitates communication between patients and their healthcare providers. The reports incorporate appropriate medical disclaimers and clearly indicate that the results are from an AI-based preliminary screening tool rather than a professional medical diagnosis.

The analytics dashboard provides users with visual representations of their analysis data, enabling them to identify patterns and trends over time. The dashboard utilizes Chart.js to create interactive visualizations including pie charts showing the distribution of detected conditions, line graphs displaying analysis frequency over time, and bar charts comparing confidence levels across different analyses. These visualizations help users understand their skin health patterns and can be valuable for discussions with healthcare providers.


The DermaGenie AI assistant represents an innovative feature that provides users with an intelligent conversational interface for skin health queries. Powered by the Perplexity AI platform, DermaGenie can answer questions about various skin conditions, provide general skin care guidance, explain medical terminology, and offer educational information about skin health. The chatbot maintains conversation context, allowing for natural, flowing discussions about skin health topics. Importantly, DermaGenie is programmed to consistently remind users that its responses are for educational purposes only and should not replace professional medical advice.

The email notification system keeps users informed about important events and updates related to their account and analyses. The system utilizes the Resend API for reliable email delivery and includes features such as welcome emails for new users, notifications for first-time analyses, profile update confirmations, and OTP delivery for authentication purposes. Users have control over their notification preferences and can opt out of non-essential communications while still receiving critical security-related emails.

The responsive design ensures that SkinCare AI provides an optimal user experience across all device types, from desktop computers to tablets and smartphones. The interface automatically adapts to different screen sizes and orientations, ensuring that all features remain accessible and usable regardless of the device being used. Special attention has been paid to touch-friendly interfaces for mobile users, with appropriately sized buttons and touch targets that facilitate easy navigation on smaller screens.

The administrative dashboard provides system administrators with comprehensive tools for monitoring and managing the SkinCare AI platform. Administrators can view system-wide statistics including total users, total analyses performed, and recent activity trends. The dashboard also provides user management capabilities, allowing administrators to view user accounts, monitor usage patterns, and address any issues that may arise. Access to the administrative dashboard is restricted to staff members through a separate authentication flow, ensuring that sensitive system information remains protected.

---

<!-- PAGE BREAK -->

### 1.3 Project Motivation


The motivation for developing SkinCare AI stems from a confluence of factors including the growing global burden of skin cancer, the limitations of current healthcare delivery systems, and the remarkable advances in artificial intelligence that have made sophisticated medical image analysis accessible to a broader audience. This section explores the various factors that motivated the development of this project and the underlying rationale for the design decisions that shaped the final system.

Skin cancer represents a significant and growing public health challenge worldwide. According to the World Health Organization, the incidence of both melanoma and non-melanoma skin cancers has been increasing steadily over the past several decades. In the United States alone, it is estimated that one in five Americans will develop skin cancer by the age of seventy. The American Cancer Society projects that approximately 97,610 new melanomas will be diagnosed in the United States in 2023, with an estimated 7,990 deaths resulting from the disease. These statistics underscore the urgent need for effective screening and early detection mechanisms that can help identify potential skin cancers before they progress to more advanced and dangerous stages.

The critical importance of early detection in skin cancer outcomes cannot be overstated. When melanoma is detected at its earliest stage, before it has penetrated the epidermis, the five-year survival rate exceeds ninety-nine percent. However, when melanoma is detected at later stages after it has spread to distant organs, the five-year survival rate drops dramatically to approximately twenty-seven percent. This stark difference in outcomes based on the stage of detection highlights the life-saving potential of early screening and the value of tools that can encourage individuals to seek professional evaluation when potential concerns are identified.

Despite the clear benefits of early detection, access to dermatological expertise remains limited in many regions around the world. In the United States, there is approximately one dermatologist for every 30,000 people, with significant geographic disparities that leave many rural and underserved communities with limited access to specialized skin care. In developing countries, the situation is often more severe, with some regions having fewer than one dermatologist per million people. This shortage of dermatological expertise creates barriers to timely screening and diagnosis, potentially allowing skin cancers to progress to more advanced stages before they are identified.


The economic burden of skin cancer treatment adds another dimension to the motivation for developing accessible screening tools. The cost of treating skin cancer in the United States is estimated at over eight billion dollars annually, with costs increasing significantly for cancers detected at later stages. Early detection not only improves patient outcomes but also reduces the overall cost of treatment, as early-stage skin cancers can often be treated with relatively simple outpatient procedures compared to the extensive treatments required for advanced cancers. By encouraging early screening and professional consultation, tools like SkinCare AI have the potential to contribute to reduced healthcare costs while improving patient outcomes.

The rapid advancement of artificial intelligence and deep learning technologies has created unprecedented opportunities for developing sophisticated medical image analysis systems. Convolutional Neural Networks have demonstrated remarkable capabilities in image classification tasks, with some studies showing that well-trained models can achieve diagnostic accuracy comparable to or exceeding that of experienced dermatologists. The availability of large, well-curated datasets of dermoscopic images, such as the ISIC archive and the HAM10000 dataset, has facilitated the development of robust models that can generalize across diverse patient populations and imaging conditions.

The democratization of deep learning frameworks and cloud computing resources has made it possible to develop and deploy sophisticated AI systems without requiring extensive specialized infrastructure. Frameworks such as TensorFlow and Keras provide accessible interfaces for building and training neural networks, while transfer learning techniques allow developers to leverage pre-trained models that have been trained on massive datasets. These technological advances have lowered the barriers to entry for developing medical AI applications, enabling projects like SkinCare AI to be developed within academic and research settings.

The increasing prevalence of smartphones with high-quality cameras has created new opportunities for mobile health applications. Modern smartphones can capture images of sufficient quality for preliminary skin analysis, making it possible for users to perform initial screenings from the comfort of their homes. This accessibility is particularly valuable for individuals who may face barriers to accessing traditional healthcare services, whether due to geographic isolation, time constraints, or economic factors. By providing a web-based platform that can be accessed from any device with a camera and internet connection, SkinCare AI aims to make preliminary skin screening accessible to a broader population.


The educational aspect of skin health awareness represents another important motivation for this project. Many individuals lack awareness of the warning signs of skin cancer and may not recognize when a skin lesion warrants professional evaluation. By providing educational information about various skin conditions alongside analysis results, SkinCare AI aims to improve skin health literacy and empower users to make informed decisions about their healthcare. The DermaGenie AI assistant further supports this educational mission by providing a conversational interface for users to learn about skin health topics.

The responsible development of AI in healthcare contexts requires careful consideration of ethical implications and potential risks. The motivation for SkinCare AI includes a commitment to developing a system that enhances rather than replaces professional medical care. The system is designed to encourage users to seek professional evaluation when concerns are identified, rather than to provide definitive diagnoses that might discourage appropriate medical consultation. This approach reflects an understanding that AI-based screening tools are most valuable when they serve as a bridge to professional care rather than as a substitute for it.

---

<!-- PAGE BREAK -->

### 1.4 Scope of the Project

The scope of the SkinCare AI project encompasses the design, development, and deployment of a comprehensive web-based skin lesion classification system that leverages deep learning technologies to provide preliminary assessments of skin conditions. This section delineates the boundaries of the project, clarifying what is included within its scope and what falls outside the intended functionality of the system.

The primary scope of SkinCare AI includes the development of a dual-model deep learning system capable of classifying dermoscopic images into eight distinct categories of skin conditions. The system is designed to process images uploaded by users through a web interface, apply appropriate preprocessing transformations, and generate classification predictions along with confidence scores. The classification categories include Melanocytic Nevi, Melanoma, Basal Cell Carcinoma, Benign Keratosis-like Lesions, Actinic Keratoses, Squamous Cell Carcinoma, Vascular Lesions, and Dermatofibroma. The system provides educational information about each condition and recommends appropriate next steps based on the classification results.


The web application development scope includes the creation of a complete user-facing interface built using the Django framework. This encompasses user registration and authentication functionality with email verification, user profile management, image upload and analysis interfaces, analysis history tracking and management, PDF report generation, analytics dashboard with interactive visualizations, and the DermaGenie AI chatbot interface. The application is designed to be responsive and accessible across desktop, tablet, and mobile devices.

The machine learning component scope includes the training and optimization of two distinct neural network models. The primary model utilizes the EfficientNetB0 architecture with transfer learning from ImageNet weights, fine-tuned on the ISIC 2019 dataset. The secondary model is a custom Convolutional Neural Network trained on a modified HAM10000 dataset. The scope includes the development of an intelligent model selection mechanism that automatically chooses the most appropriate model based on confidence thresholds and user preferences.

The administrative functionality scope includes the development of a staff-only dashboard for system monitoring and management. This dashboard provides system-wide statistics, user management capabilities, and analysis monitoring tools. The administrative interface is protected by a separate authentication flow to ensure that sensitive system information remains accessible only to authorized personnel.

The email notification system scope includes the integration of the Resend API for reliable email delivery. The system supports various notification types including welcome emails, analysis notifications, profile update confirmations, and OTP delivery for authentication purposes. Users have control over their notification preferences through their profile settings.

The security implementation scope includes the development of comprehensive security measures to protect user data and ensure system integrity. This encompasses password hashing, session management, CSRF protection, input validation, secure file upload handling, and environment variable management for sensitive configuration data.


Several important limitations define what falls outside the scope of SkinCare AI. The system is explicitly not intended to provide medical diagnoses or treatment recommendations. All results are presented as preliminary assessments for educational purposes only, with clear disclaimers emphasizing the need for professional medical evaluation. The system does not replace the expertise of qualified dermatologists or other healthcare providers, and users are consistently encouraged to seek professional consultation for any skin concerns.

The scope does not include the analysis of non-dermoscopic images or images of conditions outside the eight supported categories. While the system can process various image types, it has been trained specifically on dermoscopic images and may not provide accurate results for other image types. The system does not support real-time video analysis or webcam-based screening, although these features are identified as potential future enhancements.

The current scope is limited to a web-based application and does not include native mobile applications for iOS or Android platforms. While the web application is designed to be mobile-responsive and accessible from mobile browsers, dedicated mobile applications with features such as offline analysis or camera integration are outside the current scope.

The scope does not include integration with electronic health record systems or telemedicine platforms. While the PDF report generation feature facilitates sharing of results with healthcare providers, direct integration with clinical systems is not included in the current implementation.

The geographic scope of the system is not limited to any specific region, although the interface is currently available only in English. Internationalization and multi-language support are identified as potential future enhancements but are not included in the current scope.

The scope includes deployment on local development servers and provides guidance for production deployment, but does not include the actual deployment to production cloud infrastructure or the ongoing maintenance and support of a production system.

---

<!-- PAGE BREAK -->

### 1.5 Organization of the Report


This project report is organized into ten chapters, each addressing a specific aspect of the SkinCare AI system development. The structure follows a logical progression from introduction and analysis through design, implementation, testing, and conclusion, providing a comprehensive documentation of the entire project lifecycle.

Chapter One, Introduction, provides an overview of the SkinCare AI project, including the context and background of skin cancer detection, the salient features of the developed system, the motivation behind the project, the scope and limitations, and the organization of this report. This chapter establishes the foundation for understanding the subsequent technical discussions.

Chapter Two, System Study and Analysis, presents a detailed analysis of the problem domain and the requirements for the proposed solution. This chapter includes the formal problem statement, an examination of existing systems and their limitations, a description of the proposed system and its advantages, and a comprehensive feasibility analysis covering technical, economic, and operational aspects.

Chapter Three, Development Environment, documents the hardware and software requirements for developing and running the SkinCare AI system. This chapter provides detailed descriptions of the key technologies used in the project, including Python, Google Colab, Django, TensorFlow, and the database technology employed.

Chapter Four, System Design, presents the architectural and design decisions that shaped the SkinCare AI system. This chapter includes detailed module descriptions for all major system components, the methodology employed in development, input and output design specifications, data flow diagrams at multiple levels, the system architecture diagram, and the database design including entity-relationship diagrams and table descriptions.

Chapter Five, System Implementation, documents the actual implementation of the SkinCare AI system. This chapter covers frontend implementation details, backend implementation specifics, machine learning model implementation, the model training process, model evaluation metrics, and security implementation measures.


Chapter Six, System Testing, describes the testing strategies and procedures employed to ensure the quality and reliability of the SkinCare AI system. This chapter covers the overall testing strategy, unit testing procedures, integration testing approaches, validation testing methods, test case design principles, and sample test cases with expected and actual results.

Chapter Seven, Results and Discussion, presents the experimental results obtained from the SkinCare AI system and provides analysis and interpretation of these results. This chapter includes experimental results from model training and evaluation, performance analysis of the system, accuracy analysis across different conditions and scenarios, and comparison with existing systems in the literature.

Chapter Eight, Conclusion and Future Enhancement, summarizes the achievements of the SkinCare AI project and identifies opportunities for future development. This chapter provides a comprehensive conclusion of the work accomplished and outlines potential enhancements that could extend the functionality and impact of the system.

Chapter Nine, Bibliography and References, provides a comprehensive list of all sources cited in this report, including academic papers, technical documentation, and online resources that informed the development of SkinCare AI.

Chapter Ten, Appendices, contains supplementary materials that support the main body of the report. Appendix A presents output screens showing the user interface of the SkinCare AI system. Appendix B provides sample code snippets illustrating key implementation details. Appendix C contains a user manual providing guidance on how to use the SkinCare AI system.

The organization of this report is designed to provide readers with a clear and logical progression through the project, from initial concept and analysis through design, implementation, and evaluation. Each chapter builds upon the preceding chapters, creating a comprehensive documentation of the SkinCare AI project that can serve as both a technical reference and an academic record of the work accomplished.

---

<!-- PAGE BREAK -->

## CHAPTER 2: SYSTEM STUDY AND ANALYSIS

### 2.1 Problem Statement


The global healthcare landscape faces a significant challenge in the early detection and diagnosis of skin cancer, a disease that affects millions of individuals worldwide and claims thousands of lives annually. Despite advances in medical technology and increased awareness of skin cancer risks, substantial barriers continue to impede timely diagnosis and treatment, particularly in underserved communities and regions with limited access to dermatological expertise. This section presents a formal analysis of the problem that SkinCare AI aims to address.

The primary problem can be stated as follows: There exists a critical need for accessible, accurate, and user-friendly preliminary screening tools that can assist individuals in identifying potentially concerning skin lesions and encourage timely professional medical evaluation. The current healthcare infrastructure is insufficient to provide universal access to dermatological screening, resulting in delayed diagnoses, poorer patient outcomes, and increased healthcare costs associated with treating advanced-stage skin cancers.

The problem manifests across multiple dimensions that collectively create a complex challenge requiring a multifaceted solution. The first dimension concerns the epidemiological burden of skin cancer. Skin cancer is the most common form of cancer in many developed countries, with incidence rates continuing to rise due to factors including increased ultraviolet radiation exposure, aging populations, and improved detection methods. The World Health Organization estimates that between two and three million non-melanoma skin cancers and approximately 132,000 melanoma skin cancers occur globally each year. In the United States, it is estimated that more than 9,500 people are diagnosed with skin cancer every day, and more than two people die of the disease every hour.

The second dimension relates to the geographic and socioeconomic disparities in access to dermatological care. The distribution of dermatologists is highly uneven, with concentrations in urban areas and significant shortages in rural and underserved communities. In the United States, approximately 35 percent of counties have no dermatologist, leaving millions of residents without local access to specialized skin care. This disparity is even more pronounced in developing countries, where the ratio of dermatologists to population can be orders of magnitude lower than in developed nations.


The third dimension concerns the time-sensitive nature of skin cancer diagnosis. The prognosis for skin cancer, particularly melanoma, is highly dependent on the stage at which it is detected. Early-stage melanomas that have not penetrated beyond the epidermis have five-year survival rates exceeding ninety-nine percent, while late-stage melanomas that have metastasized to distant organs have five-year survival rates of approximately twenty-seven percent. This dramatic difference in outcomes underscores the critical importance of early detection and the potential life-saving impact of tools that can encourage timely professional evaluation.

The fourth dimension relates to the limitations of self-examination and the challenges of distinguishing benign lesions from potentially malignant ones. While regular self-examination of the skin is recommended as part of a comprehensive skin cancer prevention strategy, many individuals lack the knowledge and training to accurately assess skin lesions. The visual similarity between benign conditions such as seborrheic keratoses and potentially malignant lesions can lead to both false reassurance and unnecessary anxiety. Without professional guidance, individuals may either dismiss concerning lesions or become overly worried about benign conditions.

The fifth dimension concerns the economic impact of delayed diagnosis and treatment. The cost of treating skin cancer increases substantially with the stage of the disease. Early-stage skin cancers can often be treated with relatively simple outpatient procedures, while advanced cancers may require extensive surgery, radiation therapy, chemotherapy, or immunotherapy. The economic burden extends beyond direct medical costs to include lost productivity, reduced quality of life, and the emotional toll on patients and their families.

The problem statement can be formally articulated as: Given the high incidence of skin cancer, the critical importance of early detection, the limited availability of dermatological expertise, and the challenges of accurate self-assessment, there is a need for an accessible, AI-powered preliminary screening tool that can analyze images of skin lesions, provide educational information about potential conditions, and encourage appropriate professional medical consultation when concerns are identified.

---

<!-- PAGE BREAK -->

### 2.2 Existing System


The landscape of skin cancer detection and diagnosis encompasses a range of existing systems and approaches, from traditional clinical methods to emerging technological solutions. Understanding these existing systems is essential for contextualizing the contributions of SkinCare AI and identifying opportunities for improvement. This section provides a comprehensive examination of the current state of skin cancer detection systems.

Traditional clinical diagnosis of skin lesions relies primarily on visual examination by trained healthcare providers, typically dermatologists or primary care physicians with dermatological training. The clinical examination process typically begins with a visual inspection of the skin lesion, during which the clinician assesses characteristics such as size, shape, color, border regularity, and any changes over time. The ABCDE criteria, which stands for Asymmetry, Border irregularity, Color variation, Diameter greater than six millimeters, and Evolution or change over time, provides a standardized framework for evaluating potentially malignant lesions.

Dermoscopy, also known as dermatoscopy or epiluminescence microscopy, represents an advancement over naked-eye examination. This technique uses a handheld device called a dermatoscope to examine skin lesions with magnification and specialized lighting. Dermoscopy allows clinicians to visualize subsurface structures that are not visible to the naked eye, improving diagnostic accuracy for pigmented lesions. Studies have shown that dermoscopy can improve the sensitivity of melanoma detection by ten to thirty percent compared to naked-eye examination alone.

Histopathological examination remains the gold standard for definitive diagnosis of skin cancer. This process involves obtaining a tissue sample through biopsy, processing the sample, and examining it under a microscope by a trained pathologist. While histopathology provides definitive diagnosis, it is an invasive procedure that requires specialized laboratory facilities and expertise, making it impractical for routine screening purposes.

Several commercial and research-based AI systems for skin lesion analysis have emerged in recent years. These systems vary in their approaches, capabilities, and intended use cases. Some notable examples include applications developed by major technology companies, academic research projects, and healthcare-focused startups. These systems typically use deep learning algorithms trained on large datasets of dermoscopic images to classify skin lesions into various categories.


Teledermatology services have emerged as a means of extending dermatological expertise to underserved areas. These services allow patients to submit images of skin lesions for remote evaluation by dermatologists. While teledermatology can improve access to specialist care, it still requires the involvement of trained dermatologists and may involve delays in receiving evaluations. The quality of teledermatology consultations can also be affected by image quality and the limitations of remote examination.

Consumer-facing mobile applications for skin analysis have proliferated in recent years, with varying levels of sophistication and accuracy. Some applications use simple image analysis techniques to assess skin lesions, while others employ more advanced machine learning algorithms. The accuracy and reliability of these applications vary widely, and concerns have been raised about the potential for false reassurance or unnecessary alarm based on inaccurate assessments.

Hospital and clinic-based computer-aided diagnosis systems represent another category of existing solutions. These systems are typically designed for use by healthcare professionals and may be integrated with clinical workflows and electronic health record systems. While these systems can provide valuable decision support for clinicians, they are generally not accessible to the general public and require specialized equipment and training to operate.

Research platforms and datasets have played a crucial role in advancing the field of AI-based skin lesion analysis. The International Skin Imaging Collaboration has created extensive archives of dermoscopic images that have been used to train and evaluate numerous machine learning models. The HAM10000 dataset, published by Tschandl and colleagues, has become a benchmark for skin lesion classification research. These resources have enabled researchers worldwide to develop and compare different approaches to automated skin lesion analysis.

#### 2.2.1 Drawbacks of Existing System


Despite the various existing systems and approaches for skin cancer detection, significant limitations persist that create opportunities for improvement. This section examines the key drawbacks of existing systems that SkinCare AI aims to address.

The limited accessibility of professional dermatological care represents a fundamental drawback of traditional clinical approaches. The shortage of dermatologists, particularly in rural and underserved areas, means that many individuals cannot easily access professional skin examinations. Wait times for dermatology appointments can extend to weeks or months in many regions, potentially allowing concerning lesions to progress during the waiting period. The cost of dermatological consultations can also be prohibitive for individuals without adequate health insurance coverage.

The subjective nature of visual examination introduces variability in diagnostic accuracy. Studies have shown that inter-observer agreement among dermatologists can vary significantly, particularly for challenging cases. The accuracy of clinical diagnosis depends heavily on the experience and training of the examining clinician, leading to inconsistent outcomes across different healthcare settings. This variability can result in both missed diagnoses and unnecessary biopsies of benign lesions.

Existing AI-based systems often suffer from limited transparency and explainability. Many commercial applications provide classification results without adequate explanation of the reasoning behind the predictions. This lack of transparency can make it difficult for users to understand the basis for the assessment and may undermine trust in the system. Additionally, some systems do not provide confidence scores or uncertainty estimates, making it difficult to assess the reliability of individual predictions.

The single-model architecture employed by many existing systems can limit accuracy across diverse image types and conditions. A model trained on a specific dataset may perform well on similar images but struggle with images that differ in quality, lighting, or other characteristics. This limitation can lead to unreliable predictions for images that fall outside the training distribution.


Many existing consumer applications lack comprehensive features beyond basic image classification. Users may receive a classification result but have limited access to educational information, historical tracking, or tools for sharing results with healthcare providers. This limited functionality reduces the overall value of the application and may not adequately support users in making informed decisions about their healthcare.

The absence of proper medical disclaimers and responsible AI practices in some existing applications raises concerns about potential misuse. Applications that present results as definitive diagnoses rather than preliminary assessments may discourage users from seeking appropriate professional evaluation. The lack of clear guidance on when to seek medical attention can lead to either false reassurance or unnecessary anxiety.

Data privacy and security concerns affect many existing systems, particularly consumer-facing applications. Users may be reluctant to upload sensitive health information to applications with unclear data handling practices. The lack of transparency about how uploaded images are stored, processed, and potentially shared can undermine user trust and limit adoption.

The limited integration with healthcare workflows reduces the clinical utility of many existing systems. Applications that operate in isolation from clinical systems may not effectively support the transition from preliminary screening to professional evaluation. The inability to generate professional reports or share results with healthcare providers limits the value of these applications in facilitating appropriate medical care.

The lack of longitudinal tracking capabilities in many existing systems prevents users from monitoring changes in skin lesions over time. The ability to track changes is particularly important for identifying evolving lesions that may warrant professional evaluation. Without historical tracking, users must rely on memory or manual record-keeping to monitor their skin health over time.

---

<!-- PAGE BREAK -->

### 2.3 Proposed System


SkinCare AI represents a comprehensive solution designed to address the limitations of existing skin cancer detection systems while providing an accessible, accurate, and user-friendly platform for preliminary skin lesion screening. The proposed system integrates advanced deep learning technologies with a modern web-based interface to deliver a complete skin health management solution. This section provides a detailed description of the proposed system and its key components.

The core of the proposed system is a dual-model deep learning architecture that combines the strengths of two distinct neural network models to provide robust and accurate skin lesion classification. The primary model utilizes the EfficientNetB0 architecture, a state-of-the-art convolutional neural network that achieves excellent accuracy while maintaining computational efficiency. This model has been pre-trained on the ImageNet dataset, which contains over fourteen million images across thousands of categories, and subsequently fine-tuned on the ISIC 2019 dataset comprising over 25,000 dermoscopic images. The transfer learning approach allows the model to leverage the rich feature representations learned from ImageNet while adapting to the specific characteristics of dermoscopic images.

The secondary model is a custom-designed Convolutional Neural Network that has been trained from scratch on a modified version of the HAM10000 dataset. This model provides an alternative classification pathway that can be particularly effective for images that may not conform to typical dermoscopic standards. The custom architecture has been optimized for the specific characteristics of the training dataset and provides a complementary perspective to the EfficientNetB0 model.

The intelligent model selection mechanism represents a key innovation of the proposed system. Rather than relying on a single model for all predictions, the system automatically evaluates the confidence level of predictions from the primary model and determines whether to utilize the secondary model for potentially improved accuracy. When the primary model produces a prediction with confidence below a specified threshold, the system automatically invokes the secondary model and compares the results. This approach ensures that users receive the most reliable predictions possible, regardless of variations in image quality or lesion characteristics.


The web application component of the proposed system is built using the Django framework, a high-level Python web framework that encourages rapid development and clean, pragmatic design. Django provides a robust foundation for building secure, scalable web applications and includes built-in support for user authentication, database management, and template rendering. The application follows the Model-View-Template architectural pattern, ensuring clear separation of concerns and maintainable code structure.

The user authentication system implements comprehensive security measures to protect user accounts and sensitive health information. New users register with their email address and create a secure password. The system sends a One-Time Password to the provided email address for verification, ensuring that users provide valid email addresses and preventing unauthorized account creation. The OTP system generates secure six-digit codes that expire after ten minutes, balancing security requirements with user convenience. Password reset functionality is also provided through a similar OTP-based verification process.

The image analysis workflow is designed to be intuitive and user-friendly. Users upload images of skin lesions through a simple drag-and-drop interface or file selection dialog. The system validates uploaded images to ensure they meet minimum quality requirements and are in supported formats. Once uploaded, images are preprocessed to match the input requirements of the neural network models, including resizing, normalization, and color space conversion. The preprocessed images are then passed through the selected model or models, and the classification results are generated along with confidence scores.

The result presentation follows a legally-compliant format that clearly communicates the preliminary nature of the assessment while providing valuable educational information. Results include the predicted condition category, confidence score, educational information about the detected condition, prevention and precautionary guidelines, and clear recommendations for professional medical consultation. The presentation emphasizes that results are for educational purposes only and should not be used as a substitute for professional medical evaluation.


The analysis history feature enables users to maintain a comprehensive record of all their skin analyses over time. Each analysis record includes the original uploaded image, the classification result, confidence scores, the model used for analysis, and the timestamp of the analysis. Users can access their complete history through an intuitive interface that supports filtering and sorting by various criteria. This longitudinal tracking capability allows users to monitor changes in existing lesions and track the appearance of new skin conditions over time.

The PDF report generation capability allows users to create professional, printable reports of their analysis results. These reports are formatted for easy sharing with healthcare providers and include all relevant information from the analysis along with appropriate medical disclaimers. The reports can facilitate communication between patients and their healthcare providers, supporting the transition from preliminary screening to professional evaluation.

The analytics dashboard provides users with visual representations of their analysis data through interactive charts and graphs. The dashboard utilizes Chart.js to create visualizations including pie charts showing the distribution of detected conditions, line graphs displaying analysis frequency over time, and bar charts comparing confidence levels across different analyses. These visualizations help users understand their skin health patterns and can be valuable for discussions with healthcare providers.

The DermaGenie AI assistant provides an intelligent conversational interface for skin health queries. Powered by the Perplexity AI platform, DermaGenie can answer questions about various skin conditions, provide general skin care guidance, explain medical terminology, and offer educational information about skin health. The chatbot maintains conversation context, allowing for natural, flowing discussions about skin health topics while consistently reminding users that its responses are for educational purposes only.

#### 2.3.1 Advantages of Proposed System


The proposed SkinCare AI system offers numerous advantages over existing systems, addressing many of the limitations identified in the previous section while providing additional value through innovative features and responsible design practices.

The dual-model architecture provides improved accuracy and robustness compared to single-model systems. By combining the strengths of two distinct neural network models, the system can provide reliable predictions across a wider range of image types and conditions. The intelligent model selection mechanism ensures that users receive the most appropriate analysis for their specific images, automatically adapting to variations in image quality and lesion characteristics.

The comprehensive feature set extends well beyond basic image classification, providing users with a complete skin health management platform. The combination of analysis history tracking, PDF report generation, analytics dashboard, and AI chatbot creates a holistic solution that supports users throughout their skin health journey. This integrated approach provides significantly more value than standalone classification applications.

The emphasis on responsible AI practices ensures that the system enhances rather than replaces professional medical care. Clear medical disclaimers, legally-compliant result presentation, and consistent recommendations for professional consultation help users understand the appropriate role of AI-based screening tools. This responsible approach builds trust and encourages appropriate healthcare-seeking behavior.

The user-friendly interface makes advanced AI technology accessible to users without technical expertise. The intuitive design, clear navigation, and helpful guidance throughout the application ensure that users can effectively utilize all features regardless of their technical background. The responsive design ensures optimal user experience across desktop, tablet, and mobile devices.


The secure authentication system protects user accounts and sensitive health information while providing a seamless user experience. The OTP-based email verification ensures account security without creating excessive friction in the registration process. The comprehensive security measures, including password hashing, session management, and CSRF protection, ensure that user data remains protected.

The longitudinal tracking capability enables users to monitor changes in skin lesions over time, a feature that is particularly valuable for identifying evolving lesions that may warrant professional evaluation. The ability to compare multiple analyses and track trends provides insights that are not available from single-point-in-time assessments.

The PDF report generation facilitates communication between users and their healthcare providers, supporting the transition from preliminary screening to professional evaluation. The professional format and comprehensive information included in the reports make them valuable tools for medical consultations.

The educational content integrated throughout the application improves skin health literacy and empowers users to make informed decisions about their healthcare. The DermaGenie AI assistant provides an accessible interface for learning about skin health topics, complementing the educational information provided with analysis results.

The open architecture and use of standard technologies facilitate future enhancements and integrations. The Django framework, TensorFlow, and other technologies used in the system are well-documented and widely supported, ensuring that the system can be maintained and extended over time.

---

<!-- PAGE BREAK -->

### 2.4 Feasibility Analysis

The feasibility analysis evaluates the practicality and viability of the proposed SkinCare AI system across multiple dimensions. This comprehensive assessment considers technical, economic, and operational factors to determine whether the project can be successfully developed, deployed, and maintained. The analysis provides a foundation for informed decision-making and helps identify potential challenges that must be addressed during development.

#### 2.4.1 Technical Feasibility


Technical feasibility assesses whether the proposed system can be developed using available technologies, tools, and expertise. This analysis examines the technical requirements of the SkinCare AI system and evaluates the availability and maturity of the technologies needed to implement each component.

The deep learning component of the system relies on well-established technologies that have been extensively validated in both research and production environments. TensorFlow, the primary deep learning framework used in the project, is a mature, open-source platform developed by Google that has been used to build and deploy machine learning models across a wide range of applications. The framework provides comprehensive support for building, training, and deploying neural networks, including the EfficientNetB0 architecture used in the primary model. Keras, which serves as the high-level API for TensorFlow, provides an intuitive interface for defining and training neural network models.

The availability of pre-trained models and transfer learning techniques significantly reduces the technical complexity of developing accurate classification models. The EfficientNetB0 model, pre-trained on the ImageNet dataset, provides a strong foundation that can be fine-tuned for skin lesion classification with relatively modest computational resources. This approach has been validated in numerous research studies and has been shown to achieve competitive accuracy on dermoscopic image classification tasks.

The web application component utilizes Django, a mature and well-documented web framework that has been used to build numerous production applications. Django provides built-in support for user authentication, database management, form handling, and template rendering, reducing the development effort required to implement these common features. The framework follows security best practices by default, helping to ensure that the application is protected against common web vulnerabilities.


The frontend technologies used in the system, including HTML5, CSS3, and JavaScript, are standard web technologies supported by all modern browsers. The Chart.js library provides a straightforward approach to creating interactive data visualizations without requiring specialized expertise. The responsive design techniques used to ensure cross-device compatibility are well-established and widely documented.

The email notification system utilizes the Resend API, a modern email delivery service that provides reliable message delivery and comprehensive documentation. The API integration is straightforward and follows standard REST conventions, making it accessible to developers with basic web development experience.

The AI chatbot integration with the Perplexity AI platform leverages a well-documented API that provides natural language processing capabilities. The integration follows standard patterns for API consumption and can be implemented using Python's requests library or similar tools.

The database requirements of the system are modest and can be met using SQLite for development and testing, with the option to migrate to PostgreSQL or other production-grade databases for deployment. Django's Object-Relational Mapping provides database abstraction that simplifies database operations and facilitates migration between different database backends.

The hardware requirements for running the system are reasonable and can be met using standard computing equipment. While GPU acceleration can improve model inference speed, the system is designed to function effectively using CPU-only inference, making it accessible to users without specialized hardware. Cloud deployment options provide scalability for production environments with higher traffic volumes.

Based on this analysis, the SkinCare AI system is determined to be technically feasible. All required technologies are mature, well-documented, and have been successfully used in similar applications. The development team possesses the necessary skills and expertise to implement the proposed system using these technologies.

#### 2.4.2 Economic Feasibility


Economic feasibility evaluates the cost-effectiveness of the proposed system by analyzing development costs, operational costs, and potential benefits. This analysis helps determine whether the project represents a sound investment of resources and identifies opportunities for cost optimization.

The development costs for the SkinCare AI system are primarily associated with personnel time, as the project utilizes open-source technologies that do not require licensing fees. The Django framework, TensorFlow, and other core technologies are freely available under permissive open-source licenses. The development environment can be established using freely available tools including Python, Visual Studio Code, and Git.

The machine learning model training can be conducted using Google Colab, which provides free access to GPU-accelerated computing resources. This eliminates the need for expensive hardware investments during the development phase. The ISIC and HAM10000 datasets used for model training are publicly available for research and educational purposes, eliminating data acquisition costs.

The operational costs for running the system in a production environment depend on the deployment approach and expected traffic volume. For small-scale deployments, the system can be hosted on modest cloud infrastructure with costs ranging from minimal to moderate per month. The use of SQLite as the default database eliminates database licensing costs, although migration to PostgreSQL may be advisable for larger deployments.

The email notification system incurs costs based on the volume of emails sent. The Resend API provides a free tier that may be sufficient for small-scale deployments, with paid tiers available for higher volumes. The AI chatbot integration with Perplexity AI may incur API usage costs depending on the volume of queries processed.


The potential benefits of the system include improved access to preliminary skin screening, which may contribute to earlier detection of skin cancers and improved patient outcomes. While these benefits are difficult to quantify precisely, the potential for life-saving early detection represents significant value. The educational component of the system may also contribute to improved skin health awareness and preventive behaviors.

For academic and research contexts, the system provides a platform for studying AI-based medical image analysis and exploring approaches to responsible AI deployment in healthcare settings. The modular architecture facilitates experimentation with different models, datasets, and features.

The cost-benefit analysis indicates that the SkinCare AI system is economically feasible, particularly given the use of open-source technologies and cloud-based resources that minimize upfront investment. The potential benefits in terms of improved access to preliminary screening and educational value justify the modest development and operational costs.

#### 2.4.3 Operational Feasibility

Operational feasibility assesses whether the proposed system can be effectively used by its intended users and integrated into existing workflows and practices. This analysis considers user acceptance, training requirements, and organizational factors that may affect the successful deployment and adoption of the system.

The target users of SkinCare AI include individuals seeking preliminary assessment of skin lesions, healthcare providers who may use the system as a decision support tool, and researchers studying AI-based medical image analysis. The system has been designed with these diverse user groups in mind, providing an intuitive interface that does not require specialized technical knowledge.


The user interface has been designed following established usability principles to ensure that users can effectively navigate the application and complete desired tasks. Clear labeling, consistent navigation, and helpful guidance throughout the application reduce the learning curve and support user success. The responsive design ensures that users can access the system from their preferred devices, whether desktop computers, tablets, or smartphones.

The training requirements for using the system are minimal. The intuitive interface and built-in guidance enable most users to begin using the system effectively without formal training. The user manual provided in the appendices offers additional guidance for users who desire more detailed instructions. For healthcare providers who may use the system as a decision support tool, the clear presentation of results and confidence scores facilitates integration into clinical decision-making processes.

The system has been designed to complement rather than replace existing healthcare workflows. The emphasis on preliminary screening and the consistent recommendations for professional consultation ensure that the system supports appropriate healthcare-seeking behavior. The PDF report generation feature facilitates communication between users and their healthcare providers, supporting the transition from preliminary screening to professional evaluation.

The operational requirements for maintaining the system are manageable with standard IT resources. The Django framework provides administrative interfaces for managing user accounts and monitoring system activity. The modular architecture facilitates updates and enhancements without requiring extensive system modifications.

Based on this analysis, the SkinCare AI system is determined to be operationally feasible. The intuitive interface, minimal training requirements, and complementary relationship with existing healthcare workflows support successful deployment and adoption. The system can be effectively used by its intended users and maintained with reasonable operational resources.

---

<!-- PAGE BREAK -->

## CHAPTER 3: DEVELOPMENT ENVIRONMENT

### 3.1 Hardware Requirements


The hardware requirements for the SkinCare AI system vary depending on the intended use case, ranging from development and testing environments to production deployment scenarios. This section provides detailed specifications for the hardware needed to develop, test, and deploy the system effectively.

The development environment requires hardware capable of running the development tools, executing the web application, and performing model inference for testing purposes. The minimum hardware requirements for development include a processor with at least four cores, such as an Intel Core i5 or AMD Ryzen 5, which provides sufficient computational power for running the Django development server and executing model inference. A minimum of eight gigabytes of RAM is required to accommodate the memory requirements of the development tools, web browser, and TensorFlow model loading. Storage requirements include at least ten gigabytes of free disk space for the application code, dependencies, model files, and test data.

For development purposes, a dedicated graphics processing unit is not strictly required, as the TensorFlow models can perform inference using CPU computation. However, developers who wish to experiment with model training or who desire faster inference times may benefit from a GPU with CUDA support. The display requirements for development include a monitor with at least 1366 by 768 resolution to accommodate the development tools and web browser windows.

The recommended hardware configuration for development provides improved performance and a more comfortable development experience. A processor with six or more cores, such as an Intel Core i7 or AMD Ryzen 7, enables faster compilation and execution. Sixteen gigabytes of RAM provides headroom for running multiple applications simultaneously and handling larger datasets. A solid-state drive with at least twenty gigabytes of free space significantly improves application loading times and overall system responsiveness. A display with 1920 by 1080 resolution or higher provides more screen real estate for development tools.


The model training phase has more demanding hardware requirements due to the computational intensity of training deep neural networks. While the project utilizes Google Colab for model training, which provides free access to GPU-accelerated computing resources, understanding the hardware requirements for local training is valuable for researchers who may wish to experiment with different training configurations.

For local model training, a dedicated GPU with CUDA support is highly recommended. An NVIDIA GPU with at least six gigabytes of video memory, such as the GTX 1060 or better, can significantly accelerate training times compared to CPU-only training. The system memory requirements increase to at least sixteen gigabytes of RAM to accommodate the training data and model parameters. Storage requirements also increase, as training datasets can be several gigabytes in size and training checkpoints require additional space.

The production deployment environment has hardware requirements that depend on the expected traffic volume and performance requirements. For small-scale deployments serving a limited number of concurrent users, modest hardware similar to the development environment may be sufficient. The minimum production requirements include a processor with at least two cores, eight gigabytes of RAM, and twenty gigabytes of storage.

For larger deployments with higher traffic volumes, more substantial hardware is recommended. A processor with four or more cores provides better handling of concurrent requests. Sixteen gigabytes or more of RAM enables caching and improved performance under load. Solid-state storage with at least fifty gigabytes of capacity accommodates the application, models, user uploads, and database growth over time.

Cloud deployment options provide flexibility in scaling hardware resources based on demand. Cloud providers such as Amazon Web Services, Google Cloud Platform, and Microsoft Azure offer virtual machine instances with various hardware configurations that can be selected based on performance requirements and budget constraints. The use of containerization technologies such as Docker can facilitate deployment across different cloud environments.

---

<!-- PAGE BREAK -->

### 3.2 Software Requirements


The software requirements for the SkinCare AI system encompass the operating system, programming languages, frameworks, libraries, and external services needed to develop, test, and deploy the application. This section provides a comprehensive listing of the software components and their versions.

The operating system requirements are flexible, as the technologies used in the project are cross-platform compatible. Development and deployment can be performed on Windows, macOS, or Linux operating systems. For production deployment, Linux-based operating systems such as Ubuntu 20.04 LTS or later are recommended due to their stability, security, and widespread use in server environments. Windows Server 2019 or later is also supported for organizations that prefer Windows-based infrastructure.

Python serves as the primary programming language for the SkinCare AI system. Python version 3.10 or later is required to ensure compatibility with the latest versions of the frameworks and libraries used in the project. Python's extensive ecosystem of libraries for web development, machine learning, and data processing makes it an ideal choice for this type of application.

The package management system pip is used to install and manage Python dependencies. The requirements.txt file in the project repository lists all required packages and their versions, enabling reproducible installation of the development environment. Virtual environments are recommended to isolate project dependencies from system-wide Python installations.

Git version control system version 2.30 or later is required for managing the project source code and collaborating with other developers. Git provides distributed version control capabilities that facilitate tracking changes, branching for feature development, and merging contributions from multiple developers.


The integrated development environment is a matter of developer preference, with Visual Studio Code and PyCharm being popular choices for Python development. Visual Studio Code provides a lightweight, extensible editor with excellent Python support through extensions. PyCharm offers a more comprehensive integrated development environment with advanced features for Python development.

The backend framework Django version 4.2.1 provides the foundation for the web application. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. The framework includes built-in support for user authentication, database management, form handling, and template rendering.

TensorFlow version 2.13.0 serves as the deep learning framework for model inference. TensorFlow is an open-source platform for machine learning developed by Google that provides comprehensive tools for building and deploying machine learning models. Keras version 2.13.1, which is integrated with TensorFlow, provides the high-level API for defining and working with neural network models.

The image processing requirements are met by Pillow version 10.0.0, which provides Python imaging capabilities for loading, manipulating, and saving images. OpenCV version 4.8.0 provides additional computer vision functionality that may be useful for advanced image preprocessing.

NumPy version 1.24.3 provides fundamental support for numerical computing in Python, including multi-dimensional arrays and mathematical functions. Pandas version 2.0.3 provides data manipulation and analysis capabilities that are useful for working with datasets and generating reports.

The visualization libraries matplotlib version 3.7.2 and seaborn version 0.12.2 provide capabilities for creating static visualizations during development and analysis. The frontend visualization library Chart.js is used for creating interactive charts in the web application.

The python-dotenv library version 1.0.0 provides support for loading environment variables from configuration files, enabling secure management of sensitive configuration data such as API keys and database credentials.

---

<!-- PAGE BREAK -->

### 3.3 Software Description

#### 3.3.1 About Python


Python is a high-level, interpreted programming language that has become one of the most popular languages for software development, particularly in the fields of data science, machine learning, and web development. Created by Guido van Rossum and first released in 1991, Python has evolved through multiple major versions to become a versatile and powerful language that emphasizes code readability and developer productivity.

The design philosophy of Python emphasizes code readability through the use of significant whitespace and a clean, expressive syntax. The language follows the principle that there should be one obvious way to accomplish any given task, reducing the cognitive burden on developers and facilitating collaboration. Python's syntax is designed to be intuitive and closely resembles natural language, making it accessible to beginners while remaining powerful enough for advanced applications.

Python is an interpreted language, meaning that code is executed line by line by the Python interpreter rather than being compiled to machine code before execution. This approach provides several advantages including rapid development cycles, easy debugging, and platform independence. Python code can run on any platform that has a Python interpreter installed, including Windows, macOS, Linux, and various embedded systems.

The Python ecosystem includes an extensive standard library that provides modules for a wide range of tasks including file handling, network communication, data serialization, and much more. Beyond the standard library, the Python Package Index hosts hundreds of thousands of third-party packages that extend Python's capabilities for specialized applications. This rich ecosystem makes Python an excellent choice for projects that require integration of multiple technologies and libraries.

Python supports multiple programming paradigms including procedural, object-oriented, and functional programming. This flexibility allows developers to choose the approach that best fits their problem domain and personal preferences. The object-oriented features of Python include classes, inheritance, polymorphism, and encapsulation, enabling the development of well-structured, maintainable code.


The dynamic typing system of Python allows variables to hold values of any type without explicit type declarations. While this provides flexibility and reduces boilerplate code, Python also supports optional type hints that can improve code documentation and enable static type checking tools. The combination of dynamic typing with optional type hints provides a balance between flexibility and safety.

Memory management in Python is handled automatically through garbage collection, freeing developers from the burden of manual memory allocation and deallocation. The reference counting mechanism tracks the number of references to each object and automatically deallocates objects when they are no longer referenced. A cyclic garbage collector handles cases where objects reference each other in cycles.

Python's role in the SkinCare AI project is central, serving as the primary programming language for both the web application and the machine learning components. The Django web framework, TensorFlow deep learning library, and numerous utility libraries are all Python-based, creating a cohesive development environment. Python's readability and extensive documentation make the codebase accessible to developers with varying levels of experience.

#### 3.3.2 About Google Colab

Google Colaboratory, commonly known as Google Colab, is a cloud-based interactive computing environment that allows users to write and execute Python code through a web browser. Developed by Google Research, Colab provides free access to computing resources including graphics processing units and tensor processing units, making it an invaluable tool for machine learning research and education.

The primary advantage of Google Colab for machine learning projects is the provision of free GPU and TPU resources. Training deep neural networks is computationally intensive and can take hours or days on standard CPU hardware. The GPU acceleration provided by Colab can reduce training times by orders of magnitude, making it practical to experiment with different model architectures and hyperparameters.


Google Colab notebooks are based on the Jupyter notebook format, providing an interactive environment that combines code cells, text cells, and output displays in a single document. This format is particularly well-suited for exploratory data analysis and machine learning experimentation, as it allows developers to document their thought process alongside the code and visualize results immediately.

The integration with Google Drive provides convenient storage for notebooks, datasets, and model files. Users can mount their Google Drive within a Colab notebook, enabling seamless access to files stored in the cloud. This integration facilitates collaboration and ensures that work is automatically saved and accessible from any device.

Colab comes pre-installed with many popular Python libraries for data science and machine learning, including TensorFlow, Keras, PyTorch, NumPy, Pandas, and Matplotlib. This eliminates the need for complex environment setup and allows users to begin working immediately. Additional libraries can be installed using pip commands within the notebook.

In the SkinCare AI project, Google Colab was used for training the deep learning models. The GPU acceleration provided by Colab enabled efficient training of both the EfficientNetB0 model on the ISIC 2019 dataset and the custom CNN model on the HAM10000 subset. The notebook format facilitated documentation of the training process, including data preprocessing, model architecture definition, training configuration, and evaluation metrics.

#### 3.3.3 About Django

Django is a high-level Python web framework that enables rapid development of secure and maintainable web applications. Created in 2003 and publicly released in 2005, Django has become one of the most popular web frameworks, powering websites and applications for organizations ranging from startups to large enterprises including Instagram, Mozilla, and The Washington Post.


The design philosophy of Django emphasizes the principle of "Don't Repeat Yourself," encouraging developers to write reusable, modular code that avoids redundancy. The framework provides a comprehensive set of built-in features that handle common web development tasks, allowing developers to focus on the unique aspects of their applications rather than reimplementing standard functionality.

Django follows the Model-View-Template architectural pattern, which is similar to the Model-View-Controller pattern used in other frameworks. The Model layer defines the data structure and handles database interactions through Django's Object-Relational Mapping. The View layer contains the business logic that processes requests and generates responses. The Template layer defines the presentation of data using Django's template language.

The Object-Relational Mapping provided by Django abstracts database operations, allowing developers to work with database records as Python objects rather than writing raw SQL queries. The ORM supports multiple database backends including SQLite, PostgreSQL, MySQL, and Oracle, enabling applications to be developed and tested with one database and deployed with another. Database migrations are handled automatically, tracking changes to models and generating the necessary SQL to update the database schema.

Django's built-in authentication system provides comprehensive user management functionality including user registration, login, logout, password management, and permission-based access control. The authentication system is highly customizable, allowing developers to extend the default user model and implement custom authentication backends. Session management is handled automatically, with support for various session storage backends.

The security features of Django protect applications against common web vulnerabilities. Cross-Site Request Forgery protection is enabled by default, requiring valid tokens for form submissions. Cross-Site Scripting protection is provided through automatic escaping of template variables. SQL injection is prevented through the use of parameterized queries in the ORM. Clickjacking protection is available through middleware that sets appropriate HTTP headers.


The administrative interface provided by Django automatically generates a web-based interface for managing application data. The admin interface is highly customizable and provides a convenient way to manage users, view database records, and perform administrative tasks without writing custom code. This feature significantly accelerates development by providing immediate visibility into application data.

Django's template system provides a powerful and flexible way to generate HTML output. Templates can include variables, filters, and tags that control the rendering of content. Template inheritance allows developers to define base templates that can be extended by child templates, promoting code reuse and consistent page layouts.

In the SkinCare AI project, Django serves as the foundation for the web application, handling user authentication, database management, URL routing, and template rendering. The framework's built-in features significantly accelerated development while ensuring that the application follows security best practices.

#### 3.3.4 About TensorFlow

TensorFlow is an open-source machine learning platform developed by the Google Brain team. First released in 2015, TensorFlow has become one of the most widely used frameworks for developing and deploying machine learning models, with applications ranging from research prototypes to production systems serving millions of users.

The core abstraction in TensorFlow is the computational graph, which represents mathematical operations as nodes and data flow as edges. This graph-based approach enables efficient execution of complex computations, automatic differentiation for gradient-based optimization, and deployment across diverse hardware platforms including CPUs, GPUs, and specialized accelerators such as TPUs.


TensorFlow 2.0, released in 2019, introduced significant improvements to the framework including eager execution by default, which allows operations to be evaluated immediately rather than building a graph first. This change makes TensorFlow more intuitive and easier to debug while maintaining the performance benefits of graph execution for production deployment.

Keras, which is integrated into TensorFlow as its high-level API, provides an intuitive interface for building and training neural networks. Keras follows a modular design where models are built by combining layers, each of which performs a specific transformation on the input data. The Sequential API allows models to be defined as a linear stack of layers, while the Functional API enables more complex architectures with multiple inputs, outputs, and shared layers.

TensorFlow provides comprehensive support for convolutional neural networks, which are the foundation of modern image classification systems. The framework includes implementations of common layer types including convolutional layers, pooling layers, batch normalization, and dropout. Pre-trained models for popular architectures such as VGG, ResNet, and EfficientNet are available through the TensorFlow Hub and Keras Applications modules.

The training process in TensorFlow is highly configurable, with support for various optimizers, loss functions, and metrics. Callbacks provide hooks for monitoring training progress, saving checkpoints, adjusting learning rates, and implementing early stopping. TensorBoard provides visualization tools for monitoring training metrics, visualizing model architectures, and debugging training issues.

Model deployment is supported through multiple pathways including TensorFlow Serving for production inference, TensorFlow Lite for mobile and embedded devices, and TensorFlow.js for browser-based inference. The SavedModel format provides a portable representation of trained models that can be loaded and executed across different platforms.

In the SkinCare AI project, TensorFlow and Keras are used for loading and executing the trained neural network models. The EfficientNetB0 model and custom CNN model are both implemented using Keras and saved in the HDF5 format. The models are loaded at application startup and used to generate predictions for uploaded images.


#### 3.3.5 About Database Technology

Database technology plays a crucial role in the SkinCare AI system, providing persistent storage for user accounts, analysis records, and other application data. The system utilizes SQLite as the default database for development and testing, with support for migration to PostgreSQL or other production-grade databases for deployment.

SQLite is a self-contained, serverless, zero-configuration database engine that stores the entire database in a single file. Unlike client-server database systems, SQLite does not require a separate server process, making it ideal for development, testing, and small-scale deployments. The database file can be easily copied, backed up, and transferred between systems.

The simplicity of SQLite makes it an excellent choice for development environments where ease of setup is prioritized over scalability. Developers can begin working immediately without installing and configuring a database server. The database file is created automatically when the application is first run, and Django's migration system handles schema creation and updates.

Despite its simplicity, SQLite provides full SQL support including transactions, triggers, and views. The database engine is highly reliable and has been extensively tested, with the SQLite developers claiming that it is one of the most widely deployed software components in the world. The ACID compliance of SQLite ensures data integrity even in the event of system crashes or power failures.

For production deployments with higher traffic volumes or more demanding requirements, PostgreSQL is recommended as an alternative database backend. PostgreSQL is a powerful, open-source object-relational database system with a strong reputation for reliability, feature robustness, and performance. The database supports advanced features including complex queries, foreign keys, triggers, views, and transactional integrity.


Django's Object-Relational Mapping provides a consistent interface for database operations regardless of the underlying database backend. Models are defined as Python classes with attributes representing database fields. The ORM translates Python operations into appropriate SQL queries for the configured database backend. This abstraction allows the application to be developed and tested with SQLite and deployed with PostgreSQL without modifying the application code.

The database schema for SkinCare AI includes tables for user accounts, user profiles, analysis records, email verification tokens, password reset tokens, and chat conversation history. The schema is defined through Django models and managed through the migration system. Relationships between tables are defined using foreign keys, enabling efficient queries across related data.

Database queries in Django are performed using the QuerySet API, which provides a high-level interface for filtering, ordering, and aggregating data. QuerySets are lazy, meaning that database queries are not executed until the results are actually needed. This lazy evaluation enables efficient query construction and optimization.

The database configuration in Django is specified in the settings file, allowing different configurations for development, testing, and production environments. Environment variables can be used to specify database credentials, ensuring that sensitive information is not stored in the source code.

---

<!-- PAGE BREAK -->

## CHAPTER 4: SYSTEM DESIGN

### 4.1 Module Description

The SkinCare AI system is organized into eight primary modules, each responsible for a specific aspect of the application's functionality. This modular architecture promotes separation of concerns, facilitates maintenance and testing, and enables independent development of different system components. This section provides detailed descriptions of each module, including its purpose, components, and interactions with other modules.

#### 4.1.1 User Authentication Module


The User Authentication Module is responsible for managing user identity and access control throughout the SkinCare AI application. This module handles user registration, login, logout, email verification, and password management, ensuring that only authenticated users can access protected features and that user accounts remain secure.

The registration process begins when a new user submits the registration form with their desired username, email address, and password. The module validates the submitted data, checking that the username is unique, the email address is valid and not already registered, and the password meets minimum security requirements. If validation succeeds, a new user account is created with the password securely hashed using Django's PBKDF2 algorithm.

Following successful registration, the module initiates the email verification process. A six-digit One-Time Password is generated using a cryptographically secure random number generator and stored in the database along with a timestamp. The OTP is sent to the user's registered email address using the Email Notification Module. The user must enter the correct OTP within ten minutes to verify their email address and activate their account.

The login process authenticates users by verifying their credentials against the stored account information. When a user submits the login form, the module retrieves the corresponding user record and compares the submitted password against the stored hash. If the credentials are valid and the email address has been verified, a session is created and the user is redirected to the home page. Failed login attempts are logged for security monitoring purposes.

Session management is handled through Django's built-in session framework, which stores session data on the server and identifies sessions through cookies. Sessions are configured to expire after a period of inactivity, requiring users to re-authenticate. The module provides logout functionality that invalidates the current session and clears session data.


The password reset functionality allows users who have forgotten their passwords to regain access to their accounts. The process begins when a user requests a password reset by providing their registered email address. The module generates a new OTP and sends it to the email address. After verifying the OTP, the user can set a new password. The password reset OTP expires after ten minutes and can only be used once.

The administrative authentication flow provides a separate login mechanism for staff users who need access to the administrative dashboard. This separation ensures that administrative functions are protected by an additional layer of authentication and that regular users cannot accidentally access administrative features.

The module integrates with Django's permission system to control access to different features based on user roles. Regular users have access to analysis features, history, and profile management. Staff users have additional access to the administrative dashboard. Superusers have full access to all system features including the Django admin interface.

#### 4.1.2 Image Analysis Module

The Image Analysis Module is the core component of the SkinCare AI system, responsible for processing uploaded images and generating classification predictions using the trained deep learning models. This module handles image upload, validation, preprocessing, model inference, and result formatting.

The image upload process accepts images through a web form that supports both file selection and drag-and-drop functionality. The module validates uploaded files to ensure they are in supported formats including JPEG, PNG, and common image formats. File size limits are enforced to prevent excessive resource consumption. Uploaded images are stored in a designated media directory with unique filenames to prevent conflicts.


Image preprocessing transforms uploaded images into the format required by the neural network models. For the EfficientNetB0 model, images are resized to 224 by 224 pixels and normalized to the range expected by the model. For the custom CNN model, images are resized to 48 by 48 pixels with appropriate normalization. The preprocessing pipeline uses the Pillow library for image manipulation and NumPy for array operations.

The model inference process passes the preprocessed image through the selected neural network model to generate classification predictions. The module supports three inference modes: automatic selection, where the system chooses the most appropriate model based on confidence thresholds; EfficientNetB0-only mode; and CNN-only mode. In automatic mode, the primary model is used first, and if the confidence is below the threshold, the secondary model is invoked.

The prediction output includes the predicted class label, confidence score, and the model used for the prediction. The confidence score represents the probability assigned by the model to the predicted class, providing an indication of the model's certainty. Higher confidence scores generally indicate more reliable predictions, although confidence should be interpreted in the context of the model's overall accuracy.

The result formatting component transforms the raw prediction output into a user-friendly presentation that includes educational information about the detected condition. The formatting follows a legally-compliant template that clearly communicates the preliminary nature of the assessment and includes appropriate medical disclaimers. The formatted results include the condition name, confidence percentage, description of the condition, prevention guidelines, and recommendations for professional consultation.

The module stores analysis records in the database, creating a historical record that can be accessed through the History Module. Each record includes the uploaded image, prediction results, model used, confidence score, and timestamp. This data supports longitudinal tracking and enables the analytics features of the system.

#### 4.1.3 User Profile Module


The User Profile Module manages user profile information and provides personalized features based on user data. This module handles profile creation, viewing, editing, and the display of user-specific statistics and activity summaries.

Profile creation occurs automatically when a new user account is created. The module creates a UserProfile record linked to the user account through a one-to-one relationship. The initial profile contains default values that can be customized by the user. The profile includes fields for biographical information, contact details, date of birth, profile picture, and notification preferences.

The profile viewing interface displays the user's profile information along with statistics derived from their analysis history. Statistics include the total number of analyses performed, the date of the most recent analysis, and the distribution of detected conditions. These statistics provide users with an overview of their skin health monitoring activity.

Profile editing allows users to update their personal information and preferences. The editing interface provides form fields for all editable profile attributes. Profile picture upload is supported, with images being resized and stored in a designated media directory. Changes to profile information trigger email notifications if the user has enabled this preference.

The notification preferences section allows users to control which email notifications they receive. Users can enable or disable notifications for analysis results, profile updates, and promotional communications. These preferences are stored in the user profile and consulted by the Email Notification Module when sending emails.

The module integrates with the authentication system to ensure that users can only view and edit their own profiles. Access control is enforced through Django's authentication decorators, which redirect unauthenticated users to the login page. The profile URL structure uses the authenticated user's identity rather than a user identifier in the URL, preventing unauthorized access to other users' profiles.

#### 4.1.4 Analytics Dashboard Module


The Analytics Dashboard Module provides users with visual representations of their analysis data, enabling them to identify patterns and trends in their skin health monitoring over time. This module aggregates data from the user's analysis history and presents it through interactive charts and summary statistics.

The data aggregation component queries the database to retrieve the user's analysis records and computes various statistics. Aggregations include the count of analyses by condition type, the distribution of analyses over time, average confidence scores, and the frequency of model usage. These aggregations are computed dynamically to reflect the current state of the user's data.

The condition distribution visualization presents a pie chart showing the proportion of each detected condition across all of the user's analyses. This visualization helps users understand which conditions have been most frequently detected and may indicate areas that warrant attention or professional consultation. The chart is rendered using Chart.js, which provides interactive features including tooltips and legend toggling.

The temporal analysis visualization presents a line graph showing the frequency of analyses over time. Users can observe trends in their monitoring activity and identify periods of increased or decreased engagement. This visualization can be useful for maintaining consistent monitoring habits and identifying correlations between analysis frequency and other factors.

The confidence score analysis provides insights into the reliability of predictions across different analyses. Users can view the distribution of confidence scores and identify analyses where the model exhibited lower certainty. This information can help users prioritize which results may warrant additional attention or professional evaluation.

The dashboard interface is designed to be responsive and accessible across different device types. The layout adapts to different screen sizes, ensuring that visualizations remain readable and interactive on both desktop and mobile devices. The use of clear labels, legends, and tooltips ensures that users can interpret the visualizations without specialized knowledge.

#### 4.1.5 History and Comparison Module


The History and Comparison Module enables users to access their complete analysis history and compare multiple analyses side by side. This module supports longitudinal tracking of skin conditions and facilitates identification of changes over time.

The history listing interface displays all of the user's past analyses in a paginated, sortable list. Each entry shows a thumbnail of the analyzed image, the detected condition, confidence score, model used, and timestamp. Users can filter the list by condition type, date range, or confidence level. Sorting options allow users to order results by date, condition, or confidence score.

The detailed view for individual analyses provides comprehensive information about a specific analysis. This view includes the full-size analyzed image, complete prediction results, educational information about the detected condition, and options for generating PDF reports or adding the analysis to a comparison.

The comparison feature allows users to select multiple analyses for side-by-side comparison. This functionality is particularly valuable for monitoring changes in specific lesions over time. The comparison interface displays the selected analyses in a grid layout, with images and key information aligned for easy comparison. Users can compare analyses of the same lesion taken at different times to identify any changes in appearance.

The PDF report generation capability creates professional, printable documents that summarize analysis results. Reports include the analyzed image, prediction results, confidence scores, educational information, and appropriate medical disclaimers. The reports are formatted for easy sharing with healthcare providers and can facilitate discussions during medical consultations.

The module implements access control to ensure that users can only access their own analysis history. Database queries are filtered by the authenticated user's identity, preventing unauthorized access to other users' data. The comparison feature similarly restricts selection to analyses belonging to the current user.

#### 4.1.6 Admin Module


The Admin Module provides system administrators with tools for monitoring and managing the SkinCare AI platform. This module is accessible only to users with staff privileges and provides visibility into system-wide statistics and user activity.

The administrative dashboard presents an overview of system metrics including the total number of registered users, total analyses performed, analyses performed in the current day, week, and month, and recent user registrations. These metrics provide administrators with insight into system usage and growth trends.

The user management interface allows administrators to view user accounts and their associated information. Administrators can see user registration dates, email verification status, and analysis counts. While the interface provides visibility into user data, modification capabilities are limited to ensure data integrity and user privacy.

The analysis monitoring component provides visibility into recent analyses across all users. Administrators can view aggregate statistics about condition distributions, model usage patterns, and confidence score distributions. This information can be valuable for identifying potential issues with model performance or unusual usage patterns.

The module implements strict access control to ensure that only authorized staff members can access administrative features. The administrative login flow is separate from the regular user login, providing an additional layer of protection. Access attempts by non-staff users are logged and redirected to appropriate error pages.

The administrative interface is designed to be functional and efficient rather than visually elaborate. The focus is on providing administrators with the information they need to monitor and manage the system effectively. The interface follows consistent design patterns with the rest of the application while clearly indicating its administrative nature.

#### 4.1.7 AI Chatbot Module


The AI Chatbot Module, branded as DermaGenie, provides users with an intelligent conversational interface for skin health queries. This module integrates with the Perplexity AI platform to provide natural language responses to user questions about skin conditions, skin care, and related topics.

The chat interface presents a conversational view where users can type questions and receive responses from the AI assistant. The interface follows familiar messaging application patterns, with user messages displayed on one side and AI responses on the other. The conversation history is maintained throughout the session, allowing for contextual follow-up questions.

The message processing component handles user input and prepares it for submission to the AI service. User messages are validated to ensure they are not empty and do not exceed length limits. The component also implements rate limiting to prevent abuse of the AI service.

The AI integration component communicates with the Perplexity AI API to generate responses. The integration includes a system prompt that establishes DermaGenie's role as a skin health assistant and provides guidelines for appropriate responses. The system prompt emphasizes that responses are for educational purposes only and should not replace professional medical advice.

The response formatting component processes the AI-generated responses and prepares them for display. Responses may include formatting such as bullet points, numbered lists, and emphasis that are rendered appropriately in the chat interface. The component also ensures that responses include appropriate disclaimers when discussing medical topics.

The conversation history is stored in the database, allowing users to review past conversations and enabling the AI to maintain context across multiple messages. Each conversation record includes the user message, AI response, timestamp, and metadata about the AI model used. Users can clear their conversation history if desired.

#### 4.1.8 Email Notification Module


The Email Notification Module handles all email communications from the SkinCare AI system to users. This module integrates with the Resend API for reliable email delivery and supports various notification types including verification emails, analysis notifications, and profile update confirmations.

The email service integration component manages the connection to the Resend API. The integration uses API keys stored in environment variables to authenticate requests. The component handles API responses and implements retry logic for transient failures. Error handling ensures that email delivery failures do not disrupt the user experience.

The email template system provides consistent, professional formatting for all email communications. Templates are defined using HTML with inline CSS for broad email client compatibility. Each template includes the SkinCare AI branding, appropriate content for the notification type, and footer information including unsubscribe options where applicable.

The OTP delivery component sends verification codes for email verification and password reset processes. These emails are given high priority and include clear instructions for entering the OTP. The emails also include information about OTP expiration to help users complete the verification process in time.

The welcome email component sends a greeting message to newly registered users after they verify their email address. The welcome email introduces the key features of SkinCare AI and provides guidance for getting started with the platform.

The analysis notification component sends emails when users complete their first skin analysis. This notification congratulates users on taking a proactive step in monitoring their skin health and provides information about interpreting results and next steps. Subsequent analyses do not trigger notifications to avoid overwhelming users with emails.

The notification preferences system respects user choices about which emails they wish to receive. The module checks user preferences before sending non-essential notifications and provides mechanisms for users to update their preferences. Essential security-related emails such as OTP delivery are always sent regardless of preferences.

---

<!-- PAGE BREAK -->

### 4.2 Methodology


The development of the SkinCare AI system followed an iterative and incremental methodology that combined elements of agile development practices with structured analysis and design phases. This approach enabled flexibility in responding to emerging requirements while maintaining a clear overall direction for the project.

The project began with a requirements gathering phase that identified the core functionality needed for the skin lesion classification system. This phase involved reviewing existing literature on AI-based skin cancer detection, analyzing existing systems and their limitations, and defining the scope and objectives of the proposed system. The requirements were documented and prioritized based on their importance to the core mission of the project.

The system analysis phase examined the technical requirements and constraints of the project. This phase included evaluation of available technologies, assessment of dataset options, and analysis of the computational requirements for model training and inference. The feasibility analysis conducted during this phase confirmed that the project could be successfully implemented using available resources and technologies.

The design phase produced the architectural blueprints for the system, including the module structure, database schema, and user interface designs. The design followed established patterns and best practices for web application development, ensuring that the resulting system would be maintainable and extensible. The dual-model architecture was designed during this phase, along with the intelligent model selection mechanism.

The implementation phase proceeded iteratively, with each iteration focusing on a specific set of features or modules. The core image analysis functionality was implemented first, establishing the foundation for the system. Subsequent iterations added user authentication, profile management, history tracking, analytics, and the AI chatbot. Each iteration included testing to verify that new features worked correctly and did not introduce regressions in existing functionality.


The machine learning model development followed a separate but parallel track. The model training process began with data preparation, including downloading and preprocessing the ISIC 2019 and HAM10000 datasets. Data augmentation techniques were applied to increase the effective size of the training data and improve model generalization. The models were trained using Google Colab, with training progress monitored through TensorBoard visualizations.

Model evaluation was conducted using held-out test sets to assess classification accuracy and identify potential issues such as class imbalance or overfitting. The evaluation metrics included overall accuracy, per-class accuracy, precision, recall, and F1 score. Confusion matrices were generated to visualize the distribution of predictions across classes.

The integration phase combined the trained models with the web application, implementing the model loading, preprocessing, and inference pipelines. This phase required careful attention to ensure that the preprocessing applied during inference matched the preprocessing used during training. The intelligent model selection mechanism was implemented and tuned based on empirical evaluation of model performance.

The testing phase included unit testing of individual components, integration testing of module interactions, and system testing of end-to-end workflows. Test cases were designed to cover both normal operation and edge cases. User acceptance testing was conducted to verify that the system met the defined requirements and provided a satisfactory user experience.

The documentation phase produced comprehensive documentation including this project report, user manuals, and technical documentation. The documentation was developed incrementally throughout the project, with each phase contributing relevant content. The final documentation provides a complete record of the project and guidance for future maintenance and enhancement.

---

<!-- PAGE BREAK -->

### 4.3 Input Design


Input design encompasses the specification of all data inputs to the SkinCare AI system, including user-provided data through forms and file uploads, as well as the preprocessing of image data for model inference. Effective input design ensures data quality, user convenience, and system security.

The user registration form collects the essential information needed to create a new user account. The form includes fields for username, email address, password, and password confirmation. Each field includes validation rules that are enforced both on the client side for immediate feedback and on the server side for security. The username field requires a unique identifier of three to thirty characters. The email field validates the format and checks for uniqueness. The password field requires a minimum length and complexity.

The login form provides a simple interface for user authentication. The form includes fields for username or email and password. The form implements CSRF protection through Django's built-in mechanisms. Failed login attempts display appropriate error messages without revealing whether the username or password was incorrect, preventing enumeration attacks.

The image upload interface is the primary input mechanism for the core analysis functionality. The interface supports multiple input methods including file selection through a standard file dialog and drag-and-drop functionality for convenience. The interface provides visual feedback during the upload process, including progress indication for larger files. Accepted file formats include JPEG, PNG, and other common image formats.

Image validation ensures that uploaded files meet the requirements for analysis. The validation checks include file format verification, file size limits, and basic image integrity checks. Images that fail validation are rejected with appropriate error messages guiding users to provide suitable images. The validation process protects against malicious file uploads and ensures that the analysis pipeline receives valid input.


Image preprocessing transforms uploaded images into the format required by the neural network models. The preprocessing pipeline includes resizing to the target dimensions, color space conversion if necessary, and normalization of pixel values. For the EfficientNetB0 model, images are resized to 224 by 224 pixels and normalized using the preprocessing function specific to the EfficientNet architecture. For the custom CNN model, images are resized to 48 by 48 pixels and normalized to the range zero to one.

The model selection input allows users to specify their preference for which model should be used for analysis. The options include automatic selection, EfficientNetB0 only, and CNN only. The default option is automatic selection, which uses the intelligent model selection mechanism to choose the most appropriate model based on confidence thresholds.

The profile editing form allows users to update their personal information. The form includes fields for biographical information, phone number, date of birth, and profile picture. Each field includes appropriate validation rules. The profile picture upload supports common image formats and automatically resizes images to appropriate dimensions.

The OTP input forms collect verification codes for email verification and password reset processes. These forms include a single field for the six-digit code with appropriate validation. The forms provide clear instructions and indicate the remaining time before the OTP expires.

The chat input interface collects user messages for the DermaGenie AI assistant. The input field supports multi-line text entry and includes a character limit to prevent excessively long messages. The interface provides a send button and supports keyboard shortcuts for message submission.

The search and filter inputs in the history interface allow users to refine the displayed analysis records. Filter options include condition type, date range, and confidence level. Sort options allow ordering by date, condition, or confidence. These inputs use appropriate control types including dropdown menus, date pickers, and range sliders.

---

<!-- PAGE BREAK -->

### 4.4 Output Design


Output design specifies how the SkinCare AI system presents information to users, including analysis results, visualizations, reports, and notifications. Effective output design ensures that information is presented clearly, accurately, and in a manner appropriate for the context and audience.

The analysis results presentation is the primary output of the system and requires careful design to communicate complex information effectively while maintaining appropriate medical disclaimers. The results page displays the analyzed image alongside the prediction results. The predicted condition is prominently displayed with the confidence score shown as a percentage. Educational information about the detected condition is presented in an expandable section.

The results presentation follows a legally-compliant format that clearly communicates the preliminary nature of the assessment. A prominent disclaimer section explains that the results are for educational purposes only and should not be used as a substitute for professional medical evaluation. Recommendations for next steps are provided, with emphasis on consulting a healthcare provider for any concerns.

The confidence score visualization uses a progress bar or gauge to provide an intuitive representation of the model's certainty. The visualization is color-coded to indicate confidence levels, with higher confidence shown in green and lower confidence shown in yellow or orange. Accompanying text explains how to interpret the confidence score.

The history listing output displays analysis records in a structured format that facilitates scanning and comparison. Each record shows a thumbnail image, condition label, confidence score, and timestamp. The listing supports pagination for users with many records and provides visual indicators for different condition types.


The analytics dashboard output presents data visualizations that summarize the user's analysis history. The pie chart showing condition distribution uses distinct colors for each condition type with a legend for identification. The line graph showing analysis frequency over time uses appropriate axis labels and gridlines. Interactive features allow users to hover over data points for detailed information.

The PDF report output provides a professional, printable document summarizing analysis results. The report includes a header with the SkinCare AI branding, the analyzed image, prediction results with confidence scores, educational information about the detected condition, and a footer with medical disclaimers and generation timestamp. The report is formatted for standard paper sizes and includes appropriate margins for printing.

The comparison output displays multiple analyses side by side for easy comparison. Images are displayed at consistent sizes with prediction information aligned below each image. Visual indicators highlight differences between analyses, such as changes in detected condition or confidence level.

The chat output displays AI-generated responses in a conversational format. Responses are formatted with appropriate styling for readability, including support for lists, emphasis, and paragraph breaks. Each response includes a subtle indicator that it was generated by AI and a reminder that the information is for educational purposes only.

The email notification output follows consistent templates that maintain the SkinCare AI branding while being compatible with various email clients. Emails use a responsive design that displays correctly on both desktop and mobile email applications. Important information is highlighted, and clear calls to action guide users to the appropriate next steps.

The error output provides informative messages when operations fail or validation errors occur. Error messages are written in user-friendly language that explains what went wrong and suggests corrective actions. Technical details are logged for debugging purposes but not displayed to users.

---

<!-- PAGE BREAK -->

### 4.5 Data Flow Diagram


Data Flow Diagrams provide a graphical representation of how data moves through the SkinCare AI system, illustrating the processes that transform data, the data stores that hold information, and the external entities that interact with the system. This section presents Data Flow Diagrams at two levels of abstraction: Level 0 (Context Diagram) and Level 1 (Detailed DFD).

**Data Flow Diagram Level 0 (Context Diagram)**

The Context Diagram provides a high-level view of the SkinCare AI system, showing it as a single process that interacts with external entities. This diagram establishes the system boundary and identifies the major data flows between the system and its environment.

```
                                    ┌─────────────────┐
                                    │   Email Service │
                                    │    (Resend)     │
                                    └────────┬────────┘
                                             │
                                    Email Notifications
                                             │
                                             ▼
┌─────────────┐                    ┌─────────────────────┐                    ┌─────────────┐
│             │  Registration      │                     │  AI Queries        │             │
│             │  Login Credentials │                     │  ─────────────────►│  Perplexity │
│             │  ─────────────────►│                     │                    │     AI      │
│             │                    │                     │◄─────────────────  │             │
│    User     │  Image Upload      │    SKINCARE AI      │  AI Responses      └─────────────┘
│             │  ─────────────────►│       SYSTEM        │
│             │                    │                     │
│             │◄─────────────────  │                     │
│             │  Analysis Results  │                     │
│             │  Reports           │                     │
│             │  Notifications     │                     │
└─────────────┘                    └─────────────────────┘
                                             │
                                             │
                                    ┌────────┴────────┐
                                    │                 │
                                    ▼                 ▼
                            ┌─────────────┐   ┌─────────────┐
                            │   Admin     │   │   ML Models │
                            │   User      │   │  (External) │
                            └─────────────┘   └─────────────┘
```


**Explanation of Context Diagram**

The Context Diagram illustrates the SkinCare AI system as a central process that interacts with several external entities. The User entity represents individuals who use the system for skin lesion analysis. Users provide registration information, login credentials, and images for analysis. In return, they receive analysis results, reports, and notifications.

The Email Service entity represents the Resend API used for email delivery. The system sends email notifications to this service, which delivers them to users' email addresses. The Perplexity AI entity represents the external AI service used by the DermaGenie chatbot. The system sends user queries to this service and receives AI-generated responses.

The Admin User entity represents staff members who access the administrative dashboard. They receive system statistics and user management capabilities. The ML Models entity represents the trained neural network models that are loaded by the system for inference.

**Data Flow Diagram Level 1**

The Level 1 DFD decomposes the SkinCare AI system into its major processes, showing how data flows between these processes and the data stores.

```
┌──────────┐                                                              ┌──────────┐
│   User   │                                                              │  Admin   │
└────┬─────┘                                                              └────┬─────┘
     │                                                                         │
     │ Registration Data                                              Admin Credentials
     │ ─────────────────────────────────────────────────────────────────────► │
     │                                                                         │
     ▼                                                                         ▼
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────────────┐
│                 │         │                 │         │                         │
│  1.0 User       │────────►│   D1: Users     │◄────────│  6.0 Admin              │
│  Authentication │         │   Database      │         │  Dashboard              │
│                 │◄────────│                 │────────►│                         │
└────────┬────────┘         └─────────────────┘         └─────────────────────────┘
         │                           │
         │ Session Data              │ User Data
         ▼                           ▼
┌─────────────────┐         ┌─────────────────┐
│                 │         │                 │
│  2.0 Image      │────────►│  D2: Analysis   │
│  Analysis       │         │  Records        │
│                 │◄────────│                 │
└────────┬────────┘         └────────┬────────┘
         │                           │
         │ Prediction Request        │ History Data
         ▼                           ▼
┌─────────────────┐         ┌─────────────────┐
│                 │         │                 │
│  3.0 ML Model   │         │  4.0 History    │
│  Inference      │         │  Management     │
│                 │         │                 │
└─────────────────┘         └─────────────────┘
```


**Explanation of Level 1 DFD**

Process 1.0 User Authentication handles user registration, login, logout, and email verification. This process receives registration data and login credentials from users, validates them, and creates or authenticates user sessions. User data is stored in and retrieved from the Users Database (D1).

Process 2.0 Image Analysis handles the core skin lesion classification functionality. This process receives uploaded images from authenticated users, validates and preprocesses the images, and invokes the ML Model Inference process. Analysis results are stored in the Analysis Records data store (D2).

Process 3.0 ML Model Inference performs the actual classification using the trained neural network models. This process receives preprocessed images from the Image Analysis process, loads the appropriate model based on user preference or automatic selection, and returns prediction results including class labels and confidence scores.

Process 4.0 History Management provides access to past analysis records. This process retrieves records from the Analysis Records data store based on user queries and filtering criteria. It also supports the comparison feature by retrieving multiple records for side-by-side display.

Process 5.0 Profile Management (not shown in simplified diagram) handles user profile viewing and editing. This process retrieves and updates user profile data in the Users Database.

Process 6.0 Admin Dashboard provides administrative functionality for staff users. This process retrieves aggregate statistics from both the Users Database and Analysis Records data store, presenting system-wide metrics to administrators.

The data stores D1 (Users Database) and D2 (Analysis Records) represent the persistent storage for user account information and analysis history respectively. These data stores are implemented using Django's ORM with SQLite as the default database backend.

---

<!-- PAGE BREAK -->

### 4.6 Architecture Diagram


The System Architecture Diagram provides a comprehensive view of the SkinCare AI system's structure, showing the major components, their relationships, and the technologies used at each layer. This diagram serves as a blueprint for understanding how the system is organized and how different components interact.

**System Architecture Diagram**

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              PRESENTATION LAYER                                  │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                         Client Browsers                                  │   │
│  │   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐               │   │
│  │   │   Desktop    │   │    Mobile    │   │    Tablet    │               │   │
│  │   │   Browser    │   │   Browser    │   │   Browser    │               │   │
│  │   └──────────────┘   └──────────────┘   └──────────────┘               │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                      │                                          │
│                              HTTPS / HTTP                                       │
│                                      ▼                                          │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                    Django Template Engine                                │   │
│  │   HTML5 + CSS3 + JavaScript + Chart.js + Font Awesome                   │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              APPLICATION LAYER                                   │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                      Django Web Framework 4.2.1                          │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐        │   │
│  │  │   URL      │  │   Views    │  │   Forms    │  │ Middleware │        │   │
│  │  │  Routing   │  │            │  │            │  │            │        │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘        │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                      Business Logic Components                           │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐        │   │
│  │  │   Auth     │  │  Analysis  │  │   Email    │  │    AI      │        │   │
│  │  │  Module    │  │   Module   │  │   Module   │  │  Assistant │        │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘        │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           MACHINE LEARNING LAYER                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                    TensorFlow 2.13.0 / Keras 2.13.1                      │   │
│  │  ┌─────────────────────────┐    ┌─────────────────────────┐             │   │
│  │  │    EfficientNetB0       │    │      Custom CNN         │             │   │
│  │  │    (Primary Model)      │    │   (Secondary Model)     │             │   │
│  │  │    224x224 Input        │    │     48x48 Input         │             │   │
│  │  │    8 Classes            │    │     8 Classes           │             │   │
│  │  └─────────────────────────┘    └─────────────────────────┘             │   │
│  │                    ┌─────────────────────────┐                           │   │
│  │                    │   Model Selection       │                           │   │
│  │                    │   Logic                 │                           │   │
│  │                    └─────────────────────────┘                           │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                               DATA LAYER                                         │
│  ┌──────────────────────────┐    ┌──────────────────────────┐                  │
│  │      SQLite Database     │    │      File Storage        │                  │
│  │  ┌────────────────────┐  │    │  ┌────────────────────┐  │                  │
│  │  │  Users             │  │    │  │  Uploaded Images   │  │                  │
│  │  │  UserProfiles      │  │    │  │  Profile Pictures  │  │                  │
│  │  │  UserPredictModel  │  │    │  │  Model Files (.h5) │  │                  │
│  │  │  EmailOTP          │  │    │  │  Static Assets     │  │                  │
│  │  │  ChatConversation  │  │    │  └────────────────────┘  │                  │
│  │  └────────────────────┘  │    └──────────────────────────┘                  │
│  └──────────────────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           EXTERNAL SERVICES                                      │
│  ┌──────────────────────────┐    ┌──────────────────────────┐                  │
│  │      Resend API          │    │     Perplexity AI        │                  │
│  │   (Email Delivery)       │    │    (Chatbot Backend)     │                  │
│  └──────────────────────────┘    └──────────────────────────┘                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```


**Explanation of System Architecture**

The Presentation Layer encompasses all user-facing components of the system. Client browsers on desktop, mobile, and tablet devices access the application through HTTP/HTTPS protocols. The Django Template Engine renders HTML pages using templates that incorporate CSS3 for styling, JavaScript for interactivity, Chart.js for data visualizations, and Font Awesome for icons. The responsive design ensures consistent user experience across different device types and screen sizes.

The Application Layer contains the core business logic of the SkinCare AI system. The Django Web Framework provides the foundation, including URL routing that maps incoming requests to appropriate view functions, views that process requests and generate responses, forms that handle user input validation, and middleware that provides cross-cutting functionality such as authentication and security.

The Business Logic Components implement the specific functionality of each module. The Auth Module handles user authentication and authorization. The Analysis Module manages image upload, preprocessing, and result presentation. The Email Module handles email notification delivery. The AI Assistant module manages the DermaGenie chatbot functionality.

The Machine Learning Layer contains the deep learning components responsible for skin lesion classification. TensorFlow and Keras provide the framework for loading and executing the trained models. The EfficientNetB0 model serves as the primary classifier, accepting 224x224 pixel images and producing predictions across eight classes. The Custom CNN model serves as the secondary classifier, accepting 48x48 pixel images. The Model Selection Logic determines which model to use based on user preferences and confidence thresholds.

The Data Layer provides persistent storage for application data. The SQLite Database stores structured data including user accounts, profiles, analysis records, OTP tokens, and chat conversations. File Storage holds binary data including uploaded images, profile pictures, trained model files, and static assets such as CSS, JavaScript, and image files.

The External Services layer represents third-party services that the system integrates with. The Resend API provides reliable email delivery for notifications and verification emails. The Perplexity AI service provides natural language processing capabilities for the DermaGenie chatbot.

---

<!-- PAGE BREAK -->

### 4.7 Database Design

#### 4.7.1 ER Diagram


The Entity-Relationship Diagram illustrates the logical structure of the database, showing the entities (tables), their attributes, and the relationships between them. This diagram provides a foundation for understanding how data is organized and related within the SkinCare AI system.

**Entity-Relationship Diagram**

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│    ┌───────────────────┐                      ┌───────────────────┐            │
│    │       USER        │                      │    USERPROFILE    │            │
│    ├───────────────────┤                      ├───────────────────┤            │
│    │ PK  id            │                      │ PK  id            │            │
│    │     username      │        1:1           │ FK  user_id       │            │
│    │     email         │◄─────────────────────│     bio           │            │
│    │     password      │                      │     phone         │            │
│    │     first_name    │                      │     date_of_birth │            │
│    │     last_name     │                      │     profile_pic   │            │
│    │     is_active     │                      │     email_verified│            │
│    │     is_staff      │                      │     email_notifs  │            │
│    │     date_joined   │                      │     first_email   │            │
│    └─────────┬─────────┘                      │     created_at    │            │
│              │                                │     updated_at    │            │
│              │                                └───────────────────┘            │
│              │                                                                  │
│              │ 1:N                                                              │
│              │                                                                  │
│              ▼                                                                  │
│    ┌───────────────────┐                      ┌───────────────────┐            │
│    │ USERPREDICTMODEL  │                      │     EMAILOTP      │            │
│    ├───────────────────┤                      ├───────────────────┤            │
│    │ PK  id            │                      │ PK  id            │            │
│    │ FK  user_id       │                      │ FK  user_id       │            │
│    │     image         │        1:N           │     otp           │            │
│    │     label         │◄─────────────────────│     created_at    │            │
│    │     model_pref    │                      │     is_verified   │            │
│    │     model_used    │                      └───────────────────┘            │
│    │     confidence    │                                                        │
│    │     created_at    │                      ┌───────────────────┐            │
│    └───────────────────┘                      │ PASSWORDRESETOTP  │            │
│                                               ├───────────────────┤            │
│              │                                │ PK  id            │            │
│              │ 1:N                            │ FK  user_id       │            │
│              │                                │     otp           │            │
│              ▼                                │     created_at    │            │
│    ┌───────────────────┐                      │     is_used       │            │
│    │ CHATCONVERSATION  │                      └───────────────────┘            │
│    ├───────────────────┤                                                        │
│    │ PK  id            │                                                        │
│    │ FK  user_id       │                                                        │
│    │     user_message  │                                                        │
│    │     ai_response   │                                                        │
│    │     tokens_used   │                                                        │
│    │     model         │                                                        │
│    │     created_at    │                                                        │
│    └───────────────────┘                                                        │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```


**Explanation of ER Diagram**

The User entity represents registered users of the SkinCare AI system. This entity is provided by Django's built-in authentication system and includes standard fields for user identification and authentication. The primary key is an auto-incrementing integer id. The username and email fields provide unique identifiers for the user. The password field stores the hashed password. The is_active and is_staff fields control account status and administrative access. The date_joined field records when the account was created.

The UserProfile entity extends the User entity with additional profile information specific to the SkinCare AI application. This entity has a one-to-one relationship with User, meaning each user has exactly one profile. The profile includes biographical information, contact details, profile picture path, email verification status, notification preferences, and timestamps for creation and last update.

The UserPredictModel entity stores records of skin lesion analyses performed by users. This entity has a many-to-one relationship with User, meaning each user can have multiple analysis records. Each record includes the path to the uploaded image, the predicted label, the model preference specified by the user, the model actually used for prediction, the confidence score, and the timestamp of the analysis.

The EmailOTP entity stores One-Time Passwords used for email verification during registration. This entity has a many-to-one relationship with User, as a user may have multiple OTP records if they request new codes. Each record includes the OTP value, creation timestamp, and verification status.

The PasswordResetOTP entity stores One-Time Passwords used for password reset functionality. Similar to EmailOTP, this entity has a many-to-one relationship with User. Each record includes the OTP value, creation timestamp, and a flag indicating whether the OTP has been used.

The ChatConversation entity stores the conversation history for the DermaGenie AI assistant. This entity has a many-to-one relationship with User, as each user can have multiple conversation entries. Each record includes the user's message, the AI's response, token usage information, the AI model used, and the timestamp.

#### 4.7.2 Table Description


This section provides detailed descriptions of each database table, including field names, data types, constraints, and descriptions.

**Table: auth_user (Django Built-in User Table)**

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier for the user |
| username | VARCHAR(150) | UNIQUE, NOT NULL | Username for login |
| email | VARCHAR(254) | NOT NULL | User's email address |
| password | VARCHAR(128) | NOT NULL | Hashed password |
| first_name | VARCHAR(150) | | User's first name |
| last_name | VARCHAR(150) | | User's last name |
| is_active | BOOLEAN | DEFAULT TRUE | Account active status |
| is_staff | BOOLEAN | DEFAULT FALSE | Staff access flag |
| is_superuser | BOOLEAN | DEFAULT FALSE | Superuser access flag |
| date_joined | DATETIME | NOT NULL | Account creation timestamp |
| last_login | DATETIME | | Last login timestamp |

**Table: APP_userprofile**

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| user_id | INTEGER | FOREIGN KEY, UNIQUE | Reference to auth_user |
| bio | TEXT | | Biographical information |
| phone | VARCHAR(20) | | Phone number |
| date_of_birth | DATE | | Date of birth |
| profile_picture | VARCHAR(100) | | Path to profile image |
| email_verified | BOOLEAN | DEFAULT FALSE | Email verification status |
| email_notifications | BOOLEAN | DEFAULT TRUE | Notification preference |
| first_analysis_email_sent | BOOLEAN | DEFAULT FALSE | First email sent flag |
| created_at | DATETIME | AUTO NOW ADD | Profile creation timestamp |
| updated_at | DATETIME | AUTO NOW | Last update timestamp |


**Table: APP_userpredictmodel**

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| user_id | INTEGER | FOREIGN KEY | Reference to auth_user |
| image | VARCHAR(100) | NOT NULL | Path to uploaded image |
| label | VARCHAR(100) | NOT NULL | Predicted condition label |
| model_preference | VARCHAR(20) | DEFAULT 'auto' | User's model preference |
| model_used | VARCHAR(50) | | Model actually used |
| confidence_score | FLOAT | | Prediction confidence |
| created_at | DATETIME | AUTO NOW ADD | Analysis timestamp |

**Table: APP_emailotp**

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| user_id | INTEGER | FOREIGN KEY | Reference to auth_user |
| otp | VARCHAR(6) | NOT NULL | Six-digit OTP code |
| created_at | DATETIME | AUTO NOW ADD | OTP creation timestamp |
| is_verified | BOOLEAN | DEFAULT FALSE | Verification status |

**Table: APP_passwordresetotp**

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| user_id | INTEGER | FOREIGN KEY | Reference to auth_user |
| otp | VARCHAR(6) | NOT NULL | Six-digit OTP code |
| created_at | DATETIME | AUTO NOW ADD | OTP creation timestamp |
| is_used | BOOLEAN | DEFAULT FALSE | Usage status |

**Table: APP_chatconversation**

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| user_id | INTEGER | FOREIGN KEY | Reference to auth_user |
| user_message | TEXT | NOT NULL | User's chat message |
| ai_response | TEXT | NOT NULL | AI-generated response |
| tokens_used | INTEGER | | API tokens consumed |
| model | VARCHAR(50) | | AI model identifier |
| created_at | DATETIME | AUTO NOW ADD | Message timestamp |

---

<!-- PAGE BREAK -->

## CHAPTER 5: SYSTEM IMPLEMENTATION

### 5.1 Frontend Implementation


The frontend implementation of SkinCare AI encompasses all user-facing components of the application, including HTML templates, CSS stylesheets, and JavaScript functionality. The frontend is designed to provide an intuitive, responsive, and visually appealing user experience across different devices and screen sizes.

The template architecture follows Django's template inheritance system, with a base template that defines the common structure shared by all pages. The base template includes the HTML document structure, meta tags for responsive design, links to CSS stylesheets, the navigation header, and footer content. Child templates extend the base template and override specific blocks to provide page-specific content.

The navigation system provides consistent access to all major features of the application. The navigation bar includes links to the home page, analysis page, history, analytics, profile, and the DermaGenie chatbot. For authenticated users, the navigation displays the username and provides a logout option. For unauthenticated users, links to login and registration are displayed. The navigation is responsive, collapsing to a hamburger menu on smaller screens.

The visual design follows a dark, futuristic theme that conveys professionalism and technological sophistication. The color palette centers on deep purple and cyan accent colors against dark backgrounds. Typography uses clean, modern fonts that ensure readability across different screen sizes. Visual hierarchy is established through size, color, and spacing to guide users' attention to important elements.

The CSS implementation uses a combination of custom stylesheets and utility classes. The main stylesheet defines global styles, color variables, and component styles. Additional stylesheets provide specific functionality such as mobile responsiveness, tooltips, and the floating video background on the landing page. CSS custom properties enable consistent theming and easy customization.


The responsive design implementation ensures that the application functions well on devices ranging from large desktop monitors to small smartphone screens. Media queries adjust layout, typography, and component sizing based on viewport width. The mobile navigation provides a touch-friendly interface with appropriately sized tap targets. Images and other media are responsive, scaling appropriately to fit available space.

The JavaScript implementation provides interactive functionality throughout the application. The image upload interface includes drag-and-drop functionality with visual feedback during the drag operation. Form validation provides immediate feedback on input errors before submission. The analytics dashboard uses Chart.js to render interactive charts that respond to user interactions such as hovering and clicking.

The DermaGenie chat interface implements a real-time messaging experience. User messages are displayed immediately upon submission, with a loading indicator shown while waiting for the AI response. The chat history scrolls automatically to show the most recent messages. The interface supports keyboard shortcuts for message submission.

Accessibility considerations are incorporated throughout the frontend implementation. Semantic HTML elements provide structure that assistive technologies can interpret. Form inputs include appropriate labels and ARIA attributes. Color contrast ratios meet accessibility guidelines for readability. Keyboard navigation is supported for all interactive elements.

The landing page features a floating video background that creates a premium, engaging first impression. The video plays automatically, is muted, and loops continuously. CSS animations create a subtle floating effect that adds visual interest without being distracting. The video is loaded only on the landing page to minimize bandwidth usage on other pages.

### 5.2 Backend Implementation


The backend implementation of SkinCare AI is built on the Django framework, providing a robust foundation for handling HTTP requests, managing database operations, and implementing business logic. The backend follows Django's conventions and best practices to ensure maintainability and security.

The project structure follows Django's recommended organization, with the main project directory containing settings, URL configuration, and WSGI/ASGI entry points. The APP directory contains the application-specific code including models, views, forms, and utility modules. Static files and templates are organized in dedicated directories.

The URL routing configuration maps incoming requests to appropriate view functions. The URL patterns are defined using Django's path function, with named URLs that can be referenced in templates and redirects. The routing supports both function-based views and class-based views where appropriate.

The view implementation handles request processing and response generation. Views are implemented as functions that receive HTTP request objects and return HTTP response objects. The views use Django's authentication decorators to restrict access to authenticated users where required. Form processing follows Django's standard pattern of checking request method, validating form data, and either processing valid data or re-rendering the form with errors.

The model implementation defines the database schema using Django's ORM. Models are defined as Python classes that inherit from Django's Model class. Fields are defined using appropriate field types with constraints and options. Relationships between models are defined using ForeignKey and OneToOneField. Model methods provide convenient access to computed properties and related data.


The form implementation provides validation and processing for user input. Forms are defined as classes that inherit from Django's Form or ModelForm classes. Field validation is implemented using built-in validators and custom validation methods. Form rendering in templates uses Django's form rendering utilities with custom styling.

The utility modules encapsulate reusable functionality that is used across multiple views. The email_utils module provides functions for sending various types of email notifications. The otp_utils module handles OTP generation and verification. The password_reset_utils module manages the password reset workflow. The result_formatter module formats analysis results with appropriate educational content and disclaimers.

The AI assistant integration is implemented in the ai_assistant module. This module handles communication with the Perplexity AI API, including request formatting, response parsing, and error handling. The system prompt establishes DermaGenie's persona and guidelines for appropriate responses.

The PDF generation functionality is implemented in the pdf_utils module. This module uses the ReportLab library to generate professional PDF documents. The generated PDFs include the SkinCare AI branding, analysis results, educational content, and medical disclaimers.

The settings configuration manages application settings for different environments. Sensitive settings such as API keys and database credentials are loaded from environment variables using the python-dotenv library. The settings file includes configurations for database connections, static file handling, email backend, and security settings.

### 5.3 Machine Learning Model Implementation


The machine learning model implementation encompasses the integration of trained neural network models into the SkinCare AI web application. This implementation includes model loading, image preprocessing, inference execution, and result interpretation.

The model loading process occurs during application startup to ensure that models are ready for inference when requests arrive. The TensorFlow library's load_model function is used to load the saved model files in HDF5 format. The EfficientNetB0 model and custom CNN model are loaded into memory and stored in global variables for efficient access during inference.

The image preprocessing pipeline transforms uploaded images into the format expected by the neural network models. For the EfficientNetB0 model, images are resized to 224 by 224 pixels using Pillow's resize function with high-quality resampling. The pixel values are then normalized using the preprocessing function specific to the EfficientNet architecture, which scales values to the range expected by the model.

For the custom CNN model, images are resized to 48 by 48 pixels. The pixel values are normalized to the range zero to one by dividing by 255. The preprocessed image is converted to a NumPy array and reshaped to include the batch dimension expected by the model.

The inference execution passes the preprocessed image through the selected model to generate predictions. The model's predict method returns an array of probabilities for each class. The class with the highest probability is selected as the predicted label. The probability value for the predicted class is extracted as the confidence score.


The intelligent model selection mechanism implements the logic for choosing between the primary and secondary models. When the user selects automatic mode, the system first runs inference using the EfficientNetB0 model. If the confidence score exceeds the threshold of 0.5, the EfficientNetB0 result is used. If the confidence is below the threshold, the system runs inference using the custom CNN model and uses that result instead.

The class label mapping translates numeric class indices to human-readable condition names. The mapping is defined as a dictionary that associates each index with the corresponding condition name. The mapping is consistent with the class ordering used during model training.

The result interpretation component generates educational content based on the predicted condition. A dictionary of condition information provides descriptions, risk levels, and recommendations for each condition. This information is combined with the prediction results to create a comprehensive result presentation.

Error handling ensures that the system responds gracefully to unexpected situations. If model loading fails, appropriate error messages are logged and displayed. If inference fails due to invalid input, users receive helpful error messages. The system includes fallback behavior to ensure that users always receive a response, even if the preferred model is unavailable.

### 5.4 Model Training Process

The model training process was conducted using Google Colab, which provided free access to GPU-accelerated computing resources. This section describes the training process for both the EfficientNetB0 model and the custom CNN model.


The data preparation phase involved downloading and preprocessing the training datasets. The ISIC 2019 dataset was downloaded from the ISIC Archive and organized into directories by class label. The HAM10000 subset was similarly organized. Data augmentation was applied to increase the effective size of the training data and improve model generalization.

The data augmentation techniques included random rotation within a range of twenty degrees, random horizontal and vertical flipping, random zoom within a range of ten percent, and random brightness adjustment. These augmentations were applied on-the-fly during training using Keras's ImageDataGenerator class.

The dataset splitting divided the data into training, validation, and test sets. The training set, comprising seventy percent of the data, was used to update model weights. The validation set, comprising fifteen percent, was used to monitor training progress and tune hyperparameters. The test set, comprising the remaining fifteen percent, was held out for final evaluation.

The EfficientNetB0 model training began with loading the pre-trained EfficientNetB0 model with ImageNet weights. The top classification layers were removed, and custom layers were added for the eight-class skin lesion classification task. The custom layers included a Global Average Pooling layer, a Dense layer with 256 units and ReLU activation, a Dropout layer with rate 0.5, and a final Dense layer with 8 units and softmax activation.

The training configuration for EfficientNetB0 used the Adam optimizer with a learning rate of 0.0001. The categorical cross-entropy loss function was used for multi-class classification. The model was trained for 50 epochs with a batch size of 32. Early stopping was implemented to halt training if validation loss did not improve for 10 consecutive epochs.


The custom CNN model architecture was designed specifically for the HAM10000 subset. The architecture consists of three convolutional blocks, each containing a convolutional layer, ReLU activation, and max pooling. The first block uses 32 filters, the second uses 64 filters, and the third uses 128 filters. All convolutional layers use 3x3 kernels. The convolutional blocks are followed by a flatten layer, a dense layer with 256 units and ReLU activation, a dropout layer with rate 0.5, and a final dense layer with 8 units and softmax activation.

The training configuration for the custom CNN used the Adam optimizer with a learning rate of 0.001. The model was trained for 100 epochs with a batch size of 64. Learning rate reduction was implemented to decrease the learning rate by a factor of 0.5 if validation loss did not improve for 5 consecutive epochs.

The training progress was monitored using TensorBoard, which provided visualizations of training and validation loss, accuracy metrics, and learning rate changes. These visualizations helped identify issues such as overfitting and guided hyperparameter tuning decisions.

The trained models were saved in HDF5 format using Keras's save method. The saved files include the model architecture, trained weights, optimizer state, and training configuration. These files are loaded by the web application for inference.

### 5.5 Model Evaluation Metrics

The model evaluation phase assessed the performance of the trained models using various metrics. This evaluation provides insight into model accuracy, strengths, and limitations.


The overall accuracy metric measures the proportion of correct predictions across all classes. The EfficientNetB0 model achieved a test accuracy of 71.32 percent on the ISIC 2019 dataset. The custom CNN model achieved a test accuracy of 94.1 percent on the HAM10000 subset. The difference in accuracy reflects both the different datasets and the different model architectures.

The per-class accuracy analysis reveals how well each model performs on individual condition categories. Both models show higher accuracy on classes with more training examples, such as Melanocytic Nevi, and lower accuracy on classes with fewer examples, such as Dermatofibroma. This pattern reflects the class imbalance present in the training datasets.

The precision metric measures the proportion of positive predictions that are correct. High precision indicates that when the model predicts a particular condition, it is likely to be correct. Precision is particularly important for conditions where false positives could cause unnecessary anxiety or medical procedures.

The recall metric measures the proportion of actual positive cases that are correctly identified. High recall indicates that the model successfully identifies most cases of a particular condition. Recall is particularly important for potentially serious conditions like melanoma, where missing a case could have severe consequences.

The F1 score provides a balanced measure that combines precision and recall. The F1 score is the harmonic mean of precision and recall, providing a single metric that accounts for both false positives and false negatives. This metric is useful for comparing model performance across classes with different prevalence.

The confusion matrix provides a detailed view of model predictions, showing the distribution of predictions across all class combinations. The diagonal elements represent correct predictions, while off-diagonal elements represent misclassifications. Analysis of the confusion matrix reveals which conditions are most commonly confused with each other.

### 5.6 Security Implementation


The security implementation of SkinCare AI encompasses multiple layers of protection to safeguard user data, prevent unauthorized access, and ensure system integrity. This section describes the security measures implemented throughout the application.

Password security is implemented using Django's built-in password hashing system. Passwords are hashed using the PBKDF2 algorithm with SHA256, which applies multiple iterations of hashing to make brute-force attacks computationally expensive. The hashed passwords are stored in the database, and plaintext passwords are never stored or logged.

Session management uses Django's session framework with secure cookie settings. Session data is stored on the server, with only a session identifier transmitted in cookies. Sessions are configured to expire after a period of inactivity. The session cookie is marked as HTTP-only to prevent access from JavaScript, reducing the risk of session hijacking through XSS attacks.

Cross-Site Request Forgery protection is enabled by default in Django. All forms include CSRF tokens that are validated on submission. This protection ensures that requests originate from the application's own forms rather than from malicious third-party sites.

Cross-Site Scripting protection is provided through Django's template system, which automatically escapes variables to prevent injection of malicious scripts. User-provided content is sanitized before display to ensure that any HTML or JavaScript is rendered as text rather than executed.

SQL injection prevention is achieved through the use of Django's ORM, which uses parameterized queries for all database operations. User input is never directly interpolated into SQL queries, eliminating the risk of SQL injection attacks.


File upload security includes validation of uploaded files to ensure they are valid images. File type checking verifies that uploaded files have appropriate extensions and MIME types. File size limits prevent denial-of-service attacks through excessively large uploads. Uploaded files are stored with generated filenames to prevent path traversal attacks.

Environment variable management keeps sensitive configuration data out of the source code. API keys, database credentials, and other secrets are stored in environment variables that are loaded at runtime. The .env file containing these variables is excluded from version control through .gitignore.

Access control ensures that users can only access their own data. Database queries are filtered by the authenticated user's identity. Views that require authentication use Django's login_required decorator to redirect unauthenticated users. Administrative functions are protected by additional staff-only access checks.

Input validation is performed on all user-provided data. Form fields include appropriate validators that check data format, length, and content. Server-side validation is always performed, even when client-side validation is also present, to ensure that validation cannot be bypassed.

Error handling is implemented to prevent information disclosure. Detailed error messages and stack traces are logged for debugging but not displayed to users. Users receive generic error messages that do not reveal implementation details that could be exploited by attackers.

---

<!-- PAGE BREAK -->

## CHAPTER 6: SYSTEM TESTING

### 6.1 Testing Strategy


The testing strategy for SkinCare AI encompasses multiple levels of testing to ensure that the system functions correctly, meets requirements, and provides a satisfactory user experience. The strategy combines automated testing with manual testing to achieve comprehensive coverage.

The testing approach follows the testing pyramid model, with a broad base of unit tests, a middle layer of integration tests, and a smaller number of end-to-end tests at the top. This approach ensures that defects are caught at the lowest possible level, where they are easiest and cheapest to fix.

The test environment mirrors the production environment as closely as possible while allowing for controlled testing conditions. A separate test database is used to avoid affecting production data. Test fixtures provide consistent initial data for tests. Environment variables are configured for the test environment.

The test data strategy uses a combination of real data samples and synthetic data. Real dermoscopic images from the test set are used to verify model inference. Synthetic user data is generated for testing user management features. Edge cases and boundary conditions are specifically targeted with crafted test data.

The defect tracking process documents discovered issues and tracks their resolution. Each defect is assigned a severity level based on its impact on system functionality. Defects are prioritized for resolution based on severity and the affected functionality. Resolution is verified through regression testing.

The testing schedule allocates time for testing throughout the development process. Unit tests are written alongside the code they test. Integration testing is performed after each major feature is completed. System testing is performed before each release. User acceptance testing is conducted with representative users.

### 6.2 Unit Testing


Unit testing focuses on testing individual components in isolation to verify that they function correctly. Unit tests are automated and can be run quickly, providing rapid feedback during development.

The model unit tests verify that the machine learning models produce expected outputs for known inputs. Tests verify that models load successfully without errors. Tests verify that preprocessing functions produce correctly shaped and normalized arrays. Tests verify that inference produces probability distributions that sum to one.

The view unit tests verify that view functions handle requests correctly. Tests verify that views return appropriate HTTP status codes. Tests verify that views render the correct templates. Tests verify that views handle both valid and invalid input appropriately.

The form unit tests verify that form validation works correctly. Tests verify that valid data passes validation. Tests verify that invalid data fails validation with appropriate error messages. Tests verify that form cleaning and processing produce expected results.

The utility function unit tests verify that helper functions work correctly. Tests verify OTP generation produces valid codes. Tests verify email formatting produces correct output. Tests verify result formatting includes required elements.

The model method unit tests verify that custom model methods work correctly. Tests verify that computed properties return expected values. Tests verify that relationship traversal works correctly. Tests verify that string representations are appropriate.

### 6.3 Integration Testing


Integration testing verifies that different components of the system work together correctly. These tests focus on the interactions between modules and the data flow through the system.

The authentication integration tests verify the complete authentication workflow. Tests verify that registration creates user accounts and profiles. Tests verify that email verification updates account status. Tests verify that login creates sessions for valid credentials. Tests verify that logout invalidates sessions.

The analysis integration tests verify the complete image analysis workflow. Tests verify that image upload stores files correctly. Tests verify that preprocessing and inference produce results. Tests verify that results are stored in the database. Tests verify that results are displayed correctly.

The profile integration tests verify profile management functionality. Tests verify that profile updates are persisted to the database. Tests verify that profile picture uploads are stored correctly. Tests verify that notification preferences affect email delivery.

The history integration tests verify history and comparison functionality. Tests verify that analysis records are retrieved correctly. Tests verify that filtering and sorting work as expected. Tests verify that comparison displays multiple records correctly.

The email integration tests verify email notification functionality. Tests verify that OTP emails are sent during registration. Tests verify that welcome emails are sent after verification. Tests verify that notification preferences are respected.

### 6.4 Validation Testing


Validation testing verifies that the system meets the specified requirements and provides the expected functionality. This testing focuses on ensuring that the system does what it is supposed to do from the user's perspective.

The functional requirements validation verifies that all specified features are implemented and working. Each functional requirement is traced to one or more test cases. Tests verify that the feature works as specified. Any deviations from requirements are documented and addressed.

The user interface validation verifies that the interface meets usability requirements. Tests verify that all pages render correctly without errors. Tests verify that navigation works as expected. Tests verify that forms provide appropriate feedback. Tests verify that the interface is responsive across device sizes.

The performance validation verifies that the system meets performance requirements. Tests measure page load times under normal conditions. Tests measure inference time for image analysis. Tests verify that the system remains responsive under load.

The security validation verifies that security requirements are met. Tests verify that authentication is required for protected pages. Tests verify that users cannot access other users' data. Tests verify that input validation prevents malicious input.

The compatibility validation verifies that the system works across different environments. Tests verify functionality in different web browsers. Tests verify functionality on different operating systems. Tests verify functionality on different device types.

### 6.5 Test Case Design


Test case design follows established principles to ensure comprehensive coverage while maintaining efficiency. This section describes the approaches used to design effective test cases.

The equivalence partitioning technique divides input domains into classes where all values in a class are expected to be treated equivalently. Test cases are designed to cover each equivalence class. For example, password validation might have classes for too short, valid length, and too long passwords.

The boundary value analysis technique focuses on values at the edges of equivalence classes, where defects are most likely to occur. Test cases are designed for values at, just below, and just above boundaries. For example, if the minimum password length is 8, tests would use passwords of length 7, 8, and 9.

The decision table technique is used for features with multiple conditions that affect the outcome. A table is constructed showing all combinations of conditions and the expected outcomes. Test cases are designed to cover each combination. This technique is particularly useful for complex business logic.

The state transition technique is used for features where behavior depends on the current state. A state diagram is constructed showing states and transitions. Test cases are designed to cover each state and transition. This technique is useful for testing workflows like the registration process.

The error guessing technique leverages experience to identify likely defects. Test cases are designed based on common programming errors, known problem areas, and intuition about where defects might occur. This technique complements systematic techniques by targeting areas that might be missed.

### 6.6 Sample Test Cases


This section presents sample test cases for key functionality of the SkinCare AI system. Each test case includes an identifier, description, preconditions, test steps, expected results, and actual results.

**Table 6.1: User Authentication Test Cases**

| Test ID | Description | Preconditions | Steps | Expected Result | Status |
|---------|-------------|---------------|-------|-----------------|--------|
| TC-AUTH-001 | Valid user registration | None | 1. Navigate to registration page 2. Enter valid username, email, password 3. Submit form | User account created, OTP sent | Pass |
| TC-AUTH-002 | Registration with existing username | User exists | 1. Navigate to registration 2. Enter existing username 3. Submit | Error message displayed | Pass |
| TC-AUTH-003 | Valid email verification | Unverified user | 1. Enter correct OTP 2. Submit | Email verified, redirect to login | Pass |
| TC-AUTH-004 | Expired OTP verification | OTP older than 10 min | 1. Enter OTP 2. Submit | Error: OTP expired | Pass |
| TC-AUTH-005 | Valid login | Verified user | 1. Enter credentials 2. Submit | Session created, redirect to home | Pass |
| TC-AUTH-006 | Login with wrong password | Valid user | 1. Enter wrong password 2. Submit | Error message displayed | Pass |
| TC-AUTH-007 | Logout | Logged in user | 1. Click logout | Session ended, redirect to login | Pass |
| TC-AUTH-008 | Password reset request | Valid user | 1. Enter email 2. Submit | OTP sent to email | Pass |

**Table 6.2: Image Analysis Test Cases**

| Test ID | Description | Preconditions | Steps | Expected Result | Status |
|---------|-------------|---------------|-------|-----------------|--------|
| TC-ANAL-001 | Valid image analysis | Logged in | 1. Upload valid image 2. Select model 3. Submit | Analysis results displayed | Pass |
| TC-ANAL-002 | Invalid file type | Logged in | 1. Upload non-image file 2. Submit | Error: Invalid file type | Pass |
| TC-ANAL-003 | Auto model selection | Logged in | 1. Upload image 2. Select auto 3. Submit | Appropriate model used | Pass |
| TC-ANAL-004 | EfficientNet selection | Logged in | 1. Upload image 2. Select EfficientNet 3. Submit | EfficientNet model used | Pass |
| TC-ANAL-005 | CNN selection | Logged in | 1. Upload image 2. Select CNN 3. Submit | CNN model used | Pass |
| TC-ANAL-006 | Analysis without login | Not logged in | 1. Navigate to analysis page | Redirect to login | Pass |
| TC-ANAL-007 | Large file upload | Logged in | 1. Upload file exceeding limit | Error: File too large | Pass |
| TC-ANAL-008 | Result includes disclaimer | Logged in | 1. Complete analysis | Medical disclaimer displayed | Pass |


**Table 6.3: Profile Management Test Cases**

| Test ID | Description | Preconditions | Steps | Expected Result | Status |
|---------|-------------|---------------|-------|-----------------|--------|
| TC-PROF-001 | View profile | Logged in | 1. Navigate to profile | Profile information displayed | Pass |
| TC-PROF-002 | Update bio | Logged in | 1. Edit bio 2. Save | Bio updated in database | Pass |
| TC-PROF-003 | Upload profile picture | Logged in | 1. Select image 2. Upload | Picture saved and displayed | Pass |
| TC-PROF-004 | Invalid phone format | Logged in | 1. Enter invalid phone 2. Save | Validation error displayed | Pass |
| TC-PROF-005 | Toggle notifications | Logged in | 1. Change notification setting 2. Save | Preference updated | Pass |
| TC-PROF-006 | View analysis statistics | Logged in with history | 1. View profile | Statistics displayed correctly | Pass |

**Table 6.4: System Integration Test Cases**

| Test ID | Description | Preconditions | Steps | Expected Result | Status |
|---------|-------------|---------------|-------|-----------------|--------|
| TC-INT-001 | Complete registration flow | None | 1. Register 2. Verify email 3. Login | Full flow completes successfully | Pass |
| TC-INT-002 | Analysis to history flow | Logged in | 1. Perform analysis 2. View history | Analysis appears in history | Pass |
| TC-INT-003 | PDF report generation | Analysis exists | 1. View analysis 2. Generate PDF | Valid PDF downloaded | Pass |
| TC-INT-004 | Analytics data accuracy | Multiple analyses | 1. View analytics | Charts reflect actual data | Pass |
| TC-INT-005 | DermaGenie conversation | Logged in | 1. Send message 2. Receive response | AI response received | Pass |
| TC-INT-006 | Email notification delivery | New user | 1. Complete first analysis | Notification email received | Pass |
| TC-INT-007 | Admin dashboard access | Staff user | 1. Login as staff 2. Access admin | Dashboard displays correctly | Pass |
| TC-INT-008 | Non-staff admin access | Regular user | 1. Attempt admin access | Access denied | Pass |

---

<!-- PAGE BREAK -->

## CHAPTER 7: RESULTS AND DISCUSSION

### 7.1 Experimental Results


The experimental results of the SkinCare AI system demonstrate the effectiveness of the dual-model approach for skin lesion classification. This section presents the quantitative results obtained from model training and evaluation, as well as observations from system testing.

The EfficientNetB0 model training was conducted on the ISIC 2019 dataset comprising 25,331 dermoscopic images across eight classes. The training process utilized transfer learning from ImageNet pre-trained weights, with the base layers initially frozen and later fine-tuned. The model was trained for 50 epochs with early stopping based on validation loss.

The training history for EfficientNetB0 shows steady improvement in both training and validation accuracy over the first 30 epochs, followed by gradual convergence. The training accuracy reached approximately 78 percent, while the validation accuracy stabilized at approximately 72 percent. The gap between training and validation accuracy indicates some degree of overfitting, which was mitigated through dropout regularization and early stopping.

The final test accuracy for the EfficientNetB0 model was 71.32 percent on the held-out test set. This accuracy is consistent with results reported in the literature for similar models on the ISIC dataset, which is known to be challenging due to class imbalance and visual similarity between some conditions.

The custom CNN model training was conducted on the modified HAM10000 subset comprising 5,906 images. The model was trained from scratch for 100 epochs with learning rate reduction on plateau. The smaller dataset and simpler model architecture allowed for faster training iterations.


The training history for the custom CNN shows rapid initial improvement followed by gradual refinement. The training accuracy reached approximately 96 percent, while the validation accuracy reached approximately 94 percent. The smaller gap between training and validation accuracy suggests better generalization compared to the EfficientNetB0 model on its respective dataset.

The final test accuracy for the custom CNN model was 94.1 percent on the held-out test set. This higher accuracy compared to EfficientNetB0 reflects the smaller, more homogeneous dataset and the model architecture optimized for the specific image characteristics.

The intelligent model selection mechanism was evaluated by analyzing the distribution of model usage across a sample of test images. In automatic mode, the EfficientNetB0 model was used for approximately 65 percent of predictions where its confidence exceeded the threshold. The remaining 35 percent of predictions fell back to the custom CNN model.

The web application performance was evaluated through load testing and response time measurements. The average page load time was under 2 seconds for most pages. The image analysis process, including upload, preprocessing, and inference, completed in an average of 3.5 seconds. These response times provide acceptable user experience for the intended use case.

The email delivery success rate was measured at over 98 percent for OTP and notification emails. The small percentage of failures was attributed to invalid email addresses or temporary delivery issues. The Resend API provided reliable delivery with detailed logging for troubleshooting.

### 7.2 Performance Analysis


The performance analysis examines the computational efficiency and resource utilization of the SkinCare AI system. This analysis provides insights into system scalability and identifies potential optimization opportunities.

The model inference time was measured for both neural network models. The EfficientNetB0 model inference time averaged 850 milliseconds on CPU, with the majority of time spent on the forward pass through the network. The custom CNN model inference time averaged 120 milliseconds on CPU, reflecting its smaller architecture and lower input resolution.

The memory utilization analysis shows that the loaded models consume approximately 150 megabytes of RAM for EfficientNetB0 and 25 megabytes for the custom CNN. The total application memory footprint, including the Django framework and loaded models, is approximately 500 megabytes under normal operation.

The database query performance was analyzed using Django's query logging. Most queries complete in under 10 milliseconds. The history listing query, which retrieves multiple records with related data, averages 25 milliseconds. Index optimization on frequently queried fields ensures efficient data retrieval.

The file storage performance was evaluated for image upload and retrieval operations. Image uploads complete in under 1 second for typical file sizes. Image retrieval for display is optimized through browser caching and appropriate cache headers.

The concurrent user capacity was estimated through load testing. The system maintained acceptable response times with up to 50 concurrent users on modest hardware. Beyond this threshold, response times increased significantly, indicating the need for scaling strategies for higher traffic volumes.

### 7.3 Accuracy Analysis


The accuracy analysis provides a detailed examination of model performance across different conditions and scenarios. This analysis helps identify strengths and limitations of the classification system.

The per-class accuracy analysis for EfficientNetB0 reveals significant variation across conditions. Melanocytic Nevi, the most common class, achieved the highest accuracy at 82 percent. Melanoma achieved 68 percent accuracy, which is clinically significant given the importance of detecting this condition. Basal Cell Carcinoma achieved 71 percent accuracy. The less common classes showed lower accuracy, with Dermatofibroma at 45 percent and Vascular Lesions at 52 percent.

The per-class accuracy analysis for the custom CNN shows more uniform performance across classes. Melanocytic Nevi achieved 96 percent accuracy. Melanoma achieved 92 percent accuracy. The custom "not_skin_cancer" class achieved 89 percent accuracy, demonstrating the model's ability to distinguish skin lesions from non-lesion images.

The confusion matrix analysis reveals common misclassification patterns. Benign Keratosis-like Lesions are sometimes confused with Melanocytic Nevi, reflecting their visual similarity. Actinic Keratoses are occasionally misclassified as Squamous Cell Carcinoma, which is clinically relevant as Actinic Keratoses can progress to Squamous Cell Carcinoma.

The confidence score distribution analysis shows that higher confidence predictions tend to be more accurate. Predictions with confidence above 80 percent have accuracy exceeding 90 percent. Predictions with confidence below 50 percent have accuracy around 60 percent. This correlation validates the use of confidence thresholds in the model selection mechanism.

The impact of image quality on accuracy was assessed using images with varying characteristics. High-quality dermoscopic images achieved the best accuracy. Images with poor lighting, blur, or non-standard framing showed reduced accuracy. This finding emphasizes the importance of image quality guidance for users.

### 7.4 Comparison with Existing Systems


The comparison with existing systems contextualizes the performance and capabilities of SkinCare AI relative to other approaches in the field. This comparison considers both accuracy metrics and feature completeness.

The accuracy comparison with published research shows that SkinCare AI achieves competitive results. The EfficientNetB0 model's 71.32 percent accuracy on ISIC 2019 is comparable to results reported in recent literature, which typically range from 65 to 80 percent depending on the specific methodology and evaluation protocol. The custom CNN's 94.1 percent accuracy on the HAM10000 subset exceeds many reported results on similar datasets.

The comparison with commercial applications is limited by the proprietary nature of most commercial systems. However, published evaluations of consumer skin analysis applications have reported accuracy ranging from 55 to 85 percent, with significant variation based on image quality and condition type. SkinCare AI's dual-model approach provides robustness that may exceed single-model commercial applications.

The feature comparison highlights SkinCare AI's comprehensive functionality. Unlike many existing applications that provide only classification results, SkinCare AI includes analysis history tracking, PDF report generation, analytics dashboard, and AI chatbot assistance. This comprehensive feature set provides additional value beyond basic classification.

The responsible AI comparison examines how different systems handle the sensitive nature of medical predictions. SkinCare AI's emphasis on clear disclaimers, educational framing, and recommendations for professional consultation represents best practices that are not consistently implemented in existing applications.

**Table 7.3: Comparison with Related Works**

| System/Study | Dataset | Accuracy | Features | Disclaimers |
|--------------|---------|----------|----------|-------------|
| SkinCare AI (EfficientNetB0) | ISIC 2019 | 71.32% | Comprehensive | Yes |
| SkinCare AI (Custom CNN) | HAM10000 subset | 94.1% | Comprehensive | Yes |
| Esteva et al. (2017) | Custom | 72.1% | Classification only | Limited |
| Haenssle et al. (2018) | ISIC | 82.5% | Classification only | Yes |
| Commercial App A | Unknown | ~70% | Basic | Limited |
| Commercial App B | Unknown | ~65% | Basic | No |

---

<!-- PAGE BREAK -->

## CHAPTER 8: CONCLUSION AND FUTURE ENHANCEMENT

### 8.1 Conclusion


The SkinCare AI project has successfully achieved its primary objective of developing a comprehensive, accessible, and responsible AI-powered skin lesion classification system. The system demonstrates the potential of deep learning technologies to contribute to early skin cancer detection while maintaining appropriate boundaries regarding the role of AI in healthcare.

The dual-model architecture implemented in SkinCare AI represents a significant technical achievement. By combining the EfficientNetB0 model trained on the extensive ISIC 2019 dataset with a custom CNN model trained on the HAM10000 subset, the system provides robust classification across a wide range of image types and conditions. The intelligent model selection mechanism ensures that users receive the most reliable predictions possible, automatically adapting to variations in image quality and lesion characteristics.

The web application provides a user-friendly interface that makes advanced AI technology accessible to users without technical expertise. The comprehensive feature set, including user authentication, analysis history tracking, PDF report generation, analytics dashboard, and AI chatbot assistance, creates a complete skin health management platform that extends well beyond basic image classification.

The emphasis on responsible AI practices throughout the development process ensures that SkinCare AI serves as a complement to professional medical care rather than a replacement. Clear medical disclaimers, legally-compliant result presentation, and consistent recommendations for professional consultation help users understand the appropriate role of AI-based screening tools and encourage appropriate healthcare-seeking behavior.

The experimental results demonstrate that the system achieves competitive accuracy on standard benchmark datasets. The EfficientNetB0 model's 71.32 percent accuracy on ISIC 2019 and the custom CNN's 94.1 percent accuracy on the HAM10000 subset are consistent with or exceed results reported in the literature for similar approaches.


The project has demonstrated the feasibility of developing sophisticated medical AI applications using open-source technologies and publicly available datasets. The use of Django, TensorFlow, and other open-source tools enabled rapid development while ensuring that the resulting system follows best practices for security and maintainability.

The educational value of the project extends beyond the immediate functionality of the system. The development process provided valuable experience in integrating machine learning models with web applications, implementing secure authentication systems, and designing user interfaces for sensitive healthcare applications.

In conclusion, SkinCare AI represents a successful implementation of AI-powered skin lesion classification that balances technical sophistication with responsible deployment practices. The system provides a foundation for further development and demonstrates the potential for AI to contribute to improved skin health outcomes through accessible preliminary screening.

### 8.2 Future Enhancements

The SkinCare AI system provides a solid foundation that can be extended with additional features and capabilities. This section outlines potential future enhancements that could increase the system's value and impact.

The development of native mobile applications for iOS and Android platforms would significantly improve accessibility. Mobile applications could leverage device cameras for direct image capture, provide offline analysis capabilities through on-device model inference, and deliver push notifications for reminders and updates. The responsive web design of the current system provides a starting point for mobile development.


Model improvements could enhance classification accuracy and expand the range of detectable conditions. Training on larger and more diverse datasets could improve generalization. Ensemble methods combining multiple models could provide more robust predictions. Attention mechanisms could improve interpretability by highlighting the image regions that influenced the prediction.

Real-time analysis using webcam or smartphone camera feeds would enable continuous monitoring without the need to capture and upload individual images. This capability would require optimization of the inference pipeline for real-time performance and development of appropriate user interface elements for live analysis.

Telemedicine integration would enable direct connection between users and dermatologists for professional consultation. Integration with telemedicine platforms could allow users to share their analysis history and schedule virtual consultations. This enhancement would strengthen the bridge between preliminary screening and professional care.

Multi-language support would expand the accessibility of the system to non-English speaking users. Internationalization of the user interface, educational content, and AI chatbot responses would require translation and localization efforts. This enhancement would significantly increase the potential user base.

Advanced analytics features could provide deeper insights into skin health patterns. Predictive analytics could identify trends that may warrant attention. Comparative analysis across user populations could provide context for individual results. Integration with wearable devices could enable correlation with environmental and lifestyle factors.

API development would enable integration with third-party applications and services. A RESTful API could allow healthcare providers to integrate SkinCare AI analysis into their workflows. Developer documentation and authentication mechanisms would be required to support external integrations.

Research platform capabilities could enable the system to contribute to skin cancer research. With appropriate consent mechanisms, anonymized data could be shared with researchers. The platform could support clinical studies evaluating AI-assisted screening approaches.

---

<!-- PAGE BREAK -->

## CHAPTER 9: BIBLIOGRAPHY AND REFERENCES


1. Codella, N. C. F., Gutman, D., Celebi, M. E., Helba, B., Marchetti, M. A., Dusza, S. W., ... & Halpern, A. (2018). Skin lesion analysis toward melanoma detection: A challenge at the 2017 International Symposium on Biomedical Imaging (ISBI), hosted by the International Skin Imaging Collaboration (ISIC). In 2018 IEEE 15th International Symposium on Biomedical Imaging (ISBI 2018) (pp. 168-172). IEEE.

2. Esteva, A., Kuprel, B., Novoa, R. A., Ko, J., Swetter, S. M., Blau, H. M., & Thrun, S. (2017). Dermatologist-level classification of skin cancer with deep neural networks. Nature, 542(7639), 115-118.

3. Haenssle, H. A., Fink, C., Schneiderbauer, R., Tobber, F., Buhl, T., Blum, A., ... & Uhlmann, L. (2018). Man against machine: diagnostic performance of a deep learning convolutional neural network for dermoscopic melanoma recognition in comparison to 58 dermatologists. Annals of Oncology, 29(8), 1836-1842.

4. Tan, M., & Le, Q. (2019). EfficientNet: Rethinking model scaling for convolutional neural networks. In International Conference on Machine Learning (pp. 6105-6114). PMLR.

5. Tschandl, P., Rosendahl, C., & Kittler, H. (2018). The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions. Scientific Data, 5(1), 1-9.

6. World Health Organization. (2023). Skin cancers. Retrieved from https://www.who.int/news-room/fact-sheets/detail/skin-cancers

7. American Cancer Society. (2023). Cancer Facts & Figures 2023. Atlanta: American Cancer Society.

8. Skin Cancer Foundation. (2023). Skin Cancer Facts & Statistics. Retrieved from https://www.skincancer.org/skin-cancer-information/skin-cancer-facts/

9. Django Software Foundation. (2023). Django Documentation. Retrieved from https://docs.djangoproject.com/

10. TensorFlow. (2023). TensorFlow Documentation. Retrieved from https://www.tensorflow.org/


11. Keras. (2023). Keras Documentation. Retrieved from https://keras.io/

12. International Skin Imaging Collaboration. (2023). ISIC Archive. Retrieved from https://www.isic-archive.com/

13. Chollet, F. (2017). Deep Learning with Python. Manning Publications.

14. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.

15. LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521(7553), 436-444.

16. He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (pp. 770-778).

17. Simonyan, K., & Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556.

18. Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. Advances in Neural Information Processing Systems, 25.

19. Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., ... & Fei-Fei, L. (2015). ImageNet large scale visual recognition challenge. International Journal of Computer Vision, 115(3), 211-252.

20. Brinker, T. J., Hekler, A., Enk, A. H., Klode, J., Hauschild, A., Berking, C., ... & von Kalle, C. (2019). Deep learning outperformed 136 of 157 dermatologists in a head-to-head dermoscopic melanoma image classification task. European Journal of Cancer, 113, 47-54.

21. Marchetti, M. A., Codella, N. C., Dusza, S. W., Gutman, D. A., Helba, B., Kalber, A., ... & Halpern, A. C. (2018). Results of the 2016 International Skin Imaging Collaboration International Symposium on Biomedical Imaging challenge: Comparison of the accuracy of computer algorithms to dermatologists for the diagnosis of melanoma from dermoscopic images. Journal of the American Academy of Dermatology, 78(2), 270-277.

22. Resend. (2023). Resend Documentation. Retrieved from https://resend.com/docs

23. Chart.js. (2023). Chart.js Documentation. Retrieved from https://www.chartjs.org/docs/

24. Python Software Foundation. (2023). Python Documentation. Retrieved from https://docs.python.org/

25. NumPy. (2023). NumPy Documentation. Retrieved from https://numpy.org/doc/

---

<!-- PAGE BREAK -->

## CHAPTER 10: APPENDICES

### Appendix A: Output Screens


This appendix presents screenshots of the SkinCare AI user interface, demonstrating the visual design and functionality of the system.

**Figure A.1: Landing Page**

The landing page serves as the entry point to the SkinCare AI application. It features a floating video background that creates a premium, engaging first impression. The page includes a prominent call-to-action button directing users to begin their skin health journey. The navigation bar provides access to login and registration for new users.

**Figure A.2: User Registration Page**

The registration page provides a clean, intuitive form for new user account creation. The form includes fields for username, email address, password, and password confirmation. Validation messages appear inline to guide users in providing valid input. The dark theme with purple accents maintains visual consistency with the overall design.

**Figure A.3: Login Page**

The login page presents a simple form for user authentication. Users enter their username or email and password to access their account. A link to the password reset functionality is provided for users who have forgotten their credentials. The page includes a link to registration for users who do not yet have an account.

**Figure A.4: Home Dashboard**

The home dashboard provides an overview of the user's account and quick access to key features. Statistics cards display the total number of analyses performed and recent activity. Navigation cards provide access to the analysis page, history, analytics, and profile. The DermaGenie chatbot widget is accessible from this page.

**Figure A.5: Image Analysis Page**

The image analysis page is the core interface for skin lesion classification. The page features a drag-and-drop upload area with visual feedback during the upload process. Model selection options allow users to choose between automatic selection, EfficientNetB0, or CNN. A submit button initiates the analysis process.


**Figure A.6: Analysis Results Page**

The analysis results page presents the classification results in a clear, informative format. The uploaded image is displayed alongside the prediction results. The predicted condition is prominently shown with the confidence score displayed as a percentage and progress bar. Educational information about the detected condition is provided in an expandable section. Medical disclaimers are clearly displayed, emphasizing the preliminary nature of the assessment.

**Figure A.7: User Profile Page**

The user profile page displays the user's personal information and account statistics. The profile picture is displayed prominently, with an option to upload a new image. Editable fields allow users to update their biographical information, contact details, and notification preferences. Statistics show the total number of analyses and recent activity.

**Figure A.8: Analytics Dashboard**

The analytics dashboard presents visual representations of the user's analysis data. A pie chart shows the distribution of detected conditions across all analyses. A line graph displays analysis frequency over time. Summary statistics provide quick insights into the user's skin health monitoring activity. The charts are interactive, with tooltips providing additional information on hover.

**Figure A.9: Analysis History Page**

The analysis history page displays a list of all past analyses in a paginated format. Each entry shows a thumbnail of the analyzed image, the detected condition, confidence score, and timestamp. Filter and sort options allow users to refine the displayed results. Action buttons provide access to detailed views and comparison functionality.

**Figure A.10: DermaGenie Chat Interface**

The DermaGenie chat interface provides a conversational experience for skin health queries. The chat history displays previous messages with clear visual distinction between user messages and AI responses. The input field at the bottom allows users to type new messages. A disclaimer reminds users that responses are for educational purposes only.

---

<!-- PAGE BREAK -->

### Appendix B: Sample Code Snippets


This appendix presents sample code snippets that illustrate key implementation details of the SkinCare AI system.

**Code Snippet B.1: Model Loading and Prediction**

```python
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load models at application startup
efficientnet_model = load_model('models/EfficientNetB0_skin-cancer.h5')
cnn_model = load_model('models/den_skin-cancer.h5')

# Class labels
CLASS_LABELS = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc', 'not_skin_cancer']

def preprocess_image_efficientnet(img_path):
    """Preprocess image for EfficientNetB0 model."""
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)
    return img_array

def preprocess_image_cnn(img_path):
    """Preprocess image for custom CNN model."""
    img = image.load_img(img_path, target_size=(48, 48))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

def predict(img_path, model_preference='auto'):
    """Generate prediction using selected model."""
    if model_preference == 'efficientnet':
        img_array = preprocess_image_efficientnet(img_path)
        predictions = efficientnet_model.predict(img_array)
        model_used = 'EfficientNetB0'
    elif model_preference == 'cnn':
        img_array = preprocess_image_cnn(img_path)
        predictions = cnn_model.predict(img_array)
        model_used = 'Custom CNN'
    else:  # Auto mode
        img_array = preprocess_image_efficientnet(img_path)
        predictions = efficientnet_model.predict(img_array)
        confidence = np.max(predictions)
        if confidence < 0.5:
            img_array = preprocess_image_cnn(img_path)
            predictions = cnn_model.predict(img_array)
            model_used = 'Custom CNN'
        else:
            model_used = 'EfficientNetB0'
    
    predicted_class = np.argmax(predictions[0])
    confidence = float(np.max(predictions))
    label = CLASS_LABELS[predicted_class]
    
    return label, confidence, model_used
```


**Code Snippet B.2: User Registration View**

```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile, EmailOTP
from .otp_utils import generate_otp, send_otp_email

def Register_2(request):
    """Handle user registration."""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, '2_Register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, '2_Register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, '2_Register.html')
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_active = False  # Require email verification
        user.save()
        
        # Create profile
        UserProfile.objects.create(user=user)
        
        # Generate and send OTP
        otp = generate_otp()
        EmailOTP.objects.create(user=user, otp=otp)
        send_otp_email(email, otp)
        
        request.session['pending_user_id'] = user.id
        return redirect('verify_email')
    
    return render(request, '2_Register.html')
```


**Code Snippet B.3: OTP Generation and Verification**

```python
import random
import string
from datetime import timedelta
from django.utils import timezone
from .email_utils import send_email

def generate_otp(length=6):
    """Generate a random numeric OTP."""
    return ''.join(random.choices(string.digits, k=length))

def send_otp_email(email, otp):
    """Send OTP to user's email address."""
    subject = 'SkinCare AI - Email Verification'
    message = f'''
    Your verification code is: {otp}
    
    This code will expire in 10 minutes.
    
    If you did not request this code, please ignore this email.
    '''
    send_email(email, subject, message)

def verify_otp(user, submitted_otp):
    """Verify the submitted OTP."""
    try:
        otp_record = EmailOTP.objects.filter(
            user=user,
            is_verified=False
        ).latest('created_at')
        
        # Check expiration (10 minutes)
        expiration_time = otp_record.created_at + timedelta(minutes=10)
        if timezone.now() > expiration_time:
            return False, 'OTP has expired. Please request a new one.'
        
        # Check OTP match
        if otp_record.otp == submitted_otp:
            otp_record.is_verified = True
            otp_record.save()
            return True, 'Email verified successfully.'
        else:
            return False, 'Invalid OTP. Please try again.'
    
    except EmailOTP.DoesNotExist:
        return False, 'No OTP found. Please request a new one.'
```

**Code Snippet B.4: Email Notification Utility**

```python
import resend
from django.conf import settings

resend.api_key = settings.RESEND_API_KEY

def send_email(to_email, subject, html_content):
    """Send email using Resend API."""
    try:
        params = {
            'from': settings.DEFAULT_FROM_EMAIL,
            'to': [to_email],
            'subject': subject,
            'html': html_content
        }
        response = resend.Emails.send(params)
        return True, response
    except Exception as e:
        return False, str(e)

def send_welcome_email(user):
    """Send welcome email to new user."""
    subject = 'Welcome to SkinCare AI'
    html_content = f'''
    <h2>Welcome to SkinCare AI, {user.username}!</h2>
    <p>Thank you for joining our platform.</p>
    <p>You can now:</p>
    <ul>
        <li>Upload skin images for AI-powered analysis</li>
        <li>Track your analysis history</li>
        <li>Chat with DermaGenie for skin health guidance</li>
    </ul>
    <p>Remember: Our analysis is for educational purposes only.</p>
    '''
    return send_email(user.email, subject, html_content)
```


**Code Snippet B.5: Django Model Definitions**

```python
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Extended user profile information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )
    email_verified = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)
    first_analysis_email_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

class UserPredictModel(models.Model):
    """Skin lesion analysis record."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='predictions/')
    label = models.CharField(max_length=100)
    model_preference = models.CharField(max_length=20, default='auto')
    model_used = models.CharField(max_length=50, blank=True, null=True)
    confidence_score = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.label} - {self.created_at}'
    
    class Meta:
        ordering = ['-created_at']

class EmailOTP(models.Model):
    """Email verification OTP."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} - OTP'
```

---

<!-- PAGE BREAK -->

### Appendix C: User Manual


This appendix provides a user manual for the SkinCare AI system, guiding users through the key features and functionality.

**Getting Started**

To begin using SkinCare AI, navigate to the application URL in your web browser. The landing page provides an overview of the system and options to register or log in.

**Creating an Account**

1. Click the "Register" button on the landing page or navigation bar.
2. Enter your desired username (3-30 characters).
3. Enter your email address.
4. Create a password (minimum 8 characters).
5. Confirm your password by entering it again.
6. Click "Register" to submit the form.
7. Check your email for a verification code.
8. Enter the 6-digit code on the verification page.
9. Your account is now active and you can log in.

**Logging In**

1. Click the "Login" button on the landing page or navigation bar.
2. Enter your username or email address.
3. Enter your password.
4. Click "Login" to access your account.

**Performing a Skin Analysis**

1. Log in to your account.
2. Navigate to the "Analyze" page using the navigation bar.
3. Upload an image by clicking the upload area or dragging and dropping an image file.
4. Select your preferred model: Auto (recommended), EfficientNetB0, or CNN.
5. Click "Analyze" to submit the image.
6. Wait for the analysis to complete (typically 3-5 seconds).
7. Review the results, including the predicted condition and confidence score.
8. Read the educational information about the detected condition.
9. Note the medical disclaimer and recommendations.


**Viewing Analysis History**

1. Navigate to the "History" page using the navigation bar.
2. Browse your past analyses in the list view.
3. Use the filter options to narrow results by condition or date.
4. Use the sort options to order results by date or confidence.
5. Click on an analysis to view detailed results.

**Generating PDF Reports**

1. Navigate to a specific analysis result.
2. Click the "Generate PDF" button.
3. The PDF report will be downloaded to your device.
4. Share the report with your healthcare provider as needed.

**Using the Analytics Dashboard**

1. Navigate to the "Analytics" page using the navigation bar.
2. View the pie chart showing distribution of detected conditions.
3. View the line graph showing analysis frequency over time.
4. Hover over chart elements for detailed information.
5. Use the insights to understand your skin health patterns.

**Managing Your Profile**

1. Navigate to the "Profile" page using the navigation bar.
2. View your current profile information and statistics.
3. Click "Edit Profile" to update your information.
4. Upload a new profile picture if desired.
5. Update your notification preferences.
6. Click "Save" to apply changes.

**Using DermaGenie AI Assistant**

1. Click the DermaGenie icon or navigate to the chat page.
2. Type your question about skin health in the input field.
3. Press Enter or click Send to submit your question.
4. Read the AI-generated response.
5. Continue the conversation with follow-up questions.
6. Remember that responses are for educational purposes only.

**Resetting Your Password**

1. Click "Forgot Password" on the login page.
2. Enter your registered email address.
3. Check your email for a verification code.
4. Enter the code on the verification page.
5. Create a new password.
6. Log in with your new password.

**Important Reminders**

- SkinCare AI provides preliminary assessments for educational purposes only.
- Results should not be used as a substitute for professional medical evaluation.
- Always consult a qualified dermatologist for proper diagnosis and treatment.
- Higher confidence scores generally indicate more reliable predictions.
- Image quality affects analysis accuracy; use well-lit, focused images.

---

**END OF PROJECT REPORT**

---

*Document prepared for academic submission*
*SkinCare AI - AI-Powered Skin Lesion Classification System*
*Academic Year 2024-2025*
