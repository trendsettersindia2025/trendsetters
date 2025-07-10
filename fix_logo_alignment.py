#!/usr/bin/env python3

def fix_logo_alignment(filename):
    """Fix logo alignment on mobile by adding proper CSS"""
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check if the fix is already applied
    if 'white-space: nowrap;' in content and '.logo-wrapper {' in content and 'min-width: 200px;' in content:
        print(f"✓ {filename} already has logo alignment fix")
        return False
    
    # Find the .logo-tagline mobile CSS and add the fix
    old_css = """            .logo-tagline {
                font-size: 0.65rem !important;
            }"""
    
    new_css = """            .logo-tagline {
                font-size: 0.65rem !important;
                white-space: nowrap;
                overflow: visible;
            }
            
            .logo-wrapper {
                min-width: 200px;
            }"""
    
    if old_css in content:
        content = content.replace(old_css, new_css)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"✓ Fixed logo alignment in {filename}")
        return True
    else:
        # Try alternative approach - find @media (max-width: 480px) and add the styles
        import re
        
        # Pattern to find the 480px media query
        pattern = r'(@media\s*\(\s*max-width:\s*480px\s*\)\s*{[^}]*\.logo\s*{[^}]*}[^}]*)(})'
        
        def replacer(match):
            return match.group(1) + """
            
            .logo-tagline {
                font-size: 0.65rem !important;
                white-space: nowrap;
                overflow: visible;
            }
            
            .logo-wrapper {
                min-width: 200px;
            }
            """ + match.group(2)
        
        new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"✓ Fixed logo alignment in {filename} (alternative method)")
            return True
    
    print(f"✗ Could not fix logo alignment in {filename}")
    return False

# Fix all pages
pages = ['about.html', 'services.html', 'portfolio.html', 'contact.html']

print("Fixing logo alignment on mobile for all pages...\n")

for page in pages:
    try:
        fix_logo_alignment(page)
    except Exception as e:
        print(f"✗ Error fixing {page}: {e}")

print("\n✅ Logo alignment fix complete!")