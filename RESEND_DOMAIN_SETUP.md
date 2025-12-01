# 🌐 Resend Domain Verification Guide

## 📧 Current Limitation

With Resend's **free tier**, you can only send emails to:
- ✅ The email address you signed up with (your verified email)
- ❌ Other email addresses (requires domain verification)

**Your verified email**: `givemeanythingu@gmail.com`

---

## 🎯 Two Options to Send to Any Email

### Option 1: Verify Your Own Domain (Recommended for Production)

If you own a domain (e.g., `yourdomain.com`), you can verify it with Resend:

#### Step 1: Go to Resend Dashboard
1. Visit https://resend.com/domains
2. Click "Add Domain"

#### Step 2: Add Your Domain
1. Enter your domain name (e.g., `yourdomain.com`)
2. Click "Add"

#### Step 3: Add DNS Records
Resend will provide DNS records to add to your domain:

**Required Records:**
```
Type: TXT
Name: @
Value: resend-verification=xxxxx

Type: MX
Name: @
Value: feedback-smtp.resend.com
Priority: 10

Type: TXT
Name: @
Value: v=spf1 include:_spf.resend.com ~all

Type: TXT
Name: resend._domainkey
Value: [DKIM key provided by Resend]
```

#### Step 4: Wait for Verification
- DNS propagation can take 5-60 minutes
- Resend will automatically verify once DNS is updated
- You'll receive an email confirmation

#### Step 5: Update Django Settings
```python
# In webapp/PROJECT/settings.py
DEFAULT_FROM_EMAIL = 'SkinCare AI <noreply@yourdomain.com>'
```

---

### Option 2: Use Testing Mode (For Development)

For testing during development, you have two approaches:

#### A. Test with Your Own Email Only
Keep the current setup and only test with `givemeanythingu@gmail.com`:

```python
# No changes needed - current setup works!
# Just register with givemeanythingu@gmail.com for testing
```

#### B. Use Console Backend (No Real Emails)
For local testing without sending real emails:

```python
# In webapp/PROJECT/settings.py
# Comment out SMTP and use console backend:

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.resend.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'resend'
    EMAIL_HOST_PASSWORD = os.environ.get('RESEND_API_KEY', 're_WBFKPgfG_Kn9Cy8SmSqwh1iePuES8YWJk')
```

With console backend, emails will print to your terminal instead of sending.

---

## 🚀 Quick Start for Testing NOW

### For Immediate Testing (No Domain Required):

**Option A: Test with Your Email**
1. Go to `http://localhost:8000/register/`
2. Register with email: `givemeanythingu@gmail.com`
3. Check your Gmail inbox for OTP
4. Enter OTP and verify

**Option B: Use Console Backend**
1. Update settings to use console backend (see above)
2. Register with any email
3. Check terminal output for OTP
4. Copy OTP from terminal and verify

---

## 📊 Resend Pricing Tiers

| Tier | Price | Emails/Month | Domains | Recipients |
|------|-------|--------------|---------|------------|
| **Free** | $0 | 100 | 0 | Your email only |
| **Pro** | $20 | 50,000 | Unlimited | Anyone |
| **Business** | Custom | Custom | Unlimited | Anyone |

---

## 🔧 Recommended Setup Path

### For Development/Testing:
```python
# Use console backend - prints emails to terminal
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### For Production:
1. Buy a domain (e.g., from Namecheap, GoDaddy)
2. Verify domain with Resend
3. Upgrade to Resend Pro ($20/month)
4. Use SMTP backend with your domain

---

## 💡 Alternative Email Services

If you don't want to verify a domain, consider these alternatives:

### 1. Gmail SMTP (Free, but limited)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-gmail@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Not regular password!
```
- Limit: 500 emails/day
- Requires App Password (not regular password)
- Can send to anyone

### 2. SendGrid (Free tier: 100 emails/day)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
```

### 3. Mailgun (Free tier: 5,000 emails/month)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'postmaster@your-domain.mailgun.org'
EMAIL_HOST_PASSWORD = 'your-mailgun-password'
```

---

## 🎯 My Recommendation

**For Right Now (Testing):**
```python
# Use console backend - easiest for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

**For Production Later:**
1. Get a domain
2. Verify with Resend
3. Upgrade to Resend Pro
4. Switch back to SMTP backend

---

## 📝 Quick Switch to Console Backend

Want to test right now without domain verification? Run this:

```bash
# I can update your settings.py to use console backend
# This will print OTPs to terminal instead of sending emails
```

Let me know if you want me to:
1. ✅ Switch to console backend for testing
2. ✅ Set up Gmail SMTP instead
3. ✅ Keep Resend and test with your email only
4. ✅ Help you verify a domain with Resend

---

**Current Status**: ✅ Resend configured, but limited to `givemeanythingu@gmail.com`  
**Next Step**: Choose one of the options above!
