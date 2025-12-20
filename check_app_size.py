#!/usr/bin/env python3
"""
Check the total size of the SkinCare AI application
This will help determine if it fits within Heroku's 500MB slug limit
"""

import os
import sys
from pathlib import Path

def get_size(path):
    """Get size of file or directory in bytes"""
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total += os.path.getsize(filepath)
                except (OSError, FileNotFoundError):
                    pass
        return total
    return 0

def format_size(bytes_size):
    """Format bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} TB"

def analyze_app_size():
    print("🔍 SkinCare AI Application Size Analysis")
    print("=" * 60)
    
    # Define components to check
    components = {
        "Django Application Code": "webapp/",
        "ML Models": "webapp/models/",
        "Training Data/Notebooks": "training/",
        "Documentation": ["docs/", "*.md"],
        "Test Files": "test_*.py",
        "Configuration": [".env", ".env.example", "requirements.txt"],
        "Other Python Files": "*.py"
    }
    
    total_size = 0
    component_sizes = {}
    
    print("📊 Component Analysis:")
    print("-" * 60)
    
    # Check webapp directory (main application)
    if os.path.exists("webapp"):
        webapp_size = get_size("webapp")
        component_sizes["Django Application"] = webapp_size
        total_size += webapp_size
        print(f"📁 Django Application (webapp/): {format_size(webapp_size)}")
        
        # Break down webapp components
        webapp_subdirs = {
            "Models (ML)": "webapp/models/",
            "Templates": "webapp/templates/",
            "Static Files": "webapp/static/",
            "Media Files": "webapp/media/",
            "Python Code": ["webapp/APP/", "webapp/PROJECT/"]
        }
        
        for name, path in webapp_subdirs.items():
            if isinstance(path, list):
                subdir_size = sum(get_size(p) for p in path if os.path.exists(p))
            else:
                subdir_size = get_size(path) if os.path.exists(path) else 0
            
            if subdir_size > 0:
                print(f"  └── {name}: {format_size(subdir_size)}")
    
    # Check ML models specifically
    model_files = []
    if os.path.exists("webapp/models"):
        for file in os.listdir("webapp/models"):
            if file.endswith(('.h5', '.pkl', '.joblib', '.model')):
                filepath = os.path.join("webapp/models", file)
                size = get_size(filepath)
                model_files.append((file, size))
                print(f"  🧠 {file}: {format_size(size)}")
    
    # Check training directory
    if os.path.exists("training"):
        training_size = get_size("training")
        component_sizes["Training/Notebooks"] = training_size
        total_size += training_size
        print(f"📁 Training/Notebooks: {format_size(training_size)}")
    
    # Check documentation
    doc_size = 0
    doc_files = []
    for file in os.listdir("."):
        if file.endswith(".md"):
            size = get_size(file)
            doc_size += size
            doc_files.append((file, size))
    
    if os.path.exists("docs"):
        doc_size += get_size("docs")
    
    if doc_size > 0:
        component_sizes["Documentation"] = doc_size
        total_size += doc_size
        print(f"📁 Documentation: {format_size(doc_size)}")
    
    # Check test files
    test_size = 0
    test_files = []
    for file in os.listdir("."):
        if file.startswith("test_") and file.endswith(".py"):
            size = get_size(file)
            test_size += size
            test_files.append((file, size))
    
    if test_size > 0:
        component_sizes["Test Files"] = test_size
        total_size += test_size
        print(f"📁 Test Files: {format_size(test_size)}")
    
    # Check other Python files
    other_py_size = 0
    for file in os.listdir("."):
        if file.endswith(".py") and not file.startswith("test_"):
            other_py_size += get_size(file)
    
    if other_py_size > 0:
        component_sizes["Other Python Files"] = other_py_size
        total_size += other_py_size
        print(f"📁 Other Python Files: {format_size(other_py_size)}")
    
    # Check notebooks
    notebook_size = 0
    for file in os.listdir("."):
        if file.endswith(".ipynb"):
            notebook_size += get_size(file)
    
    if notebook_size > 0:
        component_sizes["Jupyter Notebooks"] = notebook_size
        total_size += notebook_size
        print(f"📁 Jupyter Notebooks: {format_size(notebook_size)}")
    
    print("\n" + "=" * 60)
    print("📊 DEPLOYMENT SIZE ANALYSIS")
    print("=" * 60)
    
    # Calculate deployment-relevant size (excluding training data, tests, docs)
    deployment_size = 0
    deployment_components = {}
    
    if os.path.exists("webapp"):
        # Include only essential webapp components
        essential_paths = [
            "webapp/APP/",
            "webapp/PROJECT/", 
            "webapp/templates/",
            "webapp/models/",  # ML models are essential
            "webapp/static/"
        ]
        
        for path in essential_paths:
            if os.path.exists(path):
                size = get_size(path)
                deployment_size += size
                deployment_components[path] = size
                print(f"✅ {path}: {format_size(size)}")
    
    # Add requirements.txt and other essential files
    essential_files = ["requirements.txt", ".env.example"]
    for file in essential_files:
        if os.path.exists(file):
            size = get_size(file)
            deployment_size += size
            print(f"✅ {file}: {format_size(size)}")
    
    print(f"\n🎯 DEPLOYMENT SIZE ESTIMATE: {format_size(deployment_size)}")
    
    # Heroku slug limit analysis
    heroku_limit = 500 * 1024 * 1024  # 500MB in bytes
    print(f"\n📋 HEROKU COMPATIBILITY:")
    print(f"   Heroku Slug Limit: {format_size(heroku_limit)}")
    print(f"   Your App Size: {format_size(deployment_size)}")
    print(f"   Remaining Space: {format_size(heroku_limit - deployment_size)}")
    
    if deployment_size < heroku_limit:
        percentage = (deployment_size / heroku_limit) * 100
        print(f"   ✅ FITS IN HEROKU! ({percentage:.1f}% of limit used)")
    else:
        overage = deployment_size - heroku_limit
        print(f"   ❌ TOO LARGE for Heroku by {format_size(overage)}")
    
    # Platform recommendations
    print(f"\n🚀 PLATFORM RECOMMENDATIONS:")
    
    if deployment_size < 100 * 1024 * 1024:  # < 100MB
        print("   ✅ Perfect for: Heroku, Railway, Render, Vercel")
    elif deployment_size < 500 * 1024 * 1024:  # < 500MB
        print("   ✅ Good for: Heroku, Railway, Render, DigitalOcean")
        print("   ⚠️  Tight fit: Heroku (watch dependencies)")
    else:  # > 500MB
        print("   ❌ Too large for: Heroku")
        print("   ✅ Recommended: DigitalOcean, AWS, Azure, GCP")
    
    # Optimization suggestions
    print(f"\n💡 OPTIMIZATION SUGGESTIONS:")
    
    # Check for large model files
    large_models = [f for f, s in model_files if s > 20 * 1024 * 1024]  # > 20MB
    if large_models:
        print("   🧠 Large ML Models detected:")
        for model in large_models:
            print(f"      - Consider model compression for {model}")
    
    # Check for unnecessary files
    if test_size > 10 * 1024 * 1024:  # > 10MB
        print("   🧪 Large test files - exclude from deployment")
    
    if notebook_size > 50 * 1024 * 1024:  # > 50MB
        print("   📓 Large notebooks - exclude from deployment")
    
    return {
        'total_size': total_size,
        'deployment_size': deployment_size,
        'heroku_compatible': deployment_size < heroku_limit,
        'component_sizes': component_sizes
    }

if __name__ == "__main__":
    result = analyze_app_size()
    
    print(f"\n🎉 Analysis Complete!")
    print(f"Total Project Size: {format_size(result['total_size'])}")
    print(f"Deployment Size: {format_size(result['deployment_size'])}")
    print(f"Heroku Compatible: {'✅ Yes' if result['heroku_compatible'] else '❌ No'}")