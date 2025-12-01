"""
OTP Utility Functions for Email Verification
"""
import random
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailOTP


def generate_otp():
    """Generate a random 6-digit OTP"""
    return str(random.randint(100000, 999999))


def send_otp_email(user):
    """
    Generate OTP, save to database, and send to user's email
    
    Args:
        user: Django User object
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Generate OTP
        otp = generate_otp()
        
        # Save to database
        EmailOTP.create_or_update(user, otp)
        
        # Email subject and message
        subject = 'Verify Your Email - SkinCare AI'
        message = f"""
Hello {user.username},

Thank you for registering with SkinCare AI!

Your email verification code is: {otp}

This code will expire in {getattr(settings, 'OTP_EXPIRY_MINUTES', 10)} minutes.

If you didn't request this code, please ignore this email.

Best regards,
SkinCare AI Team
        """
        
        html_message = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
        .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
        .otp-box {{ background: white; border: 2px solid #a855f7; border-radius: 10px; padding: 20px; text-align: center; margin: 20px 0; }}
        .otp-code {{ font-size: 32px; font-weight: bold; color: #a855f7; letter-spacing: 5px; }}
        .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔐 Email Verification</h1>
        </div>
        <div class="content">
            <p>Hello <strong>{user.username}</strong>,</p>
            <p>Thank you for registering with <strong>SkinCare AI</strong>!</p>
            <p>Your email verification code is:</p>
            <div class="otp-box">
                <div class="otp-code">{otp}</div>
            </div>
            <p>This code will expire in <strong>{getattr(settings, 'OTP_EXPIRY_MINUTES', 10)} minutes</strong>.</p>
            <p>If you didn't request this code, please ignore this email.</p>
            <p>Best regards,<br><strong>SkinCare AI Team</strong></p>
        </div>
        <div class="footer">
            <p>This is an automated message, please do not reply.</p>
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
            recipient_list=[user.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        return True, 'OTP sent successfully'
        
    except Exception as e:
        return False, f'Failed to send OTP: {str(e)}'


def verify_otp(user, entered_otp):
    """
    Verify the OTP entered by user
    
    Args:
        user: Django User object
        entered_otp: str - OTP entered by user
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        otp_obj = EmailOTP.objects.get(user=user)
        
        # Check if already verified
        if otp_obj.is_verified:
            return False, 'Email already verified'
        
        # Check if expired
        if otp_obj.is_expired():
            return False, 'OTP has expired. Please request a new one.'
        
        # Check if OTP matches
        if otp_obj.otp != entered_otp:
            return False, 'Invalid OTP. Please try again.'
        
        # Mark as verified
        otp_obj.is_verified = True
        otp_obj.save()
        
        # Update user profile if exists
        if hasattr(user, 'profile'):
            user.profile.email_verified = True
            user.profile.save()
        
        return True, 'Email verified successfully!'
        
    except EmailOTP.DoesNotExist:
        return False, 'No OTP found. Please request a new one.'
    except Exception as e:
        return False, f'Verification failed: {str(e)}'


def resend_otp(user):
    """
    Resend OTP to user
    
    Args:
        user: Django User object
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Check if already verified
        if hasattr(user, 'email_otp') and user.email_otp.is_verified:
            return False, 'Email already verified'
        
        # Send new OTP
        return send_otp_email(user)
        
    except Exception as e:
        return False, f'Failed to resend OTP: {str(e)}'
