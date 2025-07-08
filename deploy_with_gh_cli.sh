#!/bin/bash
# Fully automated deployment using GitHub CLI

echo "🚀 Automated Trendsetters Deployment with GitHub CLI"
echo "===================================================="

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI not found. Installing..."
    brew install gh
fi

# Check if logged in to GitHub CLI
if ! gh auth status &> /dev/null; then
    echo "📝 Please login to GitHub:"
    gh auth login
fi

cd /Users/sf/Desktop/Trendsetters

# Get GitHub username
USERNAME=$(gh api user --jq .login)
echo "👤 GitHub Username: $USERNAME"

# Create repository on GitHub
echo ""
echo "📦 Creating repository on GitHub..."
gh repo create trendsetters --public --description "Trendsetters website" --source=. --remote=origin --push

if [ $? -eq 0 ]; then
    echo "✅ Repository created and code pushed!"
else
    echo "⚠️  Repository might already exist. Trying to push..."
    git remote add origin https://github.com/$USERNAME/trendsetters.git 2>/dev/null
    git push -u origin main --force
fi

# Enable GitHub Pages
echo ""
echo "🌐 Enabling GitHub Pages..."
gh api repos/$USERNAME/trendsetters/pages \
  --method POST \
  --field source='{"branch":"main","path":"/"}' \
  2>/dev/null

if [ $? -eq 0 ]; then
    echo "✅ GitHub Pages enabled!"
else
    echo "⚠️  GitHub Pages might already be enabled"
fi

echo ""
echo "🎉 Deployment Complete!"
echo ""
echo "📍 Repository: https://github.com/$USERNAME/trendsetters"
echo "🌐 Website: https://$USERNAME.github.io/trendsetters/"
echo ""
echo "⏰ Your site will be live in 5-10 minutes!"

# Open the repository in browser
echo ""
echo "Opening your repository in browser..."
gh repo view --web