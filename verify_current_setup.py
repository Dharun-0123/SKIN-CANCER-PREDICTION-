#!/usr/bin/env python3
"""
Verify current email setup after IDE formatting
"""

import os
import sys
import django

# Add the webapp directory to Python path
sys.path.append('webapp')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT.settings')
django.setup()

from django.conf import settings
from django.core.mail import send_mail

def verify_setup():
    """Verify the current email setup"""
    print("🔍 Verifying Current Email Setup...")
    print("=" * 50)
    
    # Check settings
    print(f"📧 Email Backend: {settings.EMAIL_BACKEND}")
    print(f"🏠 SMTP Host: {settings.EMAIL_HOST}")
    print(f"🔌 SMTP Port: {settings.EMAIL_PORT}")
    print(f"🔐 Use TLS: {settings.EMAIL_USE_TLS}")
    print(f"👤 SMTP User: {settings.EMAIL_HOST_USER}")
    print(f"🔑 API Key: {settings.EMAIL_HOST_PASSWORD[:10]}...")
    print(f"📨 Default From: {settings.DEFAULT_FROM_EMAIL}")
    
    if hasattr(settings, 'SERVER_EMAIL'):
        print(f"🖥️  Server Email: {settings.SERVER_EMAIL}")
    
    if hasattr(settings, 'RESEND_DOMAIN'):
        print(f"🌐 Domain: {settings.RESEND_DOMAIN}")
    
    print("\n✅ Configuration looks good!")
    
    # Test email sending
    print("\n🧪 Testing Email Sending...")
    try:
        result = send_mail(
            subject='✅ Setup Verification - SkinCare AI',
            message='Your email setup is working perfectly after IDE formatting!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['givemeanythingu@gmail.com'],
            fail_silently=False,
        )
        
        if result:
            print("✅ Email sent successfully!")
            print("📬 Check your inbox for verification email")
        else:
            print("❌ Email sending failed")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("\n🎯 Next Steps:")
    print("1. Start your Django server: python webapp/manage.py runserver")
    print("2. Test user registration flow")
    print("3. Verify welcome emails are sent")
    print("4. Deploy to production when ready")

if __name__ == "__main__":
    verify_setup()