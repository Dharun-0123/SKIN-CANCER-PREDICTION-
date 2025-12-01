#!/usr/bin/env python
"""
Setup Verification Script for Skin Cancer Classification System
Run this before starting the server to check if everything is configured correctly.
"""

import os
import sys

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version: {}.{}.{} (OK)".format(version.major, version.minor, version.micro))
        return True
    else:
        print("❌ Python version: {}.{}.{} (Need 3.8+)".format(version.major, version.minor, version.micro))
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required = ['django', 'tensorflow', 'keras', 'PIL', 'numpy', 'cv2', 'sklearn']
    missing = []
    
    for package in required:
        try:
            if package == 'PIL':
                __import__('PIL')
            elif package == 'cv2':
                __import__('cv2')
            else:
                __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} NOT installed")
            missing.append(package)
    
    return len(missing) == 0, missing

def check_model_files():
    """Check if model files exist"""
    models = ['CNN_skin-cancer.h5', 'den_skin-cancer.h5']
    all_exist = True
    
    for model in models:
        if os.path.exists(model):
            size = os.path.getsize(model) / (1024 * 1024)  # Size in MB
            print(f"✅ {model} found ({size:.2f} MB)")
        else:
            print(f"❌ {model} NOT found")
            all_exist = False
    
    return all_exist

def check_directories():
    """Check if required directories exist"""
    dirs = ['media', 'static', 'templates', 'APP']
    all_exist = True
    
    for directory in dirs:
        if os.path.exists(directory):
            print(f"✅ {directory}/ directory exists")
        else:
            print(f"⚠️  {directory}/ directory missing (will be created)")
            try:
                os.makedirs(directory, exist_ok=True)
                print(f"   Created {directory}/ directory")
            except:
                all_exist = False
    
    return all_exist

def check_database():
    """Check database status"""
    if os.path.exists('db.sqlite3'):
        size = os.path.getsize('db.sqlite3') / 1024  # Size in KB
        print(f"✅ Database exists ({size:.2f} KB)")
        return True
    else:
        print("⚠️  Database not found (run migrations)")
        return False

def main():
    print("=" * 60)
    print("Skin Cancer Classification System - Setup Verification")
    print("=" * 60)
    print()
    
    # Check Python version
    print("1. Checking Python version...")
    python_ok = check_python_version()
    print()
    
    # Check dependencies
    print("2. Checking dependencies...")
    deps_ok, missing = check_dependencies()
    print()
    
    # Check model files
    print("3. Checking model files...")
    models_ok = check_model_files()
    print()
    
    # Check directories
    print("4. Checking directories...")
    dirs_ok = check_directories()
    print()
    
    # Check database
    print("5. Checking database...")
    db_ok = check_database()
    print()
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    all_ok = python_ok and deps_ok and models_ok and dirs_ok
    
    if all_ok:
        print("✅ All checks passed! You're ready to run the server.")
        print()
        print("To start the server, run:")
        print("  python manage.py runserver")
        print()
        if not db_ok:
            print("⚠️  Don't forget to run migrations first:")
            print("  python manage.py makemigrations")
            print("  python manage.py migrate")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print()
        if not deps_ok:
            print("To install missing dependencies:")
            print("  pip install -r requirements.txt")
        if not models_ok:
            print("Make sure model files are in the PROJECT directory")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
