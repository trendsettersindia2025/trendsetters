#!/bin/bash
# Quick deployment script for Trendsetters

echo "🚀 Deploying Trendsetters to GitHub..."

# Add all changes
git add .

# Commit with timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
git commit -m "Update: $TIMESTAMP"

# Push to GitHub
git push origin main

echo "✅ Deployment complete!"
echo "🌐 Your site will be updated at: https://[YOUR_USERNAME].github.io/trendsetters/"
echo "   (Replace [YOUR_USERNAME] with your GitHub username)"