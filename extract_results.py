#!/usr/bin/env python3
import json

# Load the notebook
with open('skincareai-1 (3).ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print("🎯 Final Model Performance Results")
print("=" * 50)

# Look for test evaluation results
for i, cell in enumerate(notebook['cells']):
    if cell.get('cell_type') == 'code':
        source = ''.join(cell.get('source', []))
        
        # Look for test evaluation
        if 'evaluate(' in source or 'test_ds' in source:
            outputs = cell.get('outputs', [])
            for output in outputs:
                if 'text' in output:
                    text = ''.join(output['text'])
                    if 'accuracy' in text.lower() or 'loss' in text.lower():
                        print(f"\n📊 Test Results (Cell {i}):")
                        print("Source:", source[:200] + "..." if len(source) > 200 else source)
                        print("Output:", text)
        
        # Look for classification report
        if 'classification_report' in source or 'precision_recall_fscore' in source:
            outputs = cell.get('outputs', [])
            for output in outputs:
                if 'text' in output:
                    text = ''.join(output['text'])
                    print(f"\n📈 Classification Report (Cell {i}):")
                    print(text)
        
        # Look for final accuracy numbers
        if 'Test Accuracy' in source or 'Final' in source:
            outputs = cell.get('outputs', [])
            for output in outputs:
                if 'text' in output:
                    text = ''.join(output['text'])
                    print(f"\n🏆 Final Results (Cell {i}):")
                    print(text)

print("\n" + "=" * 50)