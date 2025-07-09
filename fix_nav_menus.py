#!/usr/bin/env python3
import re

def fix_navigation_in_file(filename):
    """Fix missing ul tag in navigation"""
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check if nav-menu ul is missing
    if '<ul class="nav-menu">' not in content and '<li><a href=' in content:
        # Find the pattern where menu items start without ul
        pattern = r'(</div>\s*\n\s*<li><a href=")'
        
        if re.search(pattern, content):
            # Replace with proper ul opening
            content = re.sub(
                r'(</div>)\s*\n(\s*)<li><a href="services.html',
                r'\1\n\2<ul class="nav-menu">\n\2    <li><a href="index.html">Home</a></li>\n\2    <li><a href="about.html">About</a></li>\n\2    <li><a href="services.html',
                content
            )
            
            with open(filename, 'w') as f:
                f.write(content)
            
            print(f"✓ Fixed navigation in {filename}")
            return True
    
    print(f"✓ {filename} navigation is already correct")
    return False

# Check all pages
pages = ['services.html', 'portfolio.html', 'contact.html']

print("Checking and fixing navigation menus...\n")

for page in pages:
    try:
        fix_navigation_in_file(page)
    except Exception as e:
        print(f"✗ Error fixing {page}: {e}")

print("\n✅ Navigation check complete!")