#!/usr/bin/env python3

def update_year_in_file(filename):
    """Update year from 1994 to 2003"""
    
    # Read the file
    with open(filename, 'r') as f:
        content = f.read()
    
    # Count replacements
    count = 0
    
    # Replace different variations
    replacements = [
        ("Since 1994", "Since 2003"),
        ("SINCE 1994", "SINCE 2003"),
        ("since 1994", "since 2003"),
        (">1994<", ">2003<"),  # For milestone year
        ("Excellence Since 1994", "Excellence Since 2003"),
    ]
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            count += content.count(new)
    
    # Write back to file
    with open(filename, 'w') as f:
        f.write(content)
    
    if count > 0:
        print(f"✓ {filename} - Updated {count} occurrences")
    else:
        print(f"✓ {filename} - No changes needed")

# Update all HTML files
pages = ['index.html', 'about.html', 'services.html', 'portfolio.html', 'contact.html']

print("Updating year from 1994 to 2003...\n")

for page in pages:
    try:
        update_year_in_file(page)
    except Exception as e:
        print(f"✗ Error updating {page}: {e}")

print("\n✅ All pages updated!")