#!/usr/bin/env python3
"""
Script to run Django migrations for the smart email system
"""

import subprocess
import os

def run_django_migrations():
    """Run Django migrations to add the new field"""
    
    print("🔧 Running Django Migrations for Smart Email System")
    print("=" * 60)
    
    # Change to webapp directory
    original_dir = os.getcwd()
    
    try:
        os.chdir('webapp')
        print("📁 Changed to webapp directory")
        
        # Create migrations
        print("\n1️⃣ Creating migrations...")
        result1 = subprocess.run(['python', 'manage.py', 'makemigrations'], 
                                capture_output=True, text=True)
        
        if result1.returncode == 0:
            print("✅ Migrations created successfully")
            if result1.stdout:
                print(f"   Output: {result1.stdout.strip()}")
        else:
            print("❌ Error creating migrations:")
            print(f"   Error: {result1.stderr}")
            return False
        
        # Apply migrations
        print("\n2️⃣ Applying migrations...")
        result2 = subprocess.run(['python', 'manage.py', 'migrate'], 
                                capture_output=True, text=True)
        
        if result2.returncode == 0:
            print("✅ Migrations applied successfully")
            if result2.stdout:
                print(f"   Output: {result2.stdout.strip()}")
        else:
            print("❌ Error applying migrations:")
            print(f"   Error: {result2.stderr}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error running migrations: {str(e)}")
        return False
    
    finally:
        os.chdir(original_dir)

def show_migration_instructions():
    """Show manual migration instructions"""
    
    print("\n📋 Manual Migration Instructions:")
    print("-" * 40)
    print("If the automatic migration fails, run these commands manually:")
    print()
    print("1️⃣ cd webapp")
    print("2️⃣ python manage.py makemigrations")
    print("3️⃣ python manage.py migrate")
    print()
    print("This will add the 'first_analysis_email_sent' field to UserProfile")

if __name__ == "__main__":
    success = run_django_migrations()
    
    if success:
        print("\n🎉 MIGRATION COMPLETE!")
        print("✅ Database updated with new field")
        print("✅ Smart email system is now active")
        print("✅ Email quota will be preserved")
        
        print("\n📧 Email Behavior Now:")
        print("   • First analysis per user: Email sent ✅")
        print("   • Subsequent analyses: No email ❌")
        print("   • Massive quota savings achieved! 💰")
        
    else:
        show_migration_instructions()
        print("\n⚠️ Please run the manual migration commands above")