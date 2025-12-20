#!/usr/bin/env python3
"""
Fix EfficientNetB0 model compatibility issues
This script attempts to load and re-save the model to fix compatibility problems
"""

import os
import sys
import tensorflow as tf
from tensorflow import keras
import numpy as np

def fix_efficientnet_model():
    print("🔧 Fixing EfficientNetB0 Model Compatibility")
    print("=" * 50)
    
    model_path = "webapp/models/EfficientNetB0_skin-cancer.h5"
    backup_path = "webapp/models/EfficientNetB0_skin-cancer_backup.h5"
    fixed_path = "webapp/models/EfficientNetB0_skin-cancer_fixed.h5"
    
    if not os.path.exists(model_path):
        print(f"❌ Model not found: {model_path}")
        return False
    
    # Create backup
    print(f"📋 Creating backup...")
    import shutil
    shutil.copy2(model_path, backup_path)
    print(f"✅ Backup created: {backup_path}")
    
    # Try different loading methods
    print(f"\n🔍 Attempting to load model...")
    
    model = None
    
    # Method 1: Standard load
    try:
        print("   Method 1: Standard load...")
        model = keras.models.load_model(model_path, compile=False)
        print("   ✅ Standard load successful!")
    except Exception as e:
        print(f"   ❌ Standard load failed: {e}")
    
    # Method 2: With custom objects
    if model is None:
        try:
            print("   Method 2: Custom objects...")
            custom_objects = {
                'Cast': tf.cast,
                'FixedDropout': keras.layers.Dropout,
            }
            model = keras.models.load_model(model_path, compile=False, custom_objects=custom_objects)
            print("   ✅ Custom objects load successful!")
        except Exception as e:
            print(f"   ❌ Custom objects load failed: {e}")
    
    # Method 3: Load weights only
    if model is None:
        try:
            print("   Method 3: Recreate architecture and load weights...")
            # Create a new EfficientNetB0 model
            from tensorflow.keras.applications import EfficientNetB0
            from tensorflow.keras import layers, models
            
            base = EfficientNetB0(
                include_top=False,
                weights=None,  # Don't load ImageNet weights
                input_shape=(224, 224, 3)
            )
            
            model = models.Sequential([
                base,
                layers.GlobalAveragePooling2D(),
                layers.Dense(256, activation='relu'),
                layers.Dropout(0.3),
                layers.Dense(8, activation='softmax', dtype='float32')
            ])
            
            # Try to load weights
            try:
                model.load_weights(model_path)
                print("   ✅ Architecture recreation + weights load successful!")
            except:
                print("   ❌ Could not load weights into new architecture")
                model = None
                
        except Exception as e:
            print(f"   ❌ Architecture recreation failed: {e}")
    
    if model is None:
        print("\n❌ All loading methods failed!")
        print("\n💡 Suggestions:")
        print("   1. Re-export the model from Kaggle with:")
        print("      model.save('model.h5', save_format='h5')")
        print("   2. Or use SavedModel format:")
        print("      model.save('model_dir')")
        print("   3. Check TensorFlow version compatibility")
        return False
    
    # Model loaded successfully, now test and re-save
    print(f"\n✅ Model loaded successfully!")
    print(f"   Input shape: {model.input_shape}")
    print(f"   Output shape: {model.output_shape}")
    print(f"   Parameters: {model.count_params():,}")
    
    # Test with dummy data
    print(f"\n🧪 Testing model with dummy data...")
    try:
        dummy_input = np.random.random((1, 224, 224, 3)).astype(np.float32)
        prediction = model.predict(dummy_input, verbose=0)
        print(f"   ✅ Prediction successful! Output shape: {prediction.shape}")
        print(f"   Sample prediction: {prediction[0][:3]}...")
    except Exception as e:
        print(f"   ❌ Prediction test failed: {e}")
        return False
    
    # Re-save the model
    print(f"\n💾 Re-saving model for compatibility...")
    try:
        model.save(fixed_path, save_format='h5')
        print(f"   ✅ Fixed model saved: {fixed_path}")
        
        # Test loading the fixed model
        print(f"\n🔍 Testing fixed model...")
        test_model = keras.models.load_model(fixed_path, compile=False)
        test_prediction = test_model.predict(dummy_input, verbose=0)
        print(f"   ✅ Fixed model loads and works correctly!")
        
        # Replace original with fixed version
        print(f"\n🔄 Replacing original model...")
        shutil.copy2(fixed_path, model_path)
        print(f"   ✅ Original model replaced with fixed version")
        
        # Clean up
        os.remove(fixed_path)
        print(f"   🧹 Temporary files cleaned up")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Re-saving failed: {e}")
        return False

def test_fixed_model():
    """Test the fixed model"""
    print(f"\n🧪 Final Test of Fixed Model")
    print("=" * 30)
    
    model_path = "webapp/models/EfficientNetB0_skin-cancer.h5"
    
    try:
        model = keras.models.load_model(model_path, compile=False)
        print(f"✅ Model loads successfully")
        
        # Test prediction
        dummy_input = np.random.random((1, 224, 224, 3)).astype(np.float32)
        prediction = model.predict(dummy_input, verbose=0)
        
        classes = ['AK', 'BCC', 'BKL', 'DF', 'MEL', 'NV', 'SCC', 'VASC']
        predicted_class = classes[np.argmax(prediction)]
        confidence = np.max(prediction)
        
        print(f"✅ Prediction successful")
        print(f"   Predicted class: {predicted_class}")
        print(f"   Confidence: {confidence:.3f}")
        print(f"   All probabilities: {prediction[0]}")
        
        return True
        
    except Exception as e:
        print(f"❌ Final test failed: {e}")
        return False

if __name__ == "__main__":
    success = fix_efficientnet_model()
    
    if success:
        print(f"\n🎉 Model fix completed successfully!")
        test_fixed_model()
    else:
        print(f"\n❌ Model fix failed!")
        print(f"\n📋 Next steps:")
        print(f"   1. Check the original model file")
        print(f"   2. Re-export from Kaggle with proper format")
        print(f"   3. Ensure TensorFlow version compatibility")