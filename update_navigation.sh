#!/bin/bash
# Update navigation on GitHub

echo "🔄 Updating navigation on Trendsetters website..."
echo "=============================================="

cd /Users/sf/Desktop/Trendsetters

# Add and commit the updated index.html
git add index.html
git commit -m "Update navigation: Connect all pages together"

# Push to GitHub
git push origin main

echo ""
echo "✅ Navigation updated!"
echo ""
echo "The homepage now includes links to:"
echo "  • Home (index.html)"
echo "  • About (about.html)" 
echo "  • Services (services.html)"
echo "  • Portfolio (portfolio.html)"
echo "  • Contact (contact.html)"
echo ""
echo "🌐 Your updated site will be live in a few minutes at:"
echo "   https://trendsettersindia.com"