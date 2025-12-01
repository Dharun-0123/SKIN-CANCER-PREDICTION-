# 🔧 DermaGenie Troubleshooting Guide

**Common Issues and Solutions**

---

## ⚠️ Rate Limit Exceeded Error

### Error Message:
```
"Rate limit exceeded. Please try again in a moment."
```

### What This Means:
Your OpenAI account has reached its usage limit. This can happen for several reasons:

---

## 🔍 Possible Causes & Solutions

### 1. Free Tier Limitations
**Issue**: Free OpenAI accounts have very limited usage

**Solution**:
- OpenAI free tier has strict limits (often just a few requests)
- You need to add credits to your account
- Go to: https://platform.openai.com/account/billing
- Add at least $5-10 to start using the API

### 2. API Key Issues
**Issue**: API key might be invalid or expired

**Solution**:
1. Go to: https://platform.openai.com/api-keys
2. Check if your key is active
3. Create a new API key if needed
4. Update the key in `webapp/PROJECT/settings.py`

### 3. Usage Quota Exceeded
**Issue**: You've used all your credits

**Solution**:
1. Check usage: https://platform.openai.com/usage
2. Add more credits to your account
3. Set up billing: https://platform.openai.com/account/billing

### 4. Rate Limiting (Too Many Requests)
**Issue**: Sending too many requests too quickly

**Solution**:
- Wait 1-2 minutes before trying again
- OpenAI has rate limits even for paid accounts
- Implement request throttling if needed

---

## 💰 OpenAI Account Setup

### Step 1: Create Account
1. Go to: https://platform.openai.com/signup
2. Sign up with email
3. Verify your email

### Step 2: Add Payment Method
1. Go to: https://platform.openai.com/account/billing
2. Click "Add payment method"
3. Enter credit card details
4. Add credits ($5 minimum recommended)

### Step 3: Get API Key
1. Go to: https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-proj-...`)
4. Save it securely (you can't see it again!)

### Step 4: Configure in App
1. Open `webapp/PROJECT/settings.py`
2. Find the line: `OPENAI_API_KEY = '...'`
3. Replace with your new key
4. Restart the server

---

## 🔑 API Key Checklist

### Valid API Key Format:
```
sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### Check Your Key:
- ✅ Starts with `sk-proj-` or `sk-`
- ✅ Is about 100+ characters long
- ✅ Contains letters and numbers
- ✅ No spaces or line breaks
- ✅ Copied completely

### Common Mistakes:
- ❌ Key is truncated (incomplete)
- ❌ Extra spaces at start/end
- ❌ Line breaks in the middle
- ❌ Using old/revoked key
- ❌ Key from wrong account

---

## 💳 Billing & Credits

### Check Your Balance:
1. Go to: https://platform.openai.com/usage
2. View current usage
3. Check remaining credits
4. See usage history

### Add Credits:
1. Go to: https://platform.openai.com/account/billing
2. Click "Add to credit balance"
3. Choose amount ($5, $10, $20, etc.)
4. Complete payment

### Pricing (GPT-3.5-turbo):
- **Input**: $0.0015 per 1K tokens
- **Output**: $0.002 per 1K tokens
- **Average conversation**: $0.001-0.003
- **$5 credit**: ~1,500-5,000 conversations

---

## 🧪 Test Your API Key

### Method 1: Simple Test
```python
# In Django shell
python manage.py shell

from APP.ai_assistant import get_dermagenie_response
response = get_dermagenie_response("Hello, test message")
print(response)
```

### Method 2: Direct OpenAI Test
```python
import openai

openai.api_key = 'your-key-here'

try:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=50
    )
    print("✅ API key works!")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"❌ Error: {e}")
```

---

## 🔄 Alternative Solutions

### Option 1: Use Different Model
If you have access to GPT-4 but not GPT-3.5-turbo:

Edit `webapp/APP/ai_assistant.py`:
```python
# Change line ~80
model="gpt-4",  # instead of "gpt-3.5-turbo"
```

### Option 2: Implement Fallback
Add a fallback response when API fails:

