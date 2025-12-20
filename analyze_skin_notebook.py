#!/usr/bin/env python3
"""
Comprehensive analysis of the skin.ipynb notebook
"""

import json
import re

def analyze_skin_notebook():
    print("🔬 Complete Analysis of skin.ipynb")
    print("=" * 60)
    
    try:
        with open('training/skin.ipynb', 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"❌ Error reading notebook: {e}")
        return False
    
    total_cells = len(notebook['cells'])
    print(f"📊 Total cells: {total_cells}")
    
    # Analyze different sections
    sections = {
        'data_loading': [],
        'data_exploration': [],
        'preprocessing': [],
        'model_building': [],
        'training': [],
        'evaluation': [],
        'visualization': []
    }
    
    dataset_info = {}
    model_info = {}
    performance_metrics = {}
    
    print(f"\n📋 Notebook Analysis:")
    print("-" * 40)
    
    for i, cell in enumerate(notebook['cells']):
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            outputs = cell.get('outputs', [])
            
            # Extract dataset information
            if 'Number of Images:' in str(outputs):
                print(f"\n📊 Dataset Information (Cell {i}):")
                for output in outputs:
                    if 'text' in output:
                        text = ''.join(output['text'])
                        if 'Folder:' in text and 'Number of Images:' in text:
                            lines = text.strip().split('\n')
                            for j in range(0, len(lines), 4):
                                if j+2 < len(lines):
                                    folder = lines[j].replace('Folder: ', '').strip()
                                    count = lines[j+2].replace('Number of Images: ', '').strip()
                                    if folder and count.isdigit():
                                        dataset_info[folder] = int(count)
                                        print(f"   {folder}: {count} images")
            
            # Extract model architecture
            if 'Sequential' in source or 'Conv2D' in source or 'Dense' in source:
                if len(source) > 100:  # Only show substantial model code
                    print(f"\n🏗️ Model Architecture (Cell {i}):")
                    print(f"   {source[:200]}...")
                    sections['model_building'].append(i)
            
            # Extract training information
            if 'fit(' in source or 'model.fit' in source:
                print(f"\n🚀 Training Process (Cell {i}):")
                print(f"   {source[:150]}...")
                sections['training'].append(i)
                
                # Look for training output
                for output in outputs:
                    if 'text' in output:
                        text = ''.join(output['text'])
                        if 'Epoch' in text and 'accuracy' in text:
                            print(f"   Training Output Found")
                            # Extract final accuracy if possible
                            lines = text.split('\n')
                            for line in lines[-10:]:
                                if 'accuracy:' in line:
                                    print(f"   Final line: {line.strip()}")
            
            # Extract evaluation metrics
            if 'evaluate' in source or 'accuracy_score' in source or 'classification_report' in source:
                print(f"\n📈 Evaluation (Cell {i}):")
                sections['evaluation'].append(i)
                
                for output in outputs:
                    if 'text' in output:
                        text = ''.join(output['text'])
                        if 'accuracy' in text.lower() or 'precision' in text.lower():
                            print(f"   Metrics found: {text[:100]}...")
            
            # Extract model saving
            if 'save(' in source or 'save_model' in source:
                print(f"\n💾 Model Saving (Cell {i}):")
                print(f"   {source[:100]}...")
            
            # Extract data preprocessing
            if 'ImageDataGenerator' in source or 'train_test_split' in source:
                print(f"\n🔄 Data Preprocessing (Cell {i}):")
                sections['preprocessing'].append(i)
            
            # Extract visualization
            if 'plt.' in source or 'matplotlib' in source or 'plot' in source:
                if 'confusion_matrix' in source or 'accuracy' in source:
                    print(f"\n📊 Visualization (Cell {i}):")
                    sections['visualization'].append(i)
    
    # Summary
    print(f"\n" + "=" * 60)
    print("📋 NOTEBOOK SUMMARY")
    print("=" * 60)
    
    if dataset_info:
        total_images = sum(dataset_info.values())
        print(f"\n📊 Dataset Statistics:")
        print(f"   Total Images: {total_images:,}")
        print(f"   Total Classes: {len(dataset_info)}")
        print(f"\n🏷️ Class Distribution:")
        for class_name, count in sorted(dataset_info.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_images) * 100
            print(f"   {class_name:<20}: {count:>4} images ({percentage:>5.1f}%)")
    
    print(f"\n🔧 Notebook Structure:")
    print(f"   Data Loading: {len(sections['data_loading'])} cells")
    print(f"   Preprocessing: {len(sections['preprocessing'])} cells")
    print(f"   Model Building: {len(sections['model_building'])} cells")
    print(f"   Training: {len(sections['training'])} cells")
    print(f"   Evaluation: {len(sections['evaluation'])} cells")
    print(f"   Visualization: {len(sections['visualization'])} cells")
    
    # Extract key information
    print(f"\n🎯 Key Findings:")
    if dataset_info:
        print(f"   ✅ Dataset: {total_images:,} images across {len(dataset_info)} classes")
        
        # Identify class imbalance
        max_class = max(dataset_info.values())
        min_class = min(dataset_info.values())
        imbalance_ratio = max_class / min_class
        print(f"   ⚖️ Class Imbalance: {imbalance_ratio:.1f}:1 ratio")
        
        # Most/least represented classes
        sorted_classes = sorted(dataset_info.items(), key=lambda x: x[1], reverse=True)
        print(f"   📈 Largest class: {sorted_classes[0][0]} ({sorted_classes[0][1]} images)")
        print(f"   📉 Smallest class: {sorted_classes[-1][0]} ({sorted_classes[-1][1]} images)")
    
    if sections['model_building']:
        print(f"   🏗️ Model Architecture: CNN with Conv2D and Dense layers")
    
    if sections['training']:
        print(f"   🚀 Training: Model training implemented")
    
    if sections['evaluation']:
        print(f"   📊 Evaluation: Performance metrics calculated")
    
    return {
        'total_cells': total_cells,
        'dataset_info': dataset_info,
        'sections': sections
    }

if __name__ == "__main__":
    result = analyze_skin_notebook()
    
    if result:
        print(f"\n🎉 Analysis Complete!")
        if result['dataset_info']:
            total = sum(result['dataset_info'].values())
            print(f"📊 Dataset: {total:,} images, {len(result['dataset_info'])} classes")
        print(f"📝 Notebook: {result['total_cells']} cells total")
    else:
        print(f"\n❌ Analysis failed!")