# GitHub Personal Access Token Setup

## Steps to Create Token:

1. Go to GitHub.com and click your profile picture → Settings
2. Scroll down to "Developer settings" (at the bottom of left sidebar)
3. Click "Personal access tokens" → "Tokens (classic)"
4. Click "Generate new token" → "Generate new token (classic)"
5. Give it a name like "Trendsetters CLI Access"
6. Set expiration (90 days is fine)
7. Check these permissions:
   - ✅ repo (all)
   - ✅ workflow
   - ✅ admin:repo_hook
8. Click "Generate token" at bottom
9. COPY THE TOKEN IMMEDIATELY (you won't see it again!)

## Configure Git to Use Token:

Once you have the token, run this command:
```bash
git remote set-url origin https://trendsettersindia2025:YOUR_TOKEN_HERE@github.com/trendsettersindia2025/trendsetters.git
```

Replace YOUR_TOKEN_HERE with your actual token.

## Alternative: Use GitHub CLI
```bash
brew install gh
gh auth login
```
Then follow the prompts to authenticate via browser.