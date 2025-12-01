#!/usr/bin/env python
"""
Quick script to switch between email backends
"""
import os

SETTINGS_FILE = 'webapp/PROJECT/settings.py'

BACKENDS = {
    '1': {
        'name': 'Console Backend (Print to Terminal)',
        'code': "EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'",
        'description': 'Emails will print to terminal - perfect for testing'
    },
    '2': {
        'name': 'Resend SMTP (Your Email Only)',
        'code': """EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.resend.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'resend'
EMAIL_HOST_PASSWORD = os.environ.get('RESEND_API_KEY', 're_WBFKPgfG_Kn9Cy8SmSqwh1iePuES8YWJk')""",
        'description': 'Send real emails via Resend (only to givemeanythingu@gmail.com)'
    },
    '3': {
        'name': 'Gmail SMTP (Setup Required)',
        'code': """EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-gmail@gmail.com'  # Change this
EMAIL_HOST_PASSWORD = 'your-app-password'  # Change this""",
        'description': 'Send via Gmail (requires App Password setup)'
    }
}

def main():
    print("📧 Email Backend Switcher")
    print("=" * 60)
    print("\nAvailable backends:")
    for key, backend in BACKENDS.items():
        print(f"\n{key}. {backend['name']}")
        print(f"   {backend['description']}")
    
    print("\n" + "=" * 60)
    print("\n💡 Recommendation for Testing:")
    print("   Choose option 1 (Console Backend)")
    print("   - No email service needed")
    print("   - OTP will print in terminal")
    print("   - Perfect for development")
    
    print("\n💡 For Production:")
    print("   - Verify your domain with Resend")
    print("   - Or use Gmail/SendGrid")
    print("   - See RESEND_DOMAIN_SETUP.md for details")
    
    print("\n" + "=" * 60)
    choice = input("\nEnter your choice (1-3) or 'q' to quit: ").strip()
    
    if choice.lower() == 'q':
        print("Cancelled.")
        return
    
    if choice not in BACKENDS:
        print("❌ Invalid choice!")
        return
    
    backend = BACKENDS[choice]
    print(f"\n✅ Selected: {backend['name']}")
    print(f"\n📝 To apply this change, update your settings.py:")
    print("\n" + "-" * 60)
    print(backend['code'])
    print("-" * 60)
    
    if choice == '1':
        print("\n🎯 With Console Backend:")
        print("   1. Start server: python manage.py runserver")
        print("   2. Register with ANY email")
        print("   3. Check terminal for OTP")
        print("   4. Copy OTP and verify")
    elif choice == '2':
        print("\n🎯 With Resend:")
        print("   1. Start server: python manage.py runserver")
        print("   2. Register with: givemeanythingu@gmail.com")
        print("   3. Check Gmail inbox for OTP")
        print("   4. Enter OTP and verify")
    elif choice == '3':
        print("\n🎯 Gmail Setup Required:")
        print("   1. Go to Google Account settings")
        print("   2. Enable 2-Step Verification")
        print("   3. Generate App Password")
        print("   4. Use App Password in settings")

if __name__ == '__main__':
    main()
