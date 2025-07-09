#!/usr/bin/env python3

def fix_navigation(filename):
    """Fix navigation structure by adding missing ul tag"""
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    fixed = False
    new_lines = []
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        
        # Look for menu-toggle closing div followed by li items
        if '</div>' in line and i < len(lines) - 2:
            next_line = lines[i + 1] if i + 1 < len(lines) else ''
            next_next_line = lines[i + 2] if i + 2 < len(lines) else ''
            
            # Check if next lines have li items without ul
            if '<li><a href=' in next_next_line and '<ul' not in next_line:
                # Insert ul tag with proper indentation
                indent = '            '
                new_lines.append(f'{indent}<ul class="nav-menu">\n')
                # Also add Home link if missing
                if 'index.html' not in next_next_line:
                    new_lines.append(f'{indent}    <li><a href="index.html">Home</a></li>\n')
                fixed = True
    
    if fixed:
        with open(filename, 'w') as f:
            f.writelines(new_lines)
        print(f"✓ Fixed navigation in {filename}")
    else:
        print(f"✗ Could not fix navigation in {filename}")
    
    return fixed

# Fix all pages
pages = ['services.html', 'portfolio.html', 'contact.html']

print("Fixing navigation structure in all pages...\n")

for page in pages:
    try:
        fix_navigation(page)
    except Exception as e:
        print(f"✗ Error fixing {page}: {e}")

print("\n✅ Navigation fix complete!")