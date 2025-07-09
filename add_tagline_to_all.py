#!/usr/bin/env python3
import re

def add_tagline_to_page(filename):
    """Add Event Management since 2003 tagline to page"""
    
    # Read the file
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check if already has tagline
    if 'Event Management since 2003' in content:
        print(f"✓ {filename} already has tagline")
        return
    
    # Add logo wrapper CSS if not present
    if '.logo-wrapper' not in content:
        logo_css = """
        
        .logo-wrapper {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
        
        .logo-tagline {
            font-size: 0.8rem;
            color: var(--charcoal);
            font-weight: 400;
            letter-spacing: 1px;
            margin-top: -5px;
            opacity: 0.8;
        }"""
        
        # Add CSS before .logo::after or before </style>
        if '.logo::after' in content:
            content = content.replace('.logo::after', logo_css + '\n\n        .logo::after')
        else:
            content = content.replace('    </style>', logo_css + '\n    </style>')
    
    # Update the navigation HTML
    old_nav = '<a href="index.html" class="logo">THE TRENDSETTERS</a>'
    new_nav = '''<div class="logo-wrapper">
                <a href="index.html" class="logo">THE TRENDSETTERS</a>
                <span class="logo-tagline">Event Management since 2003</span>
            </div>'''
    
    content = content.replace(old_nav, new_nav)
    
    # Write back to file
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✓ {filename} updated with tagline")

# Update all pages
pages = ['about.html', 'services.html', 'portfolio.html', 'contact.html']
for page in pages:
    try:
        add_tagline_to_page(page)
    except Exception as e:
        print(f"✗ Error updating {page}: {e}")

print("\n✅ All pages updated with tagline!")