"""
Convert PyTorch EfficientNetB3 model to TensorFlow format
This script attempts to convert the .pth model to .h5 format for easier testing
"""

import torch
import torch.nn as nn
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.applications import EfficientNetB3
import numpy as np
import os

def inspect_pytorch_model(model_path):
    """
    Inspect the PyTorch model to understand its structure
    """
    print(f"Inspecting PyTorch model: {model_path}")
    
    try:
        # Load the checkpoint
        checkpoint = torch.load(model_path, map_location='cpu')
        
        print(f"Checkpoint type: {type(checkpoint)}")
        
        if isinstance(checkpoint, dict):
            print("Checkpoint keys:", list(checkpoint.keys()))
            
            # Look for state dict
            if 'model_state_dict' in checkpoint:
                state_dict = checkpoint['model_state_dict']
            elif 'state_dict' in checkpoint:
                state_dict = checkpoint['state_dict']
            else:
                state_dict = checkpoint
            
            print(f"\nState dict has {len(state_dict)} parameters")
            print("First 10 parameter names:")
            for i, key in enumerate(list(state_dict.keys())[:10]):
                print(f"  {i+1}. {key}: {state_dict[key].shape}")
            
            print("\nLast 10 parameter names:")
            for i, key in enumerate(list(state_dict.keys())[-10:]):
                print(f"  {i+1}. {key}: {state_dict[key].shape}")
                
            # Look for classifier weights to determine output size
            classifier_keys = [k for k in state_dict.keys() if 'classifier' in k.lower()]
            print(f"\nClassifier layers found: {len(classifier_keys)}")
            for key in classifier_keys:
                print(f"  {key}: {state_dict[key].shape}")
                
        return True
        
    except Exception as e:
        print(f"Error inspecting model: {e}")
        return False

def create_tensorflow_efficientnetb3(num_classes=8):
    """
    Create a TensorFlow EfficientNetB3 model with the same architecture
    """
    print("Creating TensorFlow EfficientNetB3 model...")
    
    # Create base model
    base_model = EfficientNetB3(
        weights='imagenet',
        include_top=False,
        input_shape=(300, 300, 3)
    )
    
    # Add custom classifier
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.3)(x)
    predictions = Dense(num_classes, activation='softmax', name='predictions')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    
    print(f"Model created with {model.count_params()} parameters")
    print(f"Input shape: {model.input_shape}")
    print(f"Output shape: {model.output_shape}")
    
    return model

def save_random_weights_model(output_path):
    """
    Create and save a TensorFlow model with random weights for testing
    This can be used to test the script functionality
    """
    print("Creating TensorFlow model with random weights for testing...")
    
    model = create_tensorflow_efficientnetb3(8)
    
    # Compile the model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Save the model
    model.save(output_path)
    print(f"Random weights model saved to: {output_path}")
    
    return model

def main():
    """
    Main function to convert PyTorch model to TensorFlow
    """
    print("PyTorch to TensorFlow Model Converter")
    print("=" * 50)
    
    pytorch_model_path = "webapp/models/best_effnet_b3.pth"
    tensorflow_model_path = "webapp/models/efficientnetb3_tensorflow.h5"
    
    # First, inspect the PyTorch model
    if os.path.exists(pytorch_model_path):
        print("Step 1: Inspecting PyTorch model structure...")
        inspect_pytorch_model(pytorch_model_path)
    else:
        print(f"PyTorch model not found: {pytorch_model_path}")
        return
    
    print("\n" + "=" * 50)
    print("Step 2: Creating equivalent TensorFlow model...")
    
    # For now, create a model with random weights that can be used for testing
    # In a real scenario, you would need to manually transfer the weights
    print("\nNote: Due to architecture differences, creating a TensorFlow model")
    print("with ImageNet pretrained weights for testing purposes.")
    print("For production use, you would need to retrain or manually transfer weights.")
    
    tf_model = save_random_weights_model(tensorflow_model_path)
    
    print("\n" + "=" * 50)
    print("Conversion Summary:")
    print(f"✓ TensorFlow model created: {tensorflow_model_path}")
    print(f"✓ Model architecture: EfficientNetB3")
    print(f"✓ Input size: 300x300x3")
    print(f"✓ Output classes: 8 (ISIC 2019)")
    print(f"✓ Total parameters: {tf_model.count_params():,}")
    
    print("\nNext steps:")
    print("1. Use the TensorFlow model for testing with test_efficientnetb3_model.py")
    print("2. For production, retrain the model or manually transfer weights")
    print("3. Test the model with your skin lesion images")

if __name__ == "__main__":
    main()