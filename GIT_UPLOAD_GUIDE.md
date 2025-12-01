# 🚀 Git Upload Guide - Secure Deployment

## ⚠️ IMPORTANT: Security First!

Your API keys have been moved to `.env` file which is **NOT** uploaded to Git.

---

## 📋 Pre-Upload Checklist

✅ API keys removed from code  
✅ `.env` file created (contains your keys)  
✅ `.env.example` created (template for others)  
✅ `.gitignore` configured  
✅ Sensitive data protected  

---

## 🔧 Step 1: Initialize Git (if not already done)

```bash
git init
```

---

## 📦 Step 2: Add Files to Git

```bash
# Add all files (respects .gitignore)
git add .

# Check what will be committed
git status
```

**Verify that `.env` is NOT listed!** (should show as ignored)

---

## 💬 Step 3: Create First Commit

```bash
git commit -m "Initial commit: SkinCare AI with email verification"
```

---

## 🌐 Step 4: Connect to GitHub

### Option A: New Repository
1. Go to https://github.com/new
2. Create a new repository (e.g., "skincare-ai")
3. **Don't** initialize with README (you already have one)
4. Copy the repository URL

### Option B: Existing Repository
Use your existing repository URL

---

## 🔗 Step 5: Add Remote and Push

```bash
# Add remote (replace with your URL)
git remote add origin https://github.com/yourusername/skincare-ai.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## 🔐 Step 6: Setup Environment Variables on Server

When deploying, you'll need to set environment variables:

### For Local Development:
```bash
# Windows (PowerShell)
$env:RESEND_API_KEY="re_WBFKPgfG_Kn9Cy8SmSqwh1iePuES8YWJk"

# Windows (CMD)
set RESEND_API_KEY=re_WBFKPgfG_Kn9Cy8SmSqwh1iePuES8YWJk

# Linux/Mac
export RESEND_API_KEY=re_WBFKPgfG_Kn9Cy8SmSqwh1iePuES8YWJk
```

### For Production (Heroku):
```bash
heroku config:set RESEND_API_KEY=re_WBFKPgfG_Kn9Cy8SmSqwh1iePuES8YWJk
heroku config:set OPENAI_API_KEY=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
```

### For Production (Railway/Render):
Add environment variables in the dashboard:
- `RESEND_API_KEY` = `re_WBFKPgfG_Kn9Cy8SmSqwh1iePuES8YWJk`
- `OPENAI_API_KEY` = `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`

---

## 📝 Step 7: Update README for Others

Add this section to your README.md:

```markdown
## 🔧 Setup Instructions

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/yourusername/skincare-ai.git
   cd skincare-ai
   \`\`\`

2. Create virtual environment:
   \`\`\`bash
   python -m venv venv
   venv\\Scripts\\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   \`\`\`

3. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Copy `.env.example` to `.env` and add your API keys:
   \`\`\`bash
   copy .env.example .env  # Windows
   cp .env.example .env    # Linux/Mac
   \`\`\`

5. Edit `.env` and add your keys:
   - Get Resend API key from: https://resend.com
   - Get Perplexity API key from: https://www.perplexity.ai

6. Run migrations:
   \`\`\`bash
   cd webapp
   python manage.py migrate
   \`\`\`

7. Start server:
   \`\`\`bash
   python manage.py runserver
   \`\`\`
```

---

## 🔄 Future Updates

When making changes:

```bash
# Check status
git status

# Add changes
git add .

# Commit with message
git commit -m "Add new feature"

# Push to GitHub
git push
```

---

## ⚠️ Security Reminders

1. **NEVER** commit `.env` file
2. **NEVER** hardcode API keys in code
3. **ALWAYS** use environment variables
4. **ALWAYS** check `git status` before committing
5. **ROTATE** API keys if accidentally exposed

---

## 🆘 If You Accidentally Committed API Keys

```bash
# Remove from last commit
git reset HEAD~1

# Remove file from Git but keep locally
git rm --cached .env

# Force push (if already pushed to GitHub)
git push -f origin main

# IMPORTANT: Rotate your API keys immediately!
```

Then:
1. Go to Resend dashboard and regenerate API key
2. Go to Perplexity dashboard and regenerate API key
3. Update your `.env` file with new keys

---

## ✅ Verification

Before pushing, verify:

```bash
# This should NOT show .env
git status

# This should show .env is ignored
git check-ignore .env
```

If `.env` appears in `git status`, it means it's not being ignored!

---

**Status**: 🔒 Secure & Ready to Upload  
**Last Updated**: Current Session
