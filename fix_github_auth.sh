#!/bin/bash

echo "Fixing GitHub authentication..."

# Clear all stored credentials
echo "Clearing old credentials..."
git config --global --unset credential.helper
git config --system --unset credential.helper
git config --unset credential.helper

# Set up fresh credential helper
git config --global credential.helper osxkeychain

# Clear the keychain
security delete-internet-password -s github.com 2>/dev/null || true

echo "Old credentials cleared!"
echo ""
echo "Now when you push, it will ask for:"
echo "Username: trendsettersindia2025"
echo "Password: [Your GitHub Personal Access Token or Password]"
echo ""
echo "Attempting to push now..."

git push origin main