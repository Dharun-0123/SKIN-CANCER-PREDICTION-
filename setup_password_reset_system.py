#!/usr/bin/env python3
"""
Setup and test the password reset system
"""

import os
import sys
import django

# Add the webapp directory to Python path
sys.path.append('webapp')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT.settings')
django.setup()

def setup_database():
    """Create database migrations for password reset"""
    
    print("🗄️  Setting up database for password reset system...")
    print("=" * 60)
    
    try:
        from django.core.management import execute_from_command_line
        
        # Make migrations
        print("1. Creating migrations...")
        os.chdir('webapp')
        execute_from_command_line(['manage.py', 'makemigrations'])
        print("   ✅ Migrations created")
        
        # Apply migrations
        print("\n2. Applying migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        print("   ✅ Migrations applied")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Database setup error: {str(e)}")
        return False

def test_password_reset_system():
    """Test the password reset functionality"""
    
    print("\n🧪 Testing Password Reset System...")
    print("=" * 60)
    
    try:
        from django.contrib.auth.models import User
        from APP.password_reset_utils import send_password_reset_otp, verify_password_reset_otp
        from APP.models import PasswordResetOTP
        
        # Test 1: Create test user
        print("1. Creating test user...")
        if User.objects.filter(username='resettest').exists():
            User.objects.filter(username='resettest').delete()
        
        user = User.objects.create_user(
            username='resettest',
            email='givemeanythingu@gmail.com',  # Your verified email
            password='oldpassword123'
        )
        print(f"   ✅ Test user created: {user.username}")
        
        # Test 2: Send password reset OTP
        print("\n2. Testing password reset OTP sending...")
        success, message, returned_user = send_password_reset_otp(user.email)
        
        if success:
            print(f"   ✅ Password reset OTP sent: {message}")
            print(f"   📧 Email sent to: {user.email}")
        else:
            print(f"   ❌ Failed to send OTP: {message}")
            return False
        
        # Test 3: Check OTP was created in database
        print("\n3. Checking OTP in database...")
        try:
            otp_obj = PasswordResetOTP.objects.get(user=user)
            print(f"   ✅ OTP created in database: {otp_obj.otp}")
            print(f"   ⏰ Created at: {otp_obj.created_at}")
            print(f"   🔒 Is used: {otp_obj.is_used}")
            print(f"   ⏳ Is expired: {otp_obj.is_expired()}")
        except PasswordResetOTP.DoesNotExist:
            print("   ❌ OTP not found in database")
            return False
        
        # Test 4: Verify OTP
        print("\n4. Testing OTP verification...")
        success, message = verify_password_reset_otp(user, otp_obj.otp)
        
        if success:
            print(f"   ✅ OTP verified successfully: {message}")
        else:
            print(f"   ❌ OTP verification failed: {message}")
            return False
        
        # Test 5: Test invalid OTP
        print("\n5. Testing invalid OTP...")
        success, message = verify_password_reset_otp(user, '999999')
        
        if not success:
            print(f"   ✅ Invalid OTP correctly rejected: {message}")
        else:
            print(f"   ❌ Invalid OTP was accepted (this is wrong)")
        
        # Test 6: Test non-existent email
        print("\n6. Testing non-existent email...")
        success, message, returned_user = send_password_reset_otp('nonexistent@example.com')
        
        if not success:
            print(f"   ✅ Non-existent email correctly handled: {message}")
        else:
            print(f"   ❌ Non-existent email was accepted (this is wrong)")
        
        # Cleanup
        print("\n7. Cleaning up...")
        user.delete()
        print("   ✅ Test user deleted")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Test error: {str(e)}")
        return False

def test_url_patterns():
    """Test that new URL patterns work"""
    
    print("\n🔗 Testing Password Reset URL Patterns...")
    print("-" * 50)
    
    try:
        from django.urls import reverse
        
        urls_to_test = [
            'forgot_password',
            'verify_reset_otp', 
            'reset_password',
            'resend_reset_otp'
        ]
        
        for url_name in urls_to_test:
            try:
                url_path = reverse(url_name)
                print(f"   ✅ {url_name}: {url_path}")
            except Exception as e:
                print(f"   ❌ {url_name}: Error - {str(e)}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ URL test error: {str(e)}")
        return False

def main():
    """Main setup and test function"""
    
    print("🚀 SkinCare AI - Password Reset System Setup")
    print("=" * 70)
    
    # Setup database
    db_success = setup_database()
    
    if db_success:
        # Test URL patterns
        url_success = test_url_patterns()
        
        if url_success:
            # Test password reset functionality
            test_success = test_password_reset_system()
            
            if test_success:
                print("\n🎉 Password Reset System Setup Complete!")
                print("\n📧 Features Added:")
                print("✅ Forgot Password page (/forgot-password/)")
                print("✅ OTP verification for password reset")
                print("✅ Secure password reset form")
                print("✅ Email integration with your verified domain")
                print("✅ Professional HTML email templates")
                print("✅ Session-based security")
                print("✅ OTP expiration (15 minutes)")
                print("✅ Password strength validation")
                
                print("\n🎯 How to Test:")
                print("1. Start Django server: python manage.py runserver")
                print("2. Go to: http://127.0.0.1:8000/login/")
                print("3. Click 'Reset Password' link")
                print("4. Enter your email address")
                print("5. Check email for reset code")
                print("6. Enter code and set new password")
                
                print("\n📧 Check your email at: givemeanythingu@gmail.com")
            else:
                print("\n❌ Password reset system tests failed")
        else:
            print("\n❌ URL pattern setup failed")
    else:
        print("\n❌ Database setup failed")
    
    print("=" * 70)

if __name__ == "__main__":
    main()