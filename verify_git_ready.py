#!/usr/bin/env python
"""
Verify project is ready for Git upload (no sensitive data exposed)
"""
import os
import re

def check_file_for_secrets(filepath, patterns):
    """Check if file contains any sensitive patterns"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            found = []
            for name, pattern in patterns.items():
                if re.search(pattern, content):
                    found.append(name)
            return found
    except:
        return []

def main():
    print("🔍 Verifying Git Upload Safety")
    print("=" * 60)
    
    # Patterns to check for
    sensitive_patterns = {
        'Resend API Key': r're_[A-Za-z0-9]{30,}',
        'Perplexity API Key': r'pplx-[A-Za-z0-9]{30,}',
    }
    
    # Files to check
    files_to_check = [
        'webapp/PROJECT/settings.py',
        'webapp/APP/views.py',
        'webapp/APP/otp_utils.py',
        'webapp/APP/ai_assistant.py',
    ]
    
    issues_found = False
    
    print("\n📋 Checking files for hardcoded secrets...\n")
    
    for filepath in files_to_check:
        if os.path.exists(filepath):
            secrets = check_file_for_secrets(filepath, sensitive_patterns)
            if secrets:
                print(f"❌ {filepath}")
                for secret in secrets:
                    print(f"   ⚠️  Found: {secret}")
                issues_found = True
            else:
                print(f"✅ {filepath}")
        else:
            print(f"⚠️  {filepath} (not found)")
    
    # Check if .env exists
    print("\n📋 Checking environment setup...\n")
    
    if os.path.exists('.env'):
        print("✅ .env file exists (contains your API keys)")
    else:
        print("❌ .env file missing!")
        issues_found = True
    
    if os.path.exists('.env.example'):
        print("✅ .env.example exists (template for others)")
    else:
        print("❌ .env.example missing!")
        issues_found = True
    
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'r') as f:
            gitignore = f.read()
            if '.env' in gitignore:
                print("✅ .gitignore includes .env")
            else:
                print("❌ .gitignore doesn't exclude .env!")
                issues_found = True
    else:
        print("❌ .gitignore missing!")
        issues_found = True
    
    print("\n" + "=" * 60)
    
    if issues_found:
        print("❌ ISSUES FOUND - DO NOT UPLOAD TO GIT YET!")
        print("\nPlease fix the issues above before uploading.")
        return False
    else:
        print("✅ ALL CHECKS PASSED!")
        print("\n🚀 Your project is ready for Git upload!")
        print("\n📝 Next steps:")
        print("   1. git init")
        print("   2. git add .")
        print("   3. git commit -m 'Initial commit'")
        print("   4. git remote add origin <your-repo-url>")
        print("   5. git push -u origin main")
        print("\n📖 See GIT_UPLOAD_GUIDE.md for detailed instructions")
        return True

if __name__ == '__main__':
    main()
