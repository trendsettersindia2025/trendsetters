#!/bin/bash
# Create a zip file of all HTML files for easy upload

echo "📦 Creating zip file for upload..."
cd /Users/sf/Desktop/Trendsetters

# Create zip with all website files
zip -r trendsetters-website.zip *.html

echo "✅ Created trendsetters-website.zip"
echo ""
echo "📤 Now do the following:"
echo "1. Go to: https://github.com/trendsettersindia2025/trendsetters"
echo "2. Click 'Add file' > 'Upload files'"
echo "3. Upload the trendsetters-website.zip file"
echo "4. After upload, click on the zip file and extract it"
echo ""
echo "Or upload these files individually:"
ls -la *.html

# Open the upload page
open https://github.com/trendsettersindia2025/trendsetters/upload/main