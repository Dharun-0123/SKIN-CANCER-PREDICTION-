# 📧 Email Notification Setup Guide

Quick guide to configure email notifications for SkinCare AI.

---

## 🚀 Quick Start

### Development (Current Setup)
Emails print to console - no configuration needed!

```bash
# Start server
cd webapp
python manage.py runserver

# Register a new user
# Check console for welcome email output
```

---

## 📮 Production Setup

### Option 1: Gmail (Recommended for Testing)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to Google Account → Security
   - 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Copy the 16-character password

3. **Update settings.py**:
```python
# Comment out console backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Add SMTP configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-char-app-password'
DEFAULT_FROM_EMAIL = 'SkinCare AI <your-email@gmail.com>'
```

### Option 2: SendGrid (Recommended for Production)

1. **Sign up** at https://sendgrid.com (free tier: 100 emails/day)
2. **Create API Key**:
   - Settings → API Keys → Create API Key
   - Full Access
   - Copy the key

3. **Update settings.py**:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
DEFAULT_FROM_EMAIL = 'SkinCare AI <noreply@yourdomain.com>'
```

### Option 3: AWS SES (Enterprise)

```python
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'
```

---

## 🧪 Testing Emails

### Test in Console
```bash
cd webapp
python manage.py shell
```

```python
from django.contrib.auth.models import User
from APP.email_utils import send_welcome_email

# Get a user
user = User.objects.first()

# Send test email
send_welcome_email(user)
```

### Test Registration Flow
1. Go to http://127.0.0.1:8000/register/
2. Create a new account
3. Check console/inbox for welcome email

### Test Prediction Notification
1. Login to your account
2. Go to Analyze page
3. Upload an image
4. Check console/inbox for notification

---

## 🔒 Security Best Practices

### Environment Variables (Recommended)
```python
# settings.py
import os

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

```bash
# .env file (add to .gitignore!)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Django-environ Package
```bash
pip install django-environ
```

```python
# settings.py
import environ

env = environ.Env()
environ.Env.read_env()

EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
```

---

## 📊 Email Limits

### Gmail
- 500 emails/day (free)
- 2000 emails/day (Google Workspace)

### SendGrid
- 100 emails/day (free)
- 40,000 emails/month (Essentials: $15/mo)

### AWS SES
- 62,000 emails/month (free tier)
- $0.10 per 1,000 emails after

---

## 🐛 Troubleshooting

### Emails Not Sending

**Check 1: Console Output**
```bash
# Look for error messages in terminal
```

**Check 2: Email Settings**
```python
# In Django shell
from django.core.mail import send_mail

send_mail(
    'Test Subject',
    'Test message',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

**Check 3: Gmail Security**
- Enable "Less secure app access" (if not using App Password)
- Check for security alerts in Gmail

**Check 4: Firewall**
- Ensure port 587 is open
- Check corporate firewall settings

### Common Errors

**SMTPAuthenticationError**
- Wrong username/password
- Need App Password for Gmail
- 2FA not enabled

**SMTPServerDisconnected**
- Wrong host/port
- Firewall blocking connection

**SMTPRecipientsRefused**
- Invalid recipient email
- Email doesn't exist

---

## 📝 Customizing Emails

### Edit Templates
File: `webapp/APP/email_utils.py`

```python
def send_welcome_email(user):
    subject = 'Your Custom Subject'
    html_message = """
    <html>
        <body>
            <h1>Custom HTML</h1>
            <p>Your content here</p>
        </body>
    </html>
    """
    # ... rest of function
```

### Add New Notification Types
```python
def send_custom_notification(user, data):
    subject = 'Custom Notification'
    html_message = f"""
    <html>
        <body>
            <h1>Hello {user.username}!</h1>
            <p>{data}</p>
        </body>
    </html>
    """
    
    send_mail(
        subject,
        strip_tags(html_message),
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
    )
```

---

## ✅ Checklist

- [ ] Choose email provider
- [ ] Create account/API key
- [ ] Update settings.py
- [ ] Test email sending
- [ ] Verify emails received
- [ ] Set up environment variables
- [ ] Add .env to .gitignore
- [ ] Document for team
- [ ] Monitor email limits
- [ ] Set up error alerts

---

## 🎯 Quick Commands

```bash
# Test email in shell
python manage.py shell
>>> from APP.email_utils import send_welcome_email
>>> from django.contrib.auth.models import User
>>> user = User.objects.first()
>>> send_welcome_email(user)

# Check email settings
python manage.py shell
>>> from django.conf import settings
>>> print(settings.EMAIL_BACKEND)
>>> print(settings.EMAIL_HOST)

# Create test user
python manage.py createsuperuser
```

---

**Status**: Ready to configure! Choose your email provider and follow the steps above.
