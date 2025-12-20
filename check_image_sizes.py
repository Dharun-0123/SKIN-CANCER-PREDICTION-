#!/usr/bin/env python3
"""
Check the exact image sizes used for each model architecture in the notebook
"""

import json
import re

def check_image_sizes():
    """Check image sizes for each model architecture"""
    
    with open('training/skin.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook['cells']
    
    print("=" * 80)
    print("IMAGE SIZE ANALYSIS FOR EACH MODEL ARCHITECTURE")
    print("=" * 80)
    
    model_info = []
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Look for input_shape definitions
            input_shape_matches = re.findall(r'input_shape\s*=\s*\(([^)]+)\)', source)
            
            if input_shape_matches:
                print(f"\nCell {i} - Input Shape Found:")
                for match in input_shape_matches:
                    print(f"  input_shape=({match})")
                
                # Identify which model this belongs to
                if 'Conv2D(28' in source:
                    model_info.append({
                        'model': 'Basic CNN',
                        'cell': i,
                        'input_shape': input_shape_matches[0],
                        'source_snippet': source[:200] + '...'
                    })
                elif 'VGG16' in source:
                    model_info.append({
                        'model': 'VGG16',
                        'cell': i,
                        'input_shape': input_shape_matches[0],
                        'source_snippet': source[:200] + '...'
                    })
                elif 'DenseNet121' in source:
                    model_info.append({
                        'model': 'DenseNet121',
                        'cell': i,
                        'input_shape': input_shape_matches[0],
                        'source_snippet': source[:200] + '...'
                    })
            
            # Also look for image preprocessing/resizing
            if 'resize' in source.lower() or 'cv2.resize' in source:
                print(f"\nCell {i} - Image Resizing Found:")
                lines = source.split('\n')
                for line in lines:
                    if 'resize' in line.lower():
                        print(f"  {line.strip()}")
            
            # Look for image shape definitions
            if 'img_size' in source or 'image_size' in source or 'IMG_SIZE' in source:
                print(f"\nCell {i} - Image Size Variable:")
                lines = source.split('\n')
                for line in lines:
                    if any(keyword in line for keyword in ['img_size', 'image_size', 'IMG_SIZE']):
                        print(f"  {line.strip()}")
    
    print("\n" + "=" * 80)
    print("SUMMARY OF MODEL INPUT SHAPES")
    print("=" * 80)
    
    for info in model_info:
        print(f"\n{info['model']} (Cell {info['cell']}):")
        print(f"  Input Shape: ({info['input_shape']})")
        print(f"  Code snippet: {info['source_snippet']}")
    
    # Check for any data loading that might show image dimensions
    print("\n" + "=" * 80)
    print("DATA LOADING AND PREPROCESSING")
    print("=" * 80)
    
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Look for image loading and preprocessing
            if 'cv2.imread' in source or 'Image.open' in source or 'plt.imread' in source:
                print(f"\nCell {i} - Image Loading:")
                lines = source.split('\n')
                for line in lines:
                    if any(keyword in line for keyword in ['cv2.imread', 'Image.open', 'plt.imread', 'resize']):
                        print(f"  {line.strip()}")
            
            # Look for array shapes or transformations
            if '.shape' in source and 'img' in source.lower():
                print(f"\nCell {i} - Image Shape Operations:")
                lines = source.split('\n')
                for line in lines:
                    if '.shape' in line and any(keyword in line.lower() for keyword in ['img', 'image', 'x_']):
                        print(f"  {line.strip()}")

if __name__ == "__main__":
    check_image_sizes()