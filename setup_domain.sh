#!/bin/bash
# Quick domain setup script

echo "🌐 Setting up trendsettersindia.com"
echo "===================================="

# Check if CNAME exists in repo
echo "Checking for CNAME file..."
if curl -s https://api.github.com/repos/trendsettersindia2025/trendsetters/contents/CNAME | grep -q "trendsettersindia.com"; then
    echo "✅ CNAME file already exists!"
else
    echo "❌ CNAME file not found"
    echo ""
    echo "Please add CNAME file:"
    echo "1. Go to: https://github.com/trendsettersindia2025/trendsetters"
    echo "2. Click 'Create new file'"
    echo "3. Name: CNAME"
    echo "4. Content: trendsettersindia.com"
    echo "5. Commit the file"
fi

echo ""
echo "📝 DNS Configuration for Namecheap:"
echo ""
echo "Add these A records:"
echo "  Type: A, Host: @, Value: 185.199.108.153"
echo "  Type: A, Host: @, Value: 185.199.109.153"
echo "  Type: A, Host: @, Value: 185.199.110.153"
echo "  Type: A, Host: @, Value: 185.199.111.153"
echo ""
echo "Add CNAME record:"
echo "  Type: CNAME, Host: www, Value: trendsettersindia2025.github.io"
echo ""
echo "🔗 Links to open:"
echo "  GitHub: https://github.com/trendsettersindia2025/trendsetters/new/main"
echo "  Namecheap: https://ap.www.namecheap.com/domains/domaincontrolpanel/trendsettersindia.com/advancedns"
echo "  GitHub Pages: https://github.com/trendsettersindia2025/trendsetters/settings/pages"

# Open all necessary pages
open "https://github.com/trendsettersindia2025/trendsetters/new/main"
sleep 2
open "https://ap.www.namecheap.com/domains/domaincontrolpanel/trendsettersindia.com/advancedns"
sleep 2
open "https://github.com/trendsettersindia2025/trendsetters/settings/pages"