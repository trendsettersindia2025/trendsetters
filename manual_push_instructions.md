# Manual Push Instructions

Since there's an authentication issue, here's how to push your code manually:

## Option 1: Use GitHub's Web Upload (Easiest)

1. Go to: https://github.com/trendsettersindia2025/trendsetters
2. Click "uploading an existing file" or "Upload files" button
3. Drag and drop these files:
   - index.html
   - about.html
   - services.html
   - portfolio.html
   - contact.html
4. Write commit message: "Initial commit - Trendsetters website"
5. Click "Commit changes"

## Option 2: Use Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Generate new token (classic)
3. Select scopes: repo (all)
4. Copy the token
5. Run:
```bash
cd /Users/sf/Desktop/Trendsetters
git push https://YOUR_TOKEN@github.com/trendsettersindia2025/trendsetters.git main
```

## Option 3: Fix Git Credentials

Run these commands:
```bash
# Clear old credentials
git config --global --unset credential.helper

# Set up new credentials
git config --global user.name "trendsettersindia2025"
git config --global user.email "your-email@example.com"

# Push with username/password prompt
git push -u origin main
```

## After Pushing, Enable GitHub Pages:

1. Go to: https://github.com/trendsettersindia2025/trendsetters/settings/pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: / (root)
5. Click Save

Your site will be live at: https://trendsettersindia2025.github.io/trendsetters/