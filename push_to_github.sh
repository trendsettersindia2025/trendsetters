#!/bin/bash
# Push Trendsetters to GitHub

echo "🚀 Pushing Trendsetters to GitHub..."

# Make sure we're in the right directory
cd /Users/sf/Desktop/Trendsetters

# Add remote (replace YOUR_USERNAME with your GitHub username)
echo "Enter your GitHub username:"
read USERNAME

git remote add origin https://github.com/$USERNAME/trendsetters.git

# Push to GitHub
git branch -M main
git push -u origin main

echo "✅ Code pushed to GitHub!"
echo ""
echo "📍 Next steps:"
echo "1. Go back to the browser"
echo "2. Go to Settings → Pages"
echo "3. Source: Deploy from branch"
echo "4. Branch: main, folder: / (root)"
echo "5. Click Save"
echo ""
echo "Your site will be live at: https://$USERNAME.github.io/trendsetters/"