# Complete Setup Guide: GitHub + Namecheap Domain

## What You Need to Open:

1. **GitHub** - https://github.com
2. **Namecheap** - https://namecheap.com
3. **Gmail** - https://gmail.com (for verification emails)

## Step-by-Step Process:

### 1. GitHub Setup (First Tab)
1. Log in to GitHub
2. Create new repository named `trendsetters`
3. Keep this tab open - you'll need it for Pages settings

### 2. Push Code to GitHub (Terminal)
```bash
cd /Users/sf/Desktop/Trendsetters
git add .
git commit -m "Initial commit: Trendsetters website"
git remote add origin https://github.com/[YOUR_USERNAME]/trendsetters.git
git push -u origin main
```

### 3. Enable GitHub Pages
1. In GitHub repository, go to Settings → Pages
2. Source: Deploy from branch
3. Branch: main, folder: / (root)
4. Save

### 4. Namecheap Domain Setup (Second Tab)
1. Log in to Namecheap
2. Go to Domain List
3. Click "Manage" next to your domain
4. Go to "Advanced DNS"

### 5. Add DNS Records in Namecheap

Delete existing A records and add these:

**A Records:**
- Host: `@`, Value: `185.199.108.153`
- Host: `@`, Value: `185.199.109.153`
- Host: `@`, Value: `185.199.110.153`
- Host: `@`, Value: `185.199.111.153`

**CNAME Record:**
- Host: `www`, Value: `[YOUR_USERNAME].github.io`

### 6. Add Custom Domain to GitHub
1. Go back to GitHub repository
2. Create new file named `CNAME`
3. Add your domain (e.g., `yourdomain.com`)
4. Commit the file

### 7. Final GitHub Pages Settings
1. Go to Settings → Pages again
2. Under "Custom domain", enter your domain
3. Check "Enforce HTTPS"

## Timeline:
- GitHub Pages: Active in 5-10 minutes
- DNS propagation: 30 minutes to 48 hours

## Test Your Sites:
- GitHub Pages: `https://[USERNAME].github.io/trendsetters/`
- Custom domain: `https://yourdomain.com`