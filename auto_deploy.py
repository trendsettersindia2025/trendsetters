#!/usr/bin/env python3
"""
Automated GitHub deployment for Trendsetters
"""

import subprocess
import time
import os
import sys

def run_command(cmd):
    """Run a shell command and return output"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result.returncode == 0

def main():
    print("🚀 Automated Trendsetters Deployment")
    print("=" * 40)
    
    # Change to project directory
    os.chdir("/Users/sf/Desktop/Trendsetters")
    
    # Get GitHub username
    username = input("Enter your GitHub username: ").strip()
    if not username:
        print("❌ Username required!")
        return
    
    print(f"\n📁 Working in: {os.getcwd()}")
    
    # Check if git repo exists
    if not os.path.exists(".git"):
        print("❌ No git repository found. Initializing...")
        run_command("git init")
    
    # Check current remotes
    print("\n🔍 Checking existing remotes...")
    result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
    
    if "origin" in result.stdout:
        print("⚠️  Origin already exists. Removing old origin...")
        run_command("git remote remove origin")
    
    # Add all files
    print("\n📦 Adding all files...")
    run_command("git add .")
    
    # Commit
    print("\n💾 Creating commit...")
    run_command('git commit -m "Deploy Trendsetters website to GitHub Pages"')
    
    # Add remote
    print(f"\n🔗 Adding GitHub remote...")
    repo_url = f"https://github.com/{username}/trendsetters.git"
    run_command(f"git remote add origin {repo_url}")
    
    # Push to GitHub
    print(f"\n📤 Pushing to GitHub...")
    if run_command("git branch -M main"):
        if run_command("git push -u origin main"):
            print("\n✅ Successfully pushed to GitHub!")
        else:
            print("\n⚠️  Push failed. Trying force push...")
            if run_command("git push -u origin main --force"):
                print("✅ Force push successful!")
            else:
                print("❌ Could not push. Please check:")
                print("1. Repository exists at: " + repo_url)
                print("2. You're logged in to git")
                return
    
    print("\n🎉 Deployment Complete!")
    print(f"\n📍 Your repository: https://github.com/{username}/trendsetters")
    print(f"🌐 Your site will be at: https://{username}.github.io/trendsetters/")
    print("\n⚠️  IMPORTANT: Enable GitHub Pages:")
    print("1. Go to your repository on GitHub")
    print("2. Click Settings → Pages")
    print("3. Source: Deploy from branch")
    print("4. Branch: main, folder: / (root)")
    print("5. Click Save")
    print("\nGitHub Pages will be live in 5-10 minutes!")

if __name__ == "__main__":
    main()