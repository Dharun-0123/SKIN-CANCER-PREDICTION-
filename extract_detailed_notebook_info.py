#!/usr/bin/env python3
"""
Extract detailed information from the skin.ipynb notebook
"""

import json
import re

def extract_detailed_info():
    """Extract detailed information from the notebook"""
    
    with open('training/skin.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook['cells']
    
    print("=" * 80)
    print("DETAILED SKIN CANCER DETECTION NOTEBOOK SUMMARY")
    print("=" * 80)
    
    # Extract dataset information
    extract_dataset_info(cells)
    
    # Extract model architectures
    extract_model_architectures(cells)
    
    # Extract training details
    extract_training_details(cells)
    
    # Extract results and performance
    extract_results(cells)
    
    # Extract file paths and model saving
    extract_model_paths(cells)

def extract_dataset_info(cells):
    """Extract dataset information"""
    print("\n1. DATASET INFORMATION:")
    print("-" * 50)
    
    # Find dataset structure cell
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if 'for folder in os.listdir(train)' in source:
                print("Dataset classes and image counts:")
                # Look for outputs
                if 'outputs' in cell and cell['outputs']:
                    for output in cell['outputs']:
                        if 'text' in output:
                            lines = output['text']
                            for line in lines:
                                if 'Folder:' in line or 'Number of Images:' in line:
                                    print(f"  {line.strip()}")
                break
    
    # Extract data path
    for cell in cells:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if 'train = Path(' in source:
                path_match = re.search(r"train = Path\(r?['\"]([^'\"]+)['\"]", source)
                if path_match:
                    print(f"\nDataset path: {path_match.group(1)}")
                break

def extract_model_architectures(cells):
    """Extract detailed model architectures"""
    print("\n2. MODEL ARCHITECTURES:")
    print("-" * 50)
    
    models = []
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # CNN Model
            if 'layers.Conv2D(28' in source and 'input_shape=(48, 48, 3)' in source:
                print(f"\nModel 1 - Basic CNN (Cell {i}):")
                print("  Architecture:")
                lines = source.split('\n')
                for line in lines:
                    if 'layers.' in line and ('Conv2D' in line or 'MaxPooling2D' in line or 'Flatten' in line or 'Dense' in line):
                        layer = line.strip().replace('layers.', '  - ')
                        print(layer)
                models.append('CNN')
            
            # VGG16 Model
            elif 'VGG16' in source and 'base_model' in source:
                print(f"\nModel 2 - VGG16 Transfer Learning (Cell {i}):")
                print("  Base: VGG16 (pre-trained)")
                lines = source.split('\n')
                for line in lines:
                    if 'VGG16' in line:
                        print(f"  - {line.strip()}")
                models.append('VGG16')
            
            # DenseNet Model
            elif 'DenseNet121' in source:
                print(f"\nModel 3 - DenseNet121 Transfer Learning (Cell {i}):")
                print("  Base: DenseNet121 (pre-trained)")
                lines = source.split('\n')
                for line in lines:
                    if 'DenseNet121' in line:
                        print(f"  - {line.strip()}")
                models.append('DenseNet121')
    
    print(f"\nTotal models implemented: {len(models)}")
    print(f"Models: {', '.join(models)}")

def extract_training_details(cells):
    """Extract training configuration details"""
    print("\n3. TRAINING CONFIGURATION:")
    print("-" * 50)
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Find compilation details
            if 'compile' in source and 'optimizer' in source:
                print(f"\nModel compilation (Cell {i}):")
                lines = source.split('\n')
                for line in lines:
                    if any(keyword in line for keyword in ['optimizer', 'loss', 'metrics']):
                        print(f"  - {line.strip()}")
            
            # Find training details
            if '.fit(' in source and 'epochs' in source:
                print(f"\nTraining configuration (Cell {i}):")
                lines = source.split('\n')
                for line in lines:
                    if '.fit(' in line:
                        # Extract epochs, batch_size, etc.
                        epochs_match = re.search(r'epochs\s*=\s*(\d+)', line)
                        batch_match = re.search(r'batch_size\s*=\s*(\d+)', line)
                        
                        if epochs_match:
                            print(f"  - Epochs: {epochs_match.group(1)}")
                        if batch_match:
                            print(f"  - Batch size: {batch_match.group(1)}")
                        
                        print(f"  - Training call: {line.strip()}")

def extract_results(cells):
    """Extract model performance results"""
    print("\n4. MODEL PERFORMANCE:")
    print("-" * 50)
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Look for evaluation or accuracy results
            if 'outputs' in cell and cell['outputs']:
                for output in cell['outputs']:
                    if 'text' in output:
                        text = ''.join(output['text'])
                        
                        # Look for accuracy scores
                        if 'accuracy' in text.lower() or 'loss' in text.lower():
                            print(f"\nResults from Cell {i}:")
                            lines = text.split('\n')
                            for line in lines:
                                if line.strip() and ('accuracy' in line.lower() or 'loss' in line.lower() or 'val_' in line.lower()):
                                    print(f"  {line.strip()}")
                        
                        # Look for classification reports
                        elif 'precision' in text.lower() and 'recall' in text.lower():
                            print(f"\nClassification Report from Cell {i}:")
                            print(f"  {text.strip()}")

def extract_model_paths(cells):
    """Extract model saving paths and filenames"""
    print("\n5. MODEL SAVING:")
    print("-" * 50)
    
    saved_models = []
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            if '.save(' in source and '.h5' in source:
                # Extract file path
                path_match = re.search(r"\.save\(r?['\"]([^'\"]+\.h5)['\"]", source)
                if path_match:
                    full_path = path_match.group(1)
                    filename = full_path.split('\\')[-1]  # Get just the filename
                    saved_models.append(filename)
                    print(f"\nModel saved in Cell {i}:")
                    print(f"  Filename: {filename}")
                    print(f"  Full path: {full_path}")
    
    print(f"\nTotal models saved: {len(saved_models)}")
    print("Saved model files:")
    for model in saved_models:
        print(f"  - {model}")

if __name__ == "__main__":
    extract_detailed_info()