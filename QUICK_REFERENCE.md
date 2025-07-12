# Quick Reference Guide - The Trendsetters Website

## Common Tasks

### Adding a New Phone Number
1. Open `contact.html`
2. Find the "Call Us" section (around line 1120)
3. Add new phone number with proper formatting:
```html
<a href="tel:+91XXXXXXXXXX">+91-XXXXX XXXXX</a><br>
```

### Updating Event Year/Since Date
1. Search for "2003" in all HTML files
2. Update consistently across:
   - Logo tagline
   - Footer text
   - About page content
   - Any other mentions

### Adding New Images
1. Save image with descriptive name (no spaces)
2. Place in `images/` folder
3. Reference in HTML: `<img src="images/filename.jpg" alt="Description">`

### Fixing Mobile Navigation Issues
Check for:
1. Missing `<ul class="nav-menu">` wrapper
2. Extra indentation before menu-toggle div
3. Blank lines between menu items

### Pushing Updates to Live Site
1. Open GitHub Desktop
2. Review changes
3. Commit with descriptive message
4. Push to origin/main
5. Wait 2-10 minutes for deployment

## File Locations

- **Homepage**: index.html
- **About Page**: about.html (contains founder info)
- **Services**: services.html
- **Portfolio**: portfolio.html
- **Contact**: contact.html (has phone numbers, address)
- **Images**: images/ folder
- **Domain Config**: CNAME file

## CSS Classes to Know

- `.nav-menu` - Navigation menu wrapper
- `.menu-toggle` - Hamburger menu icon
- `.logo-wrapper` - Logo and tagline container
- `.hero-section` - Main banner areas
- `.contact-info` - Contact details sections

## Testing Checklist

Before pushing any changes:
- [ ] Test on desktop browser
- [ ] Test on mobile browser
- [ ] Check hamburger menu works
- [ ] Verify all links work
- [ ] Confirm images load
- [ ] Test at 320px, 768px, and 1200px widths

## Emergency Contacts

**GitHub Pages Down?**
- Check: https://www.githubstatus.com/

**Domain Not Working?**
- Verify CNAME file contains: thetrendsettersindia.com
- Check DNS propagation: https://www.whatsmydns.net/

**Need Help?**
- Technical documentation: See TECHNICAL_DOCUMENTATION.md
- GitHub Pages docs: https://docs.github.com/pages

---
*Keep this guide handy for quick fixes and updates!*