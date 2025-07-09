#!/usr/bin/env python3
import re

def add_mobile_fixes_to_page(filename):
    """Add comprehensive mobile fixes to page"""
    
    # Read the file
    with open(filename, 'r') as f:
        content = f.read()
    
    # Find where to insert the mobile fixes (before the closing </style>)
    style_end = content.find('    </style>')
    if style_end == -1:
        print(f"✗ Could not find </style> tag in {filename}")
        return
    
    # Mobile fixes CSS
    mobile_fixes = """
        /* Additional Mobile Alignment Fixes */
        @media (max-width: 768px) {
            /* Fix menu toggle position */
            .menu-toggle {
                margin-left: auto;
            }
            
            /* Fix navigation menu */
            .nav-menu {
                padding-top: 80px !important;
                gap: 1rem !important;
                align-items: center;
                justify-content: center;
            }
            
            .nav-menu li {
                margin: 0.5rem 0 !important;
                width: 100%;
                text-align: center;
            }
            
            .nav-menu a {
                display: block;
                padding: 0.5rem;
            }
            
            /* Fix header and nav */
            header {
                padding: 0.5rem 3% !important;
            }
            
            nav {
                padding: 0.8rem 0 !important;
                align-items: center;
            }
            
            /* Fix logo and tagline */
            .logo-wrapper {
                margin-right: auto;
            }
            
            .logo {
                font-size: 1.3rem !important;
                letter-spacing: 1px !important;
            }
            
            .logo-tagline {
                font-size: 0.7rem !important;
                margin-top: -8px;
            }
            
            /* Page specific fixes */
            .hero, .services-hero, .portfolio-hero, .contact-hero, .about-hero {
                margin-top: 60px !important;
                padding-top: 2rem;
            }
            
            .hero-content, .services-hero-content, .portfolio-hero-content, .contact-hero-content, .about-hero-content {
                padding: 0 1rem !important;
                text-align: center;
            }
            
            .hero-title, .services-hero h1, .portfolio-hero h1, .contact-hero h1 {
                font-size: 2.2rem !important;
                line-height: 1.2 !important;
                margin-bottom: 0.5rem !important;
            }
            
            .hero-subtitle {
                font-size: 0.9rem !important;
                letter-spacing: 1px !important;
                margin-bottom: 1rem !important;
            }
            
            .hero-description {
                font-size: 0.95rem !important;
                line-height: 1.6 !important;
                padding: 0 1rem;
                margin-bottom: 1.5rem !important;
            }
            
            /* Fix sections */
            section {
                padding: 3rem 3% !important;
            }
            
            .section-header {
                margin-bottom: 3rem !important;
                padding: 0 1rem;
            }
            
            /* Fix cards and grids */
            .service-grid, .portfolio-grid, .services-grid {
                padding: 0 1rem;
                grid-template-columns: 1fr !important;
            }
            
            .service-card, .portfolio-item {
                margin-bottom: 2rem;
            }
            
            /* Fix footer */
            footer {
                padding: 2rem 3% !important;
                text-align: center;
            }
            
            .footer-content p {
                font-size: 0.9rem;
                margin-bottom: 1rem;
            }
            
            .social-links {
                justify-content: center;
            }
        }
        
        /* Extra small devices */
        @media (max-width: 480px) {
            .logo {
                font-size: 1.1rem !important;
            }
            
            .logo-tagline {
                font-size: 0.65rem !important;
            }
            
            .hero-title, .services-hero h1, .portfolio-hero h1, .contact-hero h1 {
                font-size: 1.8rem !important;
            }
            
            .hero-title .accent {
                font-size: 2rem !important;
                display: block;
                margin: 0.5rem 0;
            }
            
            .section-title, h2 {
                font-size: 1.8rem !important;
            }
            
            .btn-primary, .btn-secondary, .cta-button {
                width: 100%;
                max-width: 280px;
                margin: 0.5rem auto;
                padding: 0.8rem 1.8rem !important;
                font-size: 0.9rem !important;
            }
        }
"""
    
    # Insert the mobile fixes before </style>
    content = content[:style_end] + mobile_fixes + '\n' + content[style_end:]
    
    # Write back to file
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✓ {filename} updated with mobile fixes")

# Apply to all pages except index.html and about.html
pages = ['services.html', 'portfolio.html', 'contact.html']

print("Applying comprehensive mobile fixes...\n")

for page in pages:
    try:
        add_mobile_fixes_to_page(page)
    except Exception as e:
        print(f"✗ Error updating {page}: {e}")

print("\n✅ All pages updated with mobile fixes!")