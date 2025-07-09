#!/usr/bin/env python3

def add_mobile_fixes_to_about():
    """Add the same mobile fixes to about.html"""
    
    # Read the file
    with open('about.html', 'r') as f:
        content = f.read()
    
    # Check if mobile fixes already exist
    if 'Additional Mobile Alignment Fixes' in content:
        print("✓ about.html already has mobile alignment fixes")
        return
    
    # Find where to insert (before the closing </style>)
    style_end = content.find('    </style>')
    if style_end == -1:
        print("✗ Could not find </style> tag")
        return
    
    # Mobile fixes CSS (same as other pages)
    mobile_fixes = """
        /* Additional Mobile Alignment Fixes */
        @media (max-width: 768px) {
            /* Fix sections */
            section {
                padding: 3rem 3% !important;
            }
            
            .about-hero {
                margin-top: 60px !important;
                padding-top: 2rem;
            }
            
            .about-hero-content {
                padding: 0 1rem !important;
            }
            
            .hero-title {
                font-size: 2.2rem !important;
                line-height: 1.2 !important;
            }
            
            .hero-title span {
                display: block;
                margin: 0.5rem 0;
            }
            
            /* Fix value cards */
            .value-card {
                margin-bottom: 2rem;
            }
            
            /* Fix milestone alignment */
            .milestone {
                padding: 2rem 1rem !important;
            }
        }
"""
    
    # Insert the mobile fixes
    content = content[:style_end] + mobile_fixes + '\n' + content[style_end:]
    
    # Write back
    with open('about.html', 'w') as f:
        f.write(content)
    
    print("✓ about.html updated with additional mobile fixes")

# Run the update
add_mobile_fixes_to_about()