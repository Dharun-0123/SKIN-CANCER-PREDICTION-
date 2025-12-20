#!/usr/bin/env python3
"""
Setup database for email verification system
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
    """Setup database with required tables"""
    
    print("🗄️  Setting up database for email verification...")
    print("=" * 50)
    
    # Import Django management commands
    from django.core.management import execute_from_command_line
    
    try:
        # Make migrations
        print("1. Creating migrations...")
        execute_from_command_line(['manage.py', 'makemigrations'])
        print("   ✅ Migrations created")
        
        # Apply migrations
        print("\n2. Applying migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        print("   ✅ Migrations applied")
        
        # Check if tables exist
        print("\n3. Verifying database tables...")
        from django.db import connection
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]
        
        required_tables = [
            'APP_emailotp',
            'APP_userprofile',
            'APP_userpredictmodel',
            'auth_user'
        ]
        
        for table in required_tables:
            if table in tables:
                print(f"   ✅ {table} table exists")
            else:
                print(f"   ❌ {table} table missing")
        
        print("\n✅ Database setup completed!")
        
    except Exception as e:
        print(f"❌ Database setup error: {str(e)}")
        return False
    
    return True

def test_model_creation():
    """Test creating models"""
    
    print("\n🧪 Testing model creation...")
    
    try:
        from django.contrib.auth.models import User
        from APP.models import EmailOTP, UserProfile
        
        # Test User creation
        print("1. Testing User model...")
        if User.objects.filter(username='test_db_user').exists():
            User.objects.filter(username='test_db_user').delete()
        
        test_user = User.objects.create_user(
            username='test_db_user',
            email='test@example.com',
            password='testpass123'
        )
        print("   ✅ User model works")
        
        # Test EmailOTP creation
        print("2. Testing EmailOTP model...")
        otp_obj = EmailOTP.create_or_update(test_user, '123456')
        print("   ✅ EmailOTP model works")
        
        # Test UserProfile creation
        print("3. Testing UserProfile model...")
        profile, created = UserProfile.objects.get_or_create(
            user=test_user,
            defaults={'email_notifications': True}
        )
        print("   ✅ UserProfile model works")
        
        # Cleanup
        test_user.delete()
        print("   ✅ Test data cleaned up")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Model test error: {str(e)}")
        return False

def main():
    """Main setup function"""
    
    print("🚀 SkinCare AI - Database Setup for Email System")
    print("=" * 60)
    
    # Setup database
    db_ok = setup_database()
    
    if db_ok:
        # Test models
        models_ok = test_model_creation()
        
        if models_ok:
            print("\n🎉 Database is ready for email verification!")
            print("\n🎯 You can now:")
            print("1. Start Django server: python webapp/manage.py runserver")
            print("2. Register new users with email verification")
            print("3. Send OTP emails from noreply@dharundev.me")
        else:
            print("\n⚠️  Database setup completed but model tests failed")
    else:
        print("\n❌ Database setup failed")
    
    print("=" * 60)

if __name__ == "__main__":
    main()