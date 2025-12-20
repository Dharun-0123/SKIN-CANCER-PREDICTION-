# SkinCare AI - Model Information

## Primary Model: EfficientNetB0 (EfficientNetB0_skin-cancer.h5)
- **Architecture**: EfficientNetB0 with transfer learning
- **Training Data**: 25,331 images from ISIC 2019 dataset
- **Input Size**: 224x224x3 pixels
- **Classes**: 8 skin conditions
- **Test Accuracy**: 71.32%
- **Status**: Primary model (preferred for predictions)

### Class Distribution:
1. **AK** - Actinic Keratoses (867 images)
2. **BCC** - Basal Cell Carcinoma (3,323 images)  
3. **BKL** - Benign Keratosis-like Lesions (2,624 images)
4. **DF** - Dermatofibroma (239 images)
5. **MEL** - Melanoma (4,522 images)
6. **NV** - Melanocytic Nevi (12,875 images)
7. **SCC** - Squamous Cell Carcinoma (628 images)
8. **VASC** - Vascular Lesions (253 images)

## Secondary Model: CNN (CNN_skin-cancer.h5)
- **Architecture**: Custom CNN
- **Training Data**: 3,297 images
- **Input Size**: 48x48x3 pixels
- **Classes**: 7 skin conditions + not_skin_cancer
- **Test Accuracy**: 94.1%
- **Status**: Fallback model (used when primary model fails or has low confidence)

### Class Distribution:
1. Actinic keratoses
2. Basal cell carcinoma
3. Benign keratosis like lesions
4. Dermatofibroma
5. Melanoma
6. Melanocytic nevi
7. Vascular lesions
8. Not skin cancer

## Model Selection Logic:
1. **Primary**: Try EfficientNetB0 model first
2. **Confidence Check**: If confidence > 0.5, use primary result
3. **Fallback**: If primary fails or low confidence, use CNN model
4. **Logging**: All predictions logged with model used and confidence scores

## Performance Comparison:
- **EfficientNetB0**: More robust, larger dataset, modern architecture
- **CNN**: Higher accuracy on smaller dataset, faster inference
- **Recommendation**: EfficientNetB0 for production, CNN as reliable backup