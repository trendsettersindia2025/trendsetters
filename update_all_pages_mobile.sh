#!/bin/bash

# Update all pages with mobile navigation improvements

echo "Updating all pages with mobile navigation..."

# List of pages to update
pages=("about.html" "services.html" "portfolio.html" "contact.html")

# Create backup directory
mkdir -p backups

for page in "${pages[@]}"; do
    echo "Updating $page..."
    
    # Backup original file
    cp "$page" "backups/$page.backup"
    
    # Read the file
    content=$(<"$page")
    
    # Check if hamburger menu already exists
    if [[ ! "$content" =~ "menu-toggle" ]]; then
        # Add hamburger menu div after logo
        content=$(echo "$content" | sed '/<a href="index.html" class="logo">THE TRENDSETTERS<\/a>/a\
            <div class="menu-toggle">\
                <span></span>\
                <span></span>\
                <span></span>\
            </div>')
        
        # Add hamburger menu CSS before the first @media query
        hamburger_css='        /* Hamburger Menu Styles */\
        .menu-toggle {\
            display: none;\
            flex-direction: column;\
            justify-content: center;\
            align-items: center;\
            width: 30px;\
            height: 30px;\
            cursor: pointer;\
            z-index: 1001;\
        }\
\
        .menu-toggle span {\
            display: block;\
            width: 25px;\
            height: 3px;\
            background: var(--royal-blue);\
            margin: 3px 0;\
            transition: all 0.3s ease;\
        }\
\
        .menu-toggle.active span:nth-child(1) {\
            transform: rotate(45deg) translate(5px, 5px);\
        }\
\
        .menu-toggle.active span:nth-child(2) {\
            opacity: 0;\
        }\
\
        .menu-toggle.active span:nth-child(3) {\
            transform: rotate(-45deg) translate(7px, -6px);\
        }\
\'
        
        # Add the CSS before </style>
        content=$(echo "$content" | sed "/<\/style>/i\\$hamburger_css")
        
        # Add mobile menu CSS
        mobile_css='        /* Mobile Navigation */\
        @media (max-width: 768px) {\
            .menu-toggle {\
                display: flex;\
            }\
            \
            .nav-menu {\
                position: fixed;\
                left: -100%;\
                top: 0;\
                flex-direction: column;\
                background-color: var(--pure-white);\
                width: 100%;\
                height: 100vh;\
                text-align: center;\
                transition: 0.3s;\
                box-shadow: 0 10px 27px rgba(0, 0, 0, 0.05);\
                padding-top: 100px;\
                gap: 2rem;\
            }\
            \
            .nav-menu.active {\
                left: 0;\
            }\
            \
            .nav-menu li {\
                margin: 1rem 0;\
            }\
            \
            .nav-menu a {\
                font-size: 1.2rem;\
            }\
        }'
        
        # Add mobile CSS
        content=$(echo "$content" | sed "/<\/style>/i\\$mobile_css")
        
        # Add JavaScript for hamburger menu
        js_code='        // Hamburger Menu Toggle\
        const menuToggle = document.querySelector('"'"'.menu-toggle'"'"');\
        const navMenu = document.querySelector('"'"'.nav-menu'"'"');\
        const navLinks = document.querySelectorAll('"'"'.nav-menu a'"'"');\
        \
        if (menuToggle) {\
            menuToggle.addEventListener('"'"'click'"'"', function() {\
                menuToggle.classList.toggle('"'"'active'"'"');\
                navMenu.classList.toggle('"'"'active'"'"');\
            });\
            \
            navLinks.forEach(link => {\
                link.addEventListener('"'"'click'"'"', function() {\
                    menuToggle.classList.remove('"'"'active'"'"');\
                    navMenu.classList.remove('"'"'active'"'"');\
                });\
            });\
        }'
        
        # Add JavaScript before </script>
        content=$(echo "$content" | sed "/<\/script>/i\\$js_code")
        
        # Write updated content back to file
        echo "$content" > "$page"
        
        echo "✓ $page updated successfully"
    else
        echo "✓ $page already has mobile navigation"
    fi
done

echo ""
echo "✅ All pages updated with mobile navigation!"
echo "Backups saved in ./backups/"