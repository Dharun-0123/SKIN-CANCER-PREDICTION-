"""
Email notification utilities for SkinCare AI
"""
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_welcome_email(user):
    """Send welcome email to new users"""
    if not user.email:
        return False
    
    subject = 'Welcome to SkinCare AI!'
    html_message = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background: #0a0a0f; color: #e2e8f0; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background: rgba(26, 26, 36, 0.8); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 10px; padding: 30px;">
                <h1 style="color: #a855f7; text-align: center;">Welcome to SkinCare AI! 🎉</h1>
                <p>Hi <strong>{user.username}</strong>,</p>
                <p>Thank you for joining SkinCare AI! We're excited to have you on board.</p>
                <p>With SkinCare AI, you can:</p>
                <ul>
                    <li>Analyze skin lesions using advanced AI technology</li>
                    <li>Track your analysis history</li>
                    <li>Get detailed information about skin conditions</li>
                    <li>Access your personalized dashboard</li>
                </ul>
                <p style="text-align: center; margin: 30px 0;">
                    <a href="http://127.0.0.1:8000/home/" style="background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%); color: white; padding: 12px 30px; text-decoration: none; border-radius: 8px; display: inline-block;">
                        Get Started
                    </a>
                </p>
                <p>If you have any questions, feel free to reach out to our support team.</p>
                <p>Best regards,<br><strong>The SkinCare AI Team</strong></p>
            </div>
        </body>
    </html>
    """
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending welcome email: {str(e)}")
        return False


def send_prediction_notification(user, prediction_result, image_url):
    """Send email notification after a new prediction"""
    if not user.email or not hasattr(user, 'profile') or not user.profile.email_notifications:
        return False
    
    subject = 'New Skin Analysis Result - SkinCare AI'
    html_message = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background: #0a0a0f; color: #e2e8f0; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background: rgba(26, 26, 36, 0.8); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 10px; padding: 30px;">
                <h1 style="color: #06b6d4; text-align: center;">New Analysis Complete! 🔬</h1>
                <p>Hi <strong>{user.username}</strong>,</p>
                <p>Your skin lesion analysis has been completed.</p>
                <div style="background: rgba(168, 85, 247, 0.1); border-left: 4px solid #a855f7; padding: 15px; margin: 20px 0;">
                    <h3 style="color: #a855f7; margin-top: 0;">Analysis Result:</h3>
                    <p style="font-size: 16px;"><strong>{prediction_result}</strong></p>
                </div>
                <p><strong>Important:</strong> This is an AI-assisted analysis and should not replace professional medical advice. Please consult with a dermatologist for proper diagnosis and treatment.</p>
                <p style="text-align: center; margin: 30px 0;">
                    <a href="http://127.0.0.1:8000/history/" style="background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%); color: white; padding: 12px 30px; text-decoration: none; border-radius: 8px; display: inline-block;">
                        View Full History
                    </a>
                </p>
                <p>Best regards,<br><strong>The SkinCare AI Team</strong></p>
            </div>
        </body>
    </html>
    """
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending prediction notification: {str(e)}")
        return False


def send_profile_update_notification(user):
    """Send email notification when profile is updated"""
    if not user.email or not hasattr(user, 'profile') or not user.profile.email_notifications:
        return False
    
    subject = 'Profile Updated - SkinCare AI'
    html_message = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background: #0a0a0f; color: #e2e8f0; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background: rgba(26, 26, 36, 0.8); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 10px; padding: 30px;">
                <h1 style="color: #3b82f6; text-align: center;">Profile Updated Successfully! ✅</h1>
                <p>Hi <strong>{user.username}</strong>,</p>
                <p>Your profile has been updated successfully.</p>
                <p>If you didn't make this change, please contact our support team immediately.</p>
                <p style="text-align: center; margin: 30px 0;">
                    <a href="http://127.0.0.1:8000/profile/" style="background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%); color: white; padding: 12px 30px; text-decoration: none; border-radius: 8px; display: inline-block;">
                        View Profile
                    </a>
                </p>
                <p>Best regards,<br><strong>The SkinCare AI Team</strong></p>
            </div>
        </body>
    </html>
    """
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending profile update notification: {str(e)}")
        return False
