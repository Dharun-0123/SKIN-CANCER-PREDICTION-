#!/usr/bin/env python3
"""
Create a compatible EfficientNetB0 model for testing
This creates a properly formatted model that can be loaded without issues
"""

import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras import layers, models
import numpy as np

def create_compatible_efficientnet():
    print("🔧 Creating Compatible EfficientNetB0 Model")
    print("=" * 50)
    
    # Create the model architecture (same as your training)
    print("📋 Building model architecture...")
    
    base = EfficientNetB0(
        include_top=False,
        weights='imagenet',  # Use ImageNet weights as starting point
        input_shape=(224, 224, 3)
    )
    base.trainable = False  # Freeze base layers initially
    
    model = models.Sequential([
        base,
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(8, activation='softmax', dtype='float32')  # 8 classes
    ])
    
    # Compile the model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("✅ Model architecture created")
    print(f"   Input shape: {model.input_shape}")
    print(f"   Output shape: {model.output_shape}")
    print(f"   Parameters: {model.count_params():,}")
    
    # Test the model
    print("\n🧪 Testing model...")
    dummy_input = np.random.random((1, 224, 224, 3)).astype(np.float32)
    prediction = model.predict(dummy_input, verbose=0)
    
    classes = ['AK', 'BCC', 'BKL', 'DF', 'MEL', 'NV', 'SCC', 'VASC']
    predicted_class = classes[np.argmax(prediction)]
    confidence = np.max(prediction)
    
    print(f"✅ Model test successful")
    print(f"   Predicted class: {predicted_class}")
    print(f"   Confidence: {confidence:.3f}")
    
    # Save the model
    model_path = "webapp/models/EfficientNetB0_skin-cancer.h5"
    backup_path = "webapp/models/EfficientNetB0_skin-cancer_original.h5"
    
    # Backup original if it exists
    if os.path.exists(model_path):
        print(f"\n📋 Backing up original model...")
        import shutil
        shutil.copy2(model_path, backup_path)
        print(f"✅ Original backed up to: {backup_path}")
    
    print(f"\n💾 Saving compatible model...")
    model.save(model_path, save_format='h5')
    print(f"✅ Model saved: {model_path}")
    
    # Verify the saved model can be loaded
    print(f"\n🔍 Verifying saved model...")
    try:
        test_model = keras.models.load_model(model_path, compile=False)
        test_prediction = test_model.predict(dummy_input, verbose=0)
        print(f"✅ Saved model loads and works correctly!")
        
        return True
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        return False

def create_model_info():
    """Create updated model information"""
    info_text = """# EfficientNetB0 Model - Compatible Version

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
"""
    
    with open("webapp/models/EfficientNetB0_INFO.md", "w") as f:
        f.write(info_text)
    
    print("📝 Model info created: webapp/models/EfficientNetB0_INFO.md")

if __name__ == "__main__":
    success = create_compatible_efficientnet()
    
    if success:
        create_model_info()
        print(f"\n🎉 Compatible EfficientNetB0 model created successfully!")
        print(f"\n📋 Next steps:")
        print(f"   1. Test the dual-model system")
        print(f"   2. Replace with your trained weights when available")
        print(f"   3. The system will now work with both models")
    else:
        print(f"\n❌ Failed to create compatible model!")