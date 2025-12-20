"""
Password Reset Utility Functions
"""
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import PasswordResetOTP


def generate_otp():
    """Generate a random 6-digit OTP"""
    return str(random.randint(100000, 999999))


def send_password_reset_otp(email):
    """
    Generate OTP, save to database, and send password reset email
    
    Args:
        email: User's email address
        
    Returns:
        tuple: (success: bool, message: str, user: User or None)
    """
    try:
        # Check if user exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return False, 'No account found with this email address.', None
        
        # Generate OTP
        otp = generate_otp()
        
        # Save to database
        PasswordResetOTP.create_or_update(user, otp)
        
        # Email subject and message
        subject = 'Password Reset - SkinCare AI'
        message = f"""
Hello {user.username},

You have requested to reset your password for SkinCare AI.

Your password reset code is: {otp}

This code will expire in 15 minutes.

If you didn't request this password reset, please ignore this email and your password will remain unchanged.

For security reasons, please do not share this code with anyone.

Best regards,
SkinCare AI Team
        """
        
        html_message = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; background: #0a0a0f; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
        .content {{ background: rgba(26, 26, 36, 0.9); color: #e2e8f0; padding: 30px; border-radius: 0 0 10px 10px; border: 1px solid rgba(168, 85, 247, 0.3); }}
        .otp-box {{ background: rgba(168, 85, 247, 0.1); border: 2px solid #a855f7; border-radius: 10px; padding: 20px; text-align: center; margin: 20px 0; }}
        .otp-code {{ font-size: 32px; font-weight: bold; color: #a855f7; letter-spacing: 5px; }}
        .warning {{ background: rgba(239, 68, 68, 0.1); border-left: 4px solid #ef4444; padding: 15px; margin: 20px 0; color: #fca5a5; }}
        .footer {{ text-align: center; margin-top: 20px; color: #94a3b8; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔐 Password Reset Request</h1>
        </div>
        <div class="content">
            <p>Hello <strong>{user.username}</strong>,</p>
            <p>You have requested to reset your password for <strong>SkinCare AI</strong>.</p>
            <p>Your password reset code is:</p>
            <div class="otp-box">
                <div class="otp-code">{otp}</div>
            </div>
            <p>This code will expire in <strong>15 minutes</strong>.</p>
            <div class="warning">
                <p><strong>⚠️ Security Notice:</strong></p>
                <p>• If you didn't request this password reset, please ignore this email</p>
                <p>• Do not share this code with anyone</p>
                <p>• This code can only be used once</p>
            </div>
            <p>Best regards,<br><strong>SkinCare AI Team</strong></p>
        </div>
        <div class="footer">
            <p>This is an automated message, please do not reply.</p>
            <p>© 2024 SkinCare AI - Advanced Skin Lesion Classification</p>
        </div>
    </div>
</body>
</html>
        """
        
        # Send email
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=html_message,
            fail_silently=False,
        )
        
        return True, 'Password reset code sent to your email.', user
        
    except Exception as e:
        return False, f'Failed to send password reset email: {str(e)}', None


def verify_password_reset_otp(user, entered_otp):
    """
    Verify the password reset OTP entered by user
    
    Args:
        user: Django User object
        entered_otp: str - OTP entered by user
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        otp_obj = PasswordResetOTP.objects.get(user=user)
        
        # Check if already used
        if otp_obj.is_used:
            return False, 'This password reset code has already been used.'
        
        # Check if expired
        if otp_obj.is_expired():
            return False, 'Password reset code has expired. Please request a new one.'
        
        # Check if OTP matches
        if otp_obj.otp != entered_otp:
            return False, 'Invalid password reset code. Please try again.'
        
        # Mark as used (don't delete yet, keep for audit)
        otp_obj.is_used = True
        otp_obj.save()
        
        return True, 'Password reset code verified successfully!'
        
    except PasswordResetOTP.DoesNotExist:
        return False, 'No password reset request found. Please request a new code.'
    except Exception as e:
        return False, f'Verification failed: {str(e)}'


def cleanup_expired_otps():
    """
    Cleanup expired password reset OTPs (can be run as a periodic task)
    """
    from django.utils import timezone
    from datetime import timedelta
    
    # Delete OTPs older than 24 hours
    cutoff_time = timezone.now() - timedelta(hours=24)
    expired_count = PasswordResetOTP.objects.filter(created_at__lt=cutoff_time).count()
    PasswordResetOTP.objects.filter(created_at__lt=cutoff_time).delete()
    
    return expired_count