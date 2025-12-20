#!/usr/bin/env python3
"""
Complete analysis of the skin.ipynb notebook
"""

import json
import re

def analyze_notebook():
    """Analyze the complete notebook structure and content"""
    
    # Load the notebook
    with open('training/skin.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    print("=" * 80)
    print("COMPLETE SKIN CANCER DETECTION NOTEBOOK ANALYSIS")
    print("=" * 80)
    
    cells = notebook['cells']
    print(f"Total number of cells: {len(cells)}")
    
    # Analyze cell types
    code_cells = [cell for cell in cells if cell['cell_type'] == 'code']
    markdown_cells = [cell for cell in cells if cell['cell_type'] == 'markdown']
    
    print(f"Code cells: {len(code_cells)}")
    print(f"Markdown cells: {len(markdown_cells)}")
    
    print("\n" + "=" * 80)
    print("NOTEBOOK STRUCTURE AND WORKFLOW")
    print("=" * 80)
    
    sections = []
    current_section = None
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'markdown':
            # Extract markdown content
            content = ''.join(cell['source']).strip()
            if content and (content.startswith('#') or len(content) > 50):
                sections.append({
                    'type': 'markdown',
                    'index': i,
                    'content': content[:100] + '...' if len(content) > 100 else content
                })
        elif cell['cell_type'] == 'code':
            # Extract code content
            source = ''.join(cell['source']).strip()
            if source:
                # Identify key operations
                if 'import' in source and i < 5:
                    sections.append({
                        'type': 'imports',
                        'index': i,
                        'content': 'Library imports and dependencies'
                    })
                elif 'train' in source.lower() and 'path' in source.lower():
                    sections.append({
                        'type': 'data_loading',
                        'index': i,
                        'content': 'Data loading and path setup'
                    })
                elif 'plot' in source.lower() or 'plt.' in source:
                    sections.append({
                        'type': 'visualization',
                        'index': i,
                        'content': 'Data visualization and plotting'
                    })
                elif 'model' in source.lower() and ('sequential' in source.lower() or 'conv2d' in source.lower()):
                    sections.append({
                        'type': 'model_definition',
                        'index': i,
                        'content': 'Model architecture definition'
                    })
                elif 'compile' in source.lower() or 'fit' in source.lower():
                    sections.append({
                        'type': 'training',
                        'index': i,
                        'content': 'Model compilation and training'
                    })
                elif 'evaluate' in source.lower() or 'predict' in source.lower():
                    sections.append({
                        'type': 'evaluation',
                        'index': i,
                        'content': 'Model evaluation and prediction'
                    })
                elif 'save' in source.lower() and '.h5' in source:
                    sections.append({
                        'type': 'model_saving',
                        'index': i,
                        'content': 'Model saving'
                    })
    
    # Print sections
    for i, section in enumerate(sections):
        print(f"{i+1:2d}. Cell {section['index']:2d} - {section['type']:15s}: {section['content']}")
    
    print("\n" + "=" * 80)
    print("DETAILED CODE ANALYSIS")
    print("=" * 80)
    
    # Analyze specific aspects
    analyze_imports(cells)
    analyze_data_structure(cells)
    analyze_models(cells)
    analyze_training(cells)
    analyze_evaluation(cells)
    
    return notebook

def analyze_imports(cells):
    """Analyze import statements"""
    print("\n1. LIBRARY IMPORTS:")
    print("-" * 40)
    
    imports = []
    for cell in cells:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if 'import' in source:
                lines = source.split('\n')
                for line in lines:
                    if line.strip().startswith('import') or line.strip().startswith('from'):
                        imports.append(line.strip())
    
    # Categorize imports
    categories = {
        'Data Processing': ['numpy', 'pandas', 'cv2', 'PIL'],
        'Machine Learning': ['tensorflow', 'keras', 'sklearn'],
        'Visualization': ['matplotlib', 'seaborn', 'plt'],
        'System/Utils': ['os', 'shutil', 'glob', 'pathlib', 'random', 'tqdm']
    }
    
    for category, keywords in categories.items():
        print(f"\n{category}:")
        for imp in imports:
            if any(keyword in imp for keyword in keywords):
                print(f"  - {imp}")

def analyze_data_structure(cells):
    """Analyze data loading and structure"""
    print("\n2. DATA STRUCTURE:")
    print("-" * 40)
    
    for cell in cells:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Look for folder structure analysis
            if 'for folder in os.listdir' in source and 'train' in source.lower():
                print("Dataset structure analysis found:")
                if 'output' in cell and cell['output']:
                    for output in cell['output']:
                        if 'text' in output:
                            text = ''.join(output['text'])
                            print(text)
                break
    
    # Look for class definitions
    print("\nSkin condition classes identified:")
    classes = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc', 'not_skin_cancer']
    class_names = {
        'akiec': 'Actinic keratoses',
        'bcc': 'Basal cell carcinoma', 
        'bkl': 'Benign keratosis-like lesions',
        'df': 'Dermatofibroma',
        'mel': 'Melanoma',
        'nv': 'Melanocytic nevi',
        'vasc': 'Vascular lesions',
        'not_skin_cancer': 'Not skin cancer'
    }
    
    for cls in classes:
        full_name = class_names.get(cls, cls)
        print(f"  - {cls}: {full_name}")

def analyze_models(cells):
    """Analyze model architectures"""
    print("\n3. MODEL ARCHITECTURES:")
    print("-" * 40)
    
    models_found = []
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Look for model definitions
            if 'Sequential' in source and ('Conv2D' in source or 'Dense' in source):
                print(f"\nModel found in cell {i}:")
                
                # Extract model layers
                lines = source.split('\n')
                in_model = False
                layers = []
                
                for line in lines:
                    if 'Sequential' in line or 'model.add' in line:
                        in_model = True
                    
                    if in_model and ('Conv2D' in line or 'Dense' in line or 'MaxPool' in line or 'Dropout' in line or 'Flatten' in line):
                        layer_info = line.strip()
                        if 'model.add' in layer_info:
                            layer_info = layer_info.replace('model.add(', '').replace(')', '')
                        layers.append(layer_info)
                
                for layer in layers:
                    print(f"  - {layer}")
                
                models_found.append({
                    'cell': i,
                    'layers': layers
                })
    
    print(f"\nTotal models found: {len(models_found)}")

def analyze_training(cells):
    """Analyze training process"""
    print("\n4. TRAINING PROCESS:")
    print("-" * 40)
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Look for compilation
            if 'compile' in source.lower():
                print(f"\nModel compilation found in cell {i}:")
                lines = source.split('\n')
                for line in lines:
                    if 'compile' in line.lower():
                        print(f"  - {line.strip()}")
            
            # Look for training
            if 'fit' in source and 'model' in source:
                print(f"\nModel training found in cell {i}:")
                lines = source.split('\n')
                for line in lines:
                    if 'fit' in line and 'model' in line:
                        print(f"  - {line.strip()}")

def analyze_evaluation(cells):
    """Analyze evaluation and results"""
    print("\n5. EVALUATION & RESULTS:")
    print("-" * 40)
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Look for evaluation
            if 'evaluate' in source.lower() or 'accuracy' in source.lower():
                print(f"\nEvaluation found in cell {i}:")
                if 'output' in cell and cell['output']:
                    for output in cell['output']:
                        if 'text' in output:
                            text = ''.join(output['text'])
                            if text.strip():
                                print(f"  Output: {text.strip()}")
            
            # Look for model saving
            if 'save' in source and '.h5' in source:
                print(f"\nModel saving found in cell {i}:")
                lines = source.split('\n')
                for line in lines:
                    if 'save' in line and '.h5' in line:
                        print(f"  - {line.strip()}")

if __name__ == "__main__":
    analyze_notebook()