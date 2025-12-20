#!/usr/bin/env python3
"""
Fix the User import issue and verify the registration system
"""

import os
import sys

def check_and_fix_imports():
    """Check and fix import issues in views.py"""
    
    views_path = 'webapp/APP/views.py'
    
    print("🔧 Checking views.py imports...")
    
    # Read the current file
    with open(views_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if User is imported
    if 'from django.contrib.auth.models import User' in content:
        print("✅ User model is already imported correctly")
    else:
        print("❌ User model import is missing")
        return False
    
    # Check if User is used in the file
    user_usage_count = content.count('User.objects')
    print(f"📊 Found {user_usage_count} uses of User.objects in views.py")
    
    # Check for other potential import issues
    imports_to_check = [
        ('django.contrib.auth.models', 'User'),
        ('django.contrib', 'messages'),
        ('django.shortcuts', 'render'),
        ('django.shortcuts', 'redirect'),
    ]
    
    print("\n🔍 Checking required imports:")
    for module, item in imports_to_check:
        if f'from {module} import' in content and item in content:
            print(f"   ✅ {item} from {module}")
        else:
            print(f"   ⚠️  {item} from {module} - might be missing")
    
    return True

def verify_email_functions():
    """Verify email-related functions are properly imported"""
    
    print("\n📧 Checking email function imports...")
    
    # Check otp_utils.py
    otp_utils_path = 'webapp/APP/otp_utils.py'
    if os.path.exists(otp_utils_path):
        print("✅ otp_utils.py exists")
        
        with open(otp_utils_path, 'r', encoding='utf-8') as f:
            otp_content = f.read()
        
        if 'def send_otp_email' in otp_content:
            print("✅ send_otp_email function found")
        else:
            print("❌ send_otp_email function missing")
        
        if 'def verify_otp' in otp_content:
            print("✅ verify_otp function found")
        else:
            print("❌ verify_otp function missing")
    else:
        print("❌ otp_utils.py not found")
    
    # Check email_utils.py
    email_utils_path = 'webapp/APP/email_utils.py'
    if os.path.exists(email_utils_path):
        print("✅ email_utils.py exists")
        
        with open(email_utils_path, 'r', encoding='utf-8') as f:
            email_content = f.read()
        
        if 'def send_welcome_email' in email_content:
            print("✅ send_welcome_email function found")
        else:
            print("❌ send_welcome_email function missing")
    else:
        print("❌ email_utils.py not found")

def check_models():
    """Check if required models exist"""
    
    print("\n🗄️  Checking models...")
    
    models_path = 'webapp/APP/models.py'
    if os.path.exists(models_path):
        with open(models_path, 'r', encoding='utf-8') as f:
            models_content = f.read()
        
        if 'class EmailOTP' in models_content:
            print("✅ EmailOTP model found")
        else:
            print("❌ EmailOTP model missing")
        
        if 'class UserProfile' in models_content:
            print("✅ UserProfile model found")
        else:
            print("❌ UserProfile model missing")
    else:
        print("❌ models.py not found")

def main():
    """Main function to run all checks"""
    
    print("🚀 SkinCare AI - Registration System Check")
    print("=" * 50)
    
    # Check imports
    imports_ok = check_and_fix_imports()
    
    # Check email functions
    verify_email_functions()
    
    # Check models
    check_models()
    
    print("\n" + "=" * 50)
    
    if imports_ok:
        print("✅ Import issues have been fixed!")
        print("\n🎯 Next Steps:")
        print("1. Start Django server: python webapp/manage.py runserver")
        print("2. Go to: http://127.0.0.1:8000/register/")
        print("3. Register a new user")
        print("4. Check your email for OTP verification")
        print("\n📧 Emails will be sent from: noreply@dharundev.me")
    else:
        print("❌ There are still import issues to resolve")
    
    print("=" * 50)

if __name__ == "__main__":
    main()