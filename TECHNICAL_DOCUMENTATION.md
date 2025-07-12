# The Trendsetters Website - Technical Documentation

## Project Overview
This document contains all technical details, configurations, and work done on The Trendsetters event management company website.

## Domain & Hosting Information

### Domain Details
- **Domain Name**: thetrendsettersindia.com
- **Domain Registrar**: (To be confirmed with client)
- **DNS Management**: Currently showing "Invalid nameservers" in Cloudflare

### GitHub Pages Hosting
- **Repository**: Trendsetters (under user's GitHub account)
- **GitHub Pages URL**: https://[username].github.io/Trendsetters
- **Custom Domain**: thetrendsettersindia.com (configured via CNAME file)
- **Status**: Deployed and accessible

### Required DNS Configuration
To properly connect the custom domain, add these DNS records at your domain registrar:
- **Type**: A Record
- **Name**: @
- **Values**: 
  - 185.199.108.153
  - 185.199.109.153
  - 185.199.110.153
  - 185.199.111.153
- **Type**: CNAME
- **Name**: www
- **Value**: [username].github.io

## Website Structure

### Pages
1. **index.html** - Homepage
2. **about.html** - About Us page
3. **services.html** - Services offered
4. **portfolio.html** - Portfolio/Gallery
5. **contact.html** - Contact information and form

### Folders
- **images/** - Contains all website images
  - founder.jpg - Founder Mr. Girish Purdhani's photo

### Key Features
- Fully responsive design with mobile-first approach
- Hamburger menu for mobile navigation
- Smooth scrolling animations
- Contact form (frontend only)
- Social media links placeholders

## Technical Stack
- **Frontend**: Pure HTML, CSS, JavaScript (no frameworks)
- **Hosting**: GitHub Pages (static site hosting)
- **Version Control**: Git with GitHub
- **Deployment**: Automatic via GitHub Pages on push to main branch

## Important Business Information

### Company Details
- **Company Name**: The Trendsetters
- **Tagline**: Event Management since 2003
- **Founded**: 2003 (previously showed 1994, now updated throughout)
- **Industry**: Event Management, Hospitality, Catering

### Contact Information
- **Phone Numbers**: 
  - +91-98450 54162 (Primary)
  - +91-77605 90454 (Secondary - added recently)
- **Email**: girish.purdhani@gmail.com
- **Address**: Krishna Kutir, 155 SFS-208, Yelahanka New Town, Bangalore-560064

### Founder Information
- **Name**: Mr. Girish Purdhani
- **Title**: Chief Executive & Founder
- **Experience**: 
  - 30+ years in luxury hospitality
  - 20+ years in event management (since 2003)
  - 13 years at Hotel Ashok Bangalore
  - Official caterer for all Yelahanka Air Shows

## Recent Updates & Fixes

### Navigation Issues (Fixed)
- Fixed missing `<ul class="nav-menu">` tags in services.html, portfolio.html, and contact.html
- Corrected HTML formatting issues (extra indentation and blank lines)
- Ensured consistent navigation structure across all pages

### Mobile Responsiveness (Fixed)
- Added comprehensive mobile CSS for all pages
- Implemented hamburger menu functionality
- Fixed logo and tagline alignment on mobile devices
- Added responsive breakpoints at 768px and 480px

### Content Updates
- Changed all year references from 1994 to 2003
- Added "Event Management since 2003" tagline to all pages
- Removed landline number as requested
- Added second phone number +91-77605 90454
- Restored founder's photo to About page
- Updated founder's bio to emphasize event management experience since 2003

### Technical Fixes Applied
1. **CNAME File**: Corrected domain from "trendsettersindia.com" to "thetrendsettersindia.com"
2. **Navigation Links**: Changed from anchor links (#) to proper page links (.html)
3. **Mobile Menu**: Fixed overlapping menu items by correcting HTML structure
4. **Logo Alignment**: Added CSS to prevent tagline text cutoff on mobile

## Git Configuration

### Repository Details
- **Local Path**: /Users/sf/Desktop/Trendsetters
- **Remote**: https://github.com/[username]/Trendsetters.git
- **Default Branch**: main

### GitHub Authentication
- Uses GitHub Desktop app for authentication and pushing
- Previous authentication issues with FlashDemo8789 account resolved
- Current setup uses the correct account for the Trendsetters repository

## CSS Color Scheme
```css
:root {
    --royal-blue: #1e3a8a;
    --elegant-blue: #3b82f6;
    --champagne-gold: #d4af37;
    --soft-gold: #f0e68c;
    --cream: #faf8f3;
    --pure-white: #ffffff;
    --charcoal: #1f2937;
    --silver: #e5e7eb;
}
```

## Known Issues & Pending Tasks

### DNS Configuration
- Domain shows "Invalid nameservers" in Cloudflare
- Needs proper DNS configuration at domain registrar level
- A records and CNAME need to be added as specified above

### Functional Enhancements (Future)
- Contact form backend integration
- Social media links need actual URLs
- Analytics integration (Google Analytics recommended)
- SEO optimization (meta tags, schema markup)

## Deployment Process

### To Deploy Updates:
1. Make changes to HTML/CSS/JS files
2. Test locally by opening HTML files in browser
3. Commit changes: `git add -A && git commit -m "Description"`
4. Push via GitHub Desktop (recommended) or command line
5. GitHub Pages automatically deploys within 2-10 minutes

### To Update Content:
- All text content is directly in HTML files
- No CMS or database - edit HTML files directly
- Images go in the `images/` folder
- Maintain consistent naming conventions

## File Modification History

### Python Scripts Created (for bulk fixes):
- fix_all_nav_issues.py - Fixed navigation structure
- fix_nav_menus.py - Added missing ul tags
- apply_mobile_fixes_all.py - Applied mobile CSS
- fix_logo_alignment.py - Fixed logo alignment issue
- add_mobile_fixes_about.py - Mobile fixes for about page

These scripts can be deleted after use as fixes are already applied.

## Important Notes

1. **No Backend**: This is a static website with no server-side functionality
2. **Form Submissions**: Contact form is frontend only - needs backend service for actual email delivery
3. **Image Optimization**: Consider optimizing images for web to improve load times
4. **HTTPS**: Automatically enabled via GitHub Pages
5. **Custom Domain Propagation**: Can take up to 48 hours after DNS changes

## Maintenance Guidelines

1. Always test on mobile devices after making changes
2. Keep consistent branding (colors, fonts, spacing)
3. Maintain the established year of 2003 across all content
4. Regular backups recommended (GitHub provides version history)
5. Monitor GitHub Pages build status after pushes

## Support Contacts

### Technical Issues:
- GitHub Pages documentation: https://docs.github.com/pages
- DNS configuration help: Contact domain registrar support

### Content Updates:
- Primary contact: Mr. Girish Purdhani
- Email: girish.purdhani@gmail.com
- Phone: +91-98450 54162 or +91-77605 90454

---

**Last Updated**: January 2025
**Documentation Version**: 1.0
**Next Review Date**: As needed for major updates

## Quick Checklist for New Developers

- [ ] Clone repository from GitHub
- [ ] Verify all pages load correctly locally
- [ ] Check mobile responsiveness
- [ ] Confirm images load properly
- [ ] Test navigation menu on mobile
- [ ] Verify contact information is current
- [ ] Check GitHub Pages deployment status
- [ ] Confirm custom domain is working

---

*This documentation should be updated whenever significant changes are made to the website.*