```python
# In ai_assistant.py
if not response['success']:
    return {
        'success': True,
        'formatted_html': '''
            <p class="ai-paragraph">
                I'm currently unable to connect to the AI service. 
                Here are some general skin care tips:
            </p>
            <ul class="ai-list">
                <li>Always use sunscreen (SPF 30+)</li>
                <li>Check your skin regularly for changes</li>
                <li>Consult a dermatologist for concerns</li>
            </ul>
        '''
    }
```

### Option 3: Use Mock Responses (Testing)
For testing without API calls:

```python
# In settings.py
USE_MOCK_AI = True  # Set to False for production

# In ai_assistant.py
if settings.USE_MOCK_AI:
    return {
        'success': True,
        'formatted_html': '<p>Mock response for testing</p>'
    }
```

---

## 📊 Monitor Usage

### Check Usage Dashboard:
https://platform.openai.com/usage

### What to Monitor:
- **Daily usage** - Requests per day
- **Token usage** - Input/output tokens
- **Cost** - Daily/monthly spending
- **Rate limits** - Requests per minute

### Set Limits:
1. Go to: https://platform.openai.com/account/limits
2. Set monthly spending limit
3. Get email alerts
4. Prevent unexpected charges

---

## 🚨 Error Messages Explained

### "Invalid API key"
- Key is wrong or expired
- Get new key from OpenAI dashboard

### "Rate limit exceeded"
- Too many requests or no credits
- Wait or add credits

### "Insufficient quota"
- No credits remaining
- Add credits to account

### "Model not found"
- Model name is wrong
- Use "gpt-3.5-turbo" or "gpt-4"

### "Connection error"
- Internet connection issue
- Check network and try again

---

## ✅ Quick Fixes

### Fix 1: Restart Server
```bash
# Stop server (Ctrl+C)
# Start again
cd webapp
python manage.py runserver
```

### Fix 2: Clear Cache
```bash
# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +

# Or on Windows
del /s /q __pycache__
```

### Fix 3: Reinstall OpenAI
```bash
pip uninstall openai
pip install openai
```

### Fix 4: Check Settings
```python
# In Django shell
python manage.py shell

from django.conf import settings
print(settings.OPENAI_API_KEY)
# Should print your key
```

---

## 🆘 Still Not Working?

### Checklist:
- [ ] OpenAI account created
- [ ] Payment method added
- [ ] Credits added ($5+)
- [ ] API key generated
- [ ] Key copied completely
- [ ] Key added to settings.py
- [ ] Server restarted
- [ ] Internet connection working
- [ ] No firewall blocking OpenAI

### Get Help:
1. **OpenAI Support**: https://help.openai.com/
2. **Check Status**: https://status.openai.com/
3. **Documentation**: https://platform.openai.com/docs
4. **Community**: https://community.openai.com/

---

## 💡 Pro Tips

### Tip 1: Use Environment Variables
Instead of hardcoding the key:

```python
# In settings.py
import os
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Set in terminal
export OPENAI_API_KEY='your-key-here'
```

### Tip 2: Implement Caching
Cache common responses to save API calls:

```python
# Cache frequently asked questions
CACHED_RESPONSES = {
    "what is skin cancer": "Cached response...",
    # Add more
}
```

### Tip 3: Add Rate Limiting
Limit requests per user:

```python
# In views.py
from django.core.cache import cache

def check_rate_limit(user):
    key = f'dermagenie_rate_{user.id}'
    count = cache.get(key, 0)
    if count >= 10:  # 10 requests per hour
        return False
    cache.set(key, count + 1, 3600)  # 1 hour
    return True
```

---

## 📝 Summary

### Most Common Issue:
**No credits in OpenAI account**

### Quick Solution:
1. Go to: https://platform.openai.com/account/billing
2. Add $5-10 credits
3. Wait 1-2 minutes
4. Try DermaGenie again

### Prevention:
- Set up billing alerts
- Monitor usage regularly
- Set monthly spending limits
- Keep credits topped up

---

**Need more help? Check the full documentation in `DERMAGENIE_AI_FEATURE.md`**

**Status**: Ready to troubleshoot! 🔧
