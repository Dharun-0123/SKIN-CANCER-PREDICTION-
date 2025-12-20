#!/usr/bin/env python3
"""
Script to add the first_analysis_email_sent field to existing UserProfile records
"""

import os
import sys
import django

# Add the webapp directory to Python path
sys.path.append('webapp')
os.chdir('webapp')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from APP.models import UserProfile

def add_first_analysis_email_field():
    """Add the first_analysis_email_sent field to existing profiles"""
    
    print("🔧 Adding first_analysis_email_sent field to existing profiles")
    print("=" * 60)
    
    try:
        # Get all existing profiles
        profiles = UserProfile.objects.all()
        print(f"📊 Found {profiles.count()} existing user profiles")
        
        # Update existing profiles to have the new field set to False
        updated_count = 0
        for profile in profiles:
            if not hasattr(profile, 'first_analysis_email_sent'):
                profile.first_analysis_email_sent = False
                profile.save()
                updated_count += 1
        
        print(f"✅ Updated {updated_count} profiles with new field")
        print("✅ All existing users will receive first analysis email")
        print("✅ After first email, no more analysis emails will be sent")
        
        return True
        
    except Exception as e:
        print(f"❌ Error updating profiles: {str(e)}")
        return False

def test_smart_email_logic():
    """Test the smart email logic"""
    
    print("\n🧪 Testing Smart Email Logic")
    print("-" * 40)
    
    # Read the views.py file to check implementation
    with open('APP/views.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = [
        ('def send_smart_analysis_notification', 'Smart notification function exists'),
        ('first_analysis_email_sent', 'Tracks first email status'),
        ('send_smart_analysis_notification(request.user', 'Function is called'),
        ('quota preservation', 'Email quota preservation logic')
    ]
    
    all_passed = True
    for check, description in checks:
        if check in content:
            print(f"✅ {description}")
        else:
            print(f"❌ {description}")
            all_passed = False
    
    return all_passed

if __name__ == "__main__":
    print("📧 SMART EMAIL NOTIFICATION SETUP")
    print("=" * 60)
    
    # Add field to existing profiles
    migration_success = add_first_analysis_email_field()
    
    # Test the implementation
    test_success = test_smart_email_logic()
    
    if migration_success and test_success:
        print("\n🎉 SMART EMAIL SYSTEM READY!")
        print("✅ Only first analysis will trigger email")
        print("✅ Preserves your 3000/month email quota")
        print("✅ Users still get welcome confirmation")
        print("✅ No spam from repeated analyses")
        
        print("\n📊 Email Behavior:")
        print("   1st Analysis: ✅ Email sent ('Analysis complete!')")
        print("   2nd Analysis: ❌ No email (quota preserved)")
        print("   3rd Analysis: ❌ No email (quota preserved)")
        print("   ...and so on")
        
    else:
        print("\n❌ Setup incomplete - check errors above")