# EfficientNetB0 Model - Compatible Version

## Model Details
- **Architecture**: EfficientNetB0 + Dense layers
- **Input Size**: 224×224×3
- **Output Classes**: 8 skin conditions
- **Base Weights**: ImageNet pre-trained
- **Status**: Compatible placeholder model

## Note
This is a compatible model structure with ImageNet weights.
To get the trained weights from your Kaggle model:

1. In Kaggle, save with explicit format:
   ```python
   model.save('model.h5', save_format='h5', save_traces=False)
   ```

2. Or use SavedModel format:
   ```python
   model.save('model_savedmodel')
   ```

3. Or export weights only:
   ```python
   model.save_weights('model_weights.h5')
   ```

## Classes
1. AK - Actinic Keratoses
2. BCC - Basal Cell Carcinoma  
3. BKL - Benign Keratosis-like Lesions
4. DF - Dermatofibroma
5. MEL - Melanoma
6. NV - Melanocytic Nevi
7. SCC - Squamous Cell Carcinoma
8. VASC - Vascular Lesions
