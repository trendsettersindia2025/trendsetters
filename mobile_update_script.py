#!/usr/bin/env python3
import re

def add_mobile_navigation(filename):
    """Add mobile navigation to HTML file"""
    
    # Read the file
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check if already has mobile navigation
    if 'menu-toggle' in content:
        print(f"✓ {filename} already has mobile navigation")
        return
    
    # Add hamburger CSS before </style>
    hamburger_css = """        
        /* Hamburger Menu Styles */
        .menu-toggle {
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 30px;
            height: 30px;
            cursor: pointer;
            z-index: 1001;
        }

        .menu-toggle span {
            display: block;
            width: 25px;
            height: 3px;
            background: var(--royal-blue);
            margin: 3px 0;
            transition: all 0.3s ease;
        }

        .menu-toggle.active span:nth-child(1) {
            transform: rotate(45deg) translate(5px, 5px);
        }

        .menu-toggle.active span:nth-child(2) {
            opacity: 0;
        }

        .menu-toggle.active span:nth-child(3) {
            transform: rotate(-45deg) translate(7px, -6px);
        }
        
        /* Mobile Navigation */
        @media (max-width: 768px) {
            .menu-toggle {
                display: flex;
            }
            
            .nav-menu {
                position: fixed;
                left: -100%;
                top: 0;
                flex-direction: column;
                background-color: var(--pure-white);
                width: 100%;
                height: 100vh;
                text-align: center;
                transition: 0.3s;
                box-shadow: 0 10px 27px rgba(0, 0, 0, 0.05);
                padding-top: 100px;
                gap: 2rem;
            }
            
            .nav-menu.active {
                left: 0;
            }
            
            .nav-menu li {
                margin: 1rem 0;
            }
            
            .nav-menu a {
                font-size: 1.2rem;
            }
            
            header {
                padding: 0.5rem 5%;
            }
            
            nav {
                padding: 1rem 0;
            }
            
            .logo {
                font-size: 1.5rem;
                letter-spacing: 2px;
            }
            
            .cta-nav {
                padding: 0.6rem 1.5rem !important;
                font-size: 0.9rem;
            }
        }
    """
    
    # Add CSS before </style>
    content = content.replace('    </style>', hamburger_css + '\n    </style>')
    
    # Add hamburger div after logo
    hamburger_html = """            <div class="menu-toggle">
                <span></span>
                <span></span>
                <span></span>
            </div>"""
    
    content = re.sub(
        r'(<a href="index.html" class="logo">THE TRENDSETTERS</a>\s*\n\s*)(<ul class="nav-menu">)',
        r'\1' + hamburger_html + '\n            \2',
        content
    )
    
    # Add JavaScript before </script>
    js_code = """
        
        // Hamburger Menu Toggle
        const menuToggle = document.querySelector('.menu-toggle');
        const navMenu = document.querySelector('.nav-menu');
        const navLinks = document.querySelectorAll('.nav-menu a');
        
        if (menuToggle) {
            menuToggle.addEventListener('click', function() {
                menuToggle.classList.toggle('active');
                navMenu.classList.toggle('active');
            });
            
            // Close menu when clicking on a link
            navLinks.forEach(link => {
                link.addEventListener('click', function() {
                    menuToggle.classList.remove('active');
                    navMenu.classList.remove('active');
                });
            });
            
            // Close menu when clicking outside
            document.addEventListener('click', function(e) {
                if (!menuToggle.contains(e.target) && !navMenu.contains(e.target)) {
                    menuToggle.classList.remove('active');
                    navMenu.classList.remove('active');
                }
            });
        }"""
    
    # Find the last </script> tag
    last_script_pos = content.rfind('    </script>')
    if last_script_pos != -1:
        content = content[:last_script_pos] + js_code + '\n' + content[last_script_pos:]
    
    # Write back to file
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✓ {filename} updated with mobile navigation")

# Update all pages
pages = ['services.html', 'portfolio.html', 'contact.html']
for page in pages:
    try:
        add_mobile_navigation(page)
    except Exception as e:
        print(f"✗ Error updating {page}: {e}")

print("\n✅ All pages updated!")