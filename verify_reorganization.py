"""
Project Reorganization Verification Script
Checks if the reorganization plan has been fulfilled
"""

import os
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def check_exists(path, item_type="file"):
    """Check if a path exists"""
    p = Path(path)
    exists = p.exists()
    
    if item_type == "folder":
        exists = exists and p.is_dir()
    elif item_type == "file":
        exists = exists and p.is_file()
    
    status = f"{Fore.GREEN}✅" if exists else f"{Fore.RED}❌"
    return exists, status

def check_empty(path):
    """Check if a folder is empty"""
    p = Path(path)
    if not p.exists():
        return True, f"{Fore.YELLOW}⚠️  (doesn't exist)"
    
    if not p.is_dir():
        return False, f"{Fore.RED}❌ (not a folder)"
    
    is_empty = not any(p.iterdir())
    status = f"{Fore.GREEN}✅ (empty)" if is_empty else f"{Fore.YELLOW}⚠️  (has content)"
    return is_empty, status

def main():
    print("=" * 80)
    print(f"{Fore.CYAN}📋 PROJECT REORGANIZATION VERIFICATION")
    print("=" * 80)
    print()
    
    total_checks = 0
    passed_checks = 0
    
    # 1. Check for folders that should be deleted/empty
    print(f"{Fore.YELLOW}1. EMPTY FOLDERS TO DELETE")
    print("-" * 80)
    
    empty_folders = [
        "APP",
        "media", 
        "static",
        "templates"
    ]
    
    for folder in empty_folders:
        is_empty, status = check_empty(folder)
        total_checks += 1
        if is_empty:
            passed_checks += 1
        print(f"  {status} {folder}/ should be empty or deleted")
    print()
    
    # 2. Check for new structure folders
    print(f"{Fore.YELLOW}2. NEW STRUCTURE FOLDERS")
    print("-" * 80)
    
    new_folders = [
        ("docs", "folder"),
        ("webapp", "folder"),
        ("webapp/models", "folder"),
        ("webapp/scripts", "folder"),
        ("webapp/APP", "folder"),
        ("webapp/PROJECT", "folder"),
        ("webapp/templates", "folder"),
        ("webapp/static", "folder"),
        ("webapp/media", "folder"),
        ("training", "folder"),
        ("training/data", "folder"),
    ]
    
    for folder, ftype in new_folders:
        exists, status = check_exists(folder, ftype)
        total_checks += 1
        if exists:
            passed_checks += 1
        print(f"  {status} {folder}/")
    print()
    
    # 3. Check for moved files
    print(f"{Fore.YELLOW}3. KEY FILES IN CORRECT LOCATION")
    print("-" * 80)
    
    key_files = [
        ("webapp/manage.py", "file"),
        ("webapp/requirements.txt", "file"),
        ("training/skin.ipynb", "file"),
        ("training/SKIN CANCER.docx", "file"),
    ]
    
    for file_path, ftype in key_files:
        exists, status = check_exists(file_path, ftype)
        total_checks += 1
        if exists:
            passed_checks += 1
        print(f"  {status} {file_path}")
    print()
    
    # 4. Check for model files
    print(f"{Fore.YELLOW}4. MODEL FILES")
    print("-" * 80)
    
    model_files = [
        "webapp/models/CNN_skin-cancer.h5",
        "webapp/models/den_skin-cancer.h5",
    ]
    
    for model_file in model_files:
        exists, status = check_exists(model_file, "file")
        total_checks += 1
        if exists:
            passed_checks += 1
        print(f"  {status} {model_file}")
    print()
    
    # 5. Check for utility scripts
    print(f"{Fore.YELLOW}5. UTILITY SCRIPTS")
    print("-" * 80)
    
    scripts = [
        "webapp/scripts/check_setup.py",
        "webapp/scripts/fix_templates.py",
        "webapp/scripts/performance_check.py",
    ]
    
    for script in scripts:
        exists, status = check_exists(script, "file")
        total_checks += 1
        if exists:
            passed_checks += 1
        print(f"  {status} {script}")
    print()
    
    # 6. Check for training data
    print(f"{Fore.YELLOW}6. TRAINING DATA")
    print("-" * 80)
    
    data_folders = [
        "training/data/akiec",
        "training/data/bcc",
        "training/data/bkl",
        "training/data/df",
        "training/data/mel",
        "training/data/not_skin_cancer",
        "training/data/nv",
        "training/data/vasc",
    ]
    
    for data_folder in data_folders:
        exists, status = check_exists(data_folder, "folder")
        total_checks += 1
        if exists:
            passed_checks += 1
        print(f"  {status} {data_folder}/")
    print()
    
    # 7. Check for old DEPLOYMENT structure
    print(f"{Fore.YELLOW}7. OLD STRUCTURE (SHOULD BE REMOVED)")
    print("-" * 80)
    
    old_structure = Path("DEPLOYMENT/DEPLOYMENT/PROJECT")
    if old_structure.exists():
        print(f"  {Fore.RED}❌ DEPLOYMENT/DEPLOYMENT/PROJECT/ still exists (should be removed)")
        total_checks += 1
    else:
        print(f"  {Fore.GREEN}✅ DEPLOYMENT/DEPLOYMENT/PROJECT/ removed")
        total_checks += 1
        passed_checks += 1
    print()
    
    # 8. Check for documentation
    print(f"{Fore.YELLOW}8. DOCUMENTATION")
    print("-" * 80)
    
    docs = [
        "README.md",
        "docs/SETUP_GUIDE.md",
        "docs/PERFORMANCE_REPORT.md",
        "docs/TESTING_GUIDE.md",
    ]
    
    for doc in docs:
        exists, status = check_exists(doc, "file")
        total_checks += 1
        if exists:
            passed_checks += 1
        print(f"  {status} {doc}")
    print()
    
    # Summary
    print("=" * 80)
    print(f"{Fore.CYAN}📊 SUMMARY")
    print("=" * 80)
    
    percentage = (passed_checks / total_checks * 100) if total_checks > 0 else 0
    
    print(f"Total Checks: {total_checks}")
    print(f"Passed: {Fore.GREEN}{passed_checks}")
    print(f"Failed: {Fore.RED}{total_checks - passed_checks}")
    print(f"Completion: {percentage:.1f}%")
    print()
    
    if percentage == 100:
        print(f"{Fore.GREEN}✅ REORGANIZATION COMPLETE!")
        print(f"{Fore.GREEN}🎉 All requirements fulfilled!")
    elif percentage >= 80:
        print(f"{Fore.YELLOW}⚠️  REORGANIZATION MOSTLY COMPLETE")
        print(f"{Fore.YELLOW}Some items still need attention")
    elif percentage >= 50:
        print(f"{Fore.YELLOW}⚠️  REORGANIZATION IN PROGRESS")
        print(f"{Fore.YELLOW}About half complete")
    else:
        print(f"{Fore.RED}❌ REORGANIZATION NOT STARTED")
        print(f"{Fore.RED}Most items still need to be done")
    
    print()
    print("=" * 80)
    
    # Recommendations
    if percentage < 100:
        print(f"{Fore.CYAN}💡 NEXT STEPS")
        print("=" * 80)
        
        if not Path("webapp/manage.py").exists():
            print("1. Move DEPLOYMENT/DEPLOYMENT/PROJECT/* to webapp/")
        
        if not Path("training/skin.ipynb").exists():
            print("2. Move skin.ipynb to training/")
        
        if not Path("training/SKIN CANCER.docx").exists():
            print("3. Move 'SKIN CANCER.docx' to training/")
        
        if not Path("training/data/akiec").exists():
            print("4. Move Train/* folders to training/data/")
        
        if Path("DEPLOYMENT/DEPLOYMENT/PROJECT").exists():
            print("5. Remove old DEPLOYMENT/DEPLOYMENT/PROJECT structure")
        
        if not Path("docs/SETUP_GUIDE.md").exists():
            print("6. Create documentation in docs/ folder")
        
        print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
