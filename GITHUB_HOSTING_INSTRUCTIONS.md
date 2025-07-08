# GitHub Hosting Instructions for Trendsetters

Follow these steps to host your Trendsetters website on GitHub:

## Step 1: Create GitHub Repository

1. **Log into GitHub** with trendsettert95@gmail.com
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Repository settings:
   - **Repository name**: `trendsetters`
   - **Description**: "Trendsetters website"
   - **Public** (required for GitHub Pages)
   - **DO NOT** initialize with README (we already have files)
5. Click **"Create repository"**

## Step 2: Add Repository as Remote

After creating the repository, GitHub will show you commands. Run these in Terminal:

```bash
cd /Users/sf/Desktop/Trendsetters
git remote add origin https://github.com/YOUR_USERNAME/trendsetters.git
```

Replace `YOUR_USERNAME` with your GitHub username.

## Step 3: Commit and Push Files

```bash
# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Trendsetters website"

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **"Settings"** tab
3. Scroll down to **"Pages"** section (left sidebar)
4. Under **"Source"**, select:
   - **Deploy from a branch**
   - **Branch**: main
   - **Folder**: / (root)
5. Click **"Save"**

## Step 5: Access Your Website

After a few minutes, your site will be available at:
```
https://YOUR_USERNAME.github.io/trendsetters/
```

## Optional: Custom Domain

If you have a custom domain:

1. In repository, create file `CNAME` with your domain
2. In your domain provider, add:
   - A records pointing to:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - CNAME record: www pointing to YOUR_USERNAME.github.io

## Updating Your Site

To update your website:

```bash
# Make your changes
git add .
git commit -m "Update website"
git push
```

Changes will automatically deploy to GitHub Pages!