#!/usr/bin/env python3
"""
Setup script for dual-model system in SkinCare AI
This script helps you integrate the new EfficientNetB0 model with the existing system.
"""

import os
import shutil
from pathlib import Path

def setup_dual_models():
    print("🔧 Setting up Dual-Model System for SkinCare AI")
    print("=" * 60)
    
    models_dir = Path("webapp/models")
    
    # Check existing models
    print("\n📁 Current Models:")
    existing_models = []
    for model_file in models_dir.glob("*.h5"):
        size_mb = model_file.stat().st_size / (1024 * 1024)
        print(f"   ✅ {model_file.name} ({size_mb:.1f} MB)")
        existing_models.append(model_file.name)
    
    # Check for new EfficientNetB0 model
    efficientnet_model = models_dir / "EfficientNetB0_skin-cancer.h5"
    
    if not efficientnet_model.exists():
        print(f"\n⚠️  Primary model not found: {efficientnet_model}")
        print("\n📋 To complete the setup:")
        print("   1. Train your EfficientNetB0 model using the notebook")
        print("   2. Save the model as 'EfficientNetB0_skin-cancer.h5'")
        print("   3. Copy it to: webapp/models/EfficientNetB0_skin-cancer.h5")
        print("\n💡 Example code to save your trained model:")
        print("   ```python")
        print("   # In your Kaggle notebook, after training:")
        print("   model.save('/kaggle/working/EfficientNetB0_skin-cancer.h5')")
        print("   ```")
        
        # Create a placeholder file with instructions
        placeholder_content = """
# EfficientNetB0 Model Placeholder
# 
# This file is a placeholder for the EfficientNetB0 model.
# 
# To add your trained model:
# 1. Train the EfficientNetB0 model using the provided notebook
# 2. Save it as 'EfficientNetB0_skin-cancer.h5'
# 3. Replace this file with your trained model
# 
# Expected specifications:
# - Input size: 224x224x3
# - Output classes: 8 (AK, BCC, BKL, DF, MEL, NV, SCC, VASC)
# - Architecture: EfficientNetB0 + GlobalAveragePooling + Dense layers
# - Training data: 25,331 images from ISIC 2019
"""
        
        with open(efficientnet_model.with_suffix('.txt'), 'w') as f:
            f.write(placeholder_content)
        
        print(f"\n📝 Created placeholder instructions: {efficientnet_model.with_suffix('.txt')}")
    else:
        size_mb = efficientnet_model.stat().st_size / (1024 * 1024)
        print(f"\n✅ Primary model found: EfficientNetB0_skin-cancer.h5 ({size_mb:.1f} MB)")
    
    # Model configuration summary
    print(f"\n🎯 Dual-Model Configuration:")
    print(f"   Primary Model: EfficientNetB0 (25,331 images, 71.32% accuracy)")
    print(f"   Secondary Model: CNN (3,297 images, 94.1% accuracy)")
    print(f"   Selection Logic: Primary first, fallback to secondary if needed")
    
    # Test the updated views.py
    print(f"\n🧪 Testing Model Loading Logic...")
    try:
        # Import Django settings
        import sys
        sys.path.append('webapp')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT.settings')
        
        import django
        django.setup()
        
        from django.conf import settings
        
        primary_path = os.path.join(settings.BASE_DIR, "models", "EfficientNetB0_skin-cancer.h5")
        secondary_path = os.path.join(settings.BASE_DIR, "models", "CNN_skin-cancer.h5")
        
        print(f"   Primary model path: {primary_path}")
        print(f"   Primary exists: {os.path.exists(primary_path)}")
        print(f"   Secondary model path: {secondary_path}")
        print(f"   Secondary exists: {os.path.exists(secondary_path)}")
        
        if os.path.exists(secondary_path):
            print("   ✅ Secondary model ready")
        else:
            print("   ❌ Secondary model missing")
            
        if os.path.exists(primary_path):
            print("   ✅ Primary model ready")
        else:
            print("   ⚠️  Primary model not found - will use secondary model")
            
    except Exception as e:
        print(f"   ⚠️  Could not test Django setup: {e}")
    
    print(f"\n🚀 Next Steps:")
    if not efficientnet_model.exists():
        print("   1. Complete EfficientNetB0 model training")
        print("   2. Copy trained model to webapp/models/")
        print("   3. Test the application")
    else:
        print("   1. Test the application with both models")
        print("   2. Monitor prediction logs for model usage")
        print("   3. Adjust confidence threshold if needed")
    
    print(f"\n📊 Model Comparison:")
    print(f"   EfficientNetB0: Better generalization, modern architecture")
    print(f"   CNN: Higher accuracy on training data, faster inference")
    print(f"   Combined: Best of both worlds with intelligent fallback")
    
    print(f"\n✅ Dual-model setup complete!")
    return True

def create_model_test_script():
    """Create a test script for the dual-model system"""
    
    test_script = """#!/usr/bin/env python3
import os
import sys
import django

# Setup Django
sys.path.append('webapp')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT.settings')
django.setup()

from tensorflow import keras
from django.conf import settings
import numpy as np

def test_models():
    print("🧪 Testing Dual-Model System")
    print("=" * 40)
    
    # Test primary model
    primary_path = os.path.join(settings.BASE_DIR, "models", "EfficientNetB0_skin-cancer.h5")
    secondary_path = os.path.join(settings.BASE_DIR, "models", "CNN_skin-cancer.h5")
    
    print(f"\\n🔍 Primary Model Test:")
    if os.path.exists(primary_path):
        try:
            model = keras.models.load_model(primary_path, compile=False)
            print(f"   ✅ Loaded successfully")
            print(f"   Input shape: {model.input_shape}")
            print(f"   Output shape: {model.output_shape}")
            print(f"   Parameters: {model.count_params():,}")
        except Exception as e:
            print(f"   ❌ Failed to load: {e}")
    else:
        print(f"   ⚠️  File not found: {primary_path}")
    
    print(f"\\n🔍 Secondary Model Test:")
    if os.path.exists(secondary_path):
        try:
            model = keras.models.load_model(secondary_path, compile=False)
            print(f"   ✅ Loaded successfully")
            print(f"   Input shape: {model.input_shape}")
            print(f"   Output shape: {model.output_shape}")
            print(f"   Parameters: {model.count_params():,}")
        except Exception as e:
            print(f"   ❌ Failed to load: {e}")
    else:
        print(f"   ❌ File not found: {secondary_path}")
    
    print(f"\\n✅ Model testing complete!")

if __name__ == "__main__":
    test_models()
"""
    
    with open("test_dual_models.py", "w") as f:
        f.write(test_script)
    
    print(f"📝 Created model test script: test_dual_models.py")

if __name__ == "__main__":
    setup_dual_models()
    create_model_test_script()
    
    print(f"\n🎉 Setup Complete!")
    print(f"Run 'python test_dual_models.py' to test your models")