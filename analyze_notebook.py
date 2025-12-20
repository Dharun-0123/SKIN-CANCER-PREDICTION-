#!/usr/bin/env python3
import json

# Load the notebook
with open('skincareai-1 (3).ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print("🔬 SkinCare AI - New Model Analysis")
print("=" * 50)

# Count cells
total_cells = len(notebook['cells'])
print(f"Total cells: {total_cells}")

# Find key information
dataset_info = {}
model_info = {}
training_info = {}

for i, cell in enumerate(notebook['cells']):
    if cell.get('cell_type') == 'code':
        source = ''.join(cell.get('source', []))
        
        # Look for dataset information
        if 'Counter(' in source and 'label_map' in source:
            outputs = cell.get('outputs', [])
            for output in outputs:
                if 'text' in output:
                    text = ''.join(output['text'])
                    if 'Counter' in text:
                        print(f"\n📊 Dataset Information (Cell {i}):")
                        print(text)
        
        # Look for data split information
        if 'Split complete' in source or 'train_dir' in source:
            outputs = cell.get('outputs', [])
            for output in outputs:
                if 'text' in output:
                    text = ''.join(output['text'])
                    if 'Split complete' in text or 'train:' in text:
                        print(f"\n📈 Data Split Information (Cell {i}):")
                        print(text)
        
        # Look for model architecture
        if 'EfficientNet' in source or 'model.compile' in source:
            print(f"\n🏗️ Model Architecture (Cell {i}):")
            print(source[:500] + "..." if len(source) > 500 else source)
        
        # Look for training results
        if 'fit(' in source or 'history' in source:
            print(f"\n🚀 Training Process (Cell {i}):")
            print(source[:300] + "..." if len(source) > 300 else source)
            
            outputs = cell.get('outputs', [])
            for output in outputs:
                if 'text' in output:
                    text = ''.join(output['text'])
                    if 'Epoch' in text or 'accuracy' in text or 'loss' in text:
                        print("Training Output:")
                        print(text[:1000] + "..." if len(text) > 1000 else text)

print("\n" + "=" * 50)
print("Analysis Complete!")