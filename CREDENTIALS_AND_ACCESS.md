# Credentials and Access Information

## ⚠️ IMPORTANT: Keep this file secure and do not commit to public repositories

## GitHub Access
- **Repository URL**: https://github.com/[username]/Trendsetters
- **Repository Name**: Trendsetters
- **Visibility**: Public (required for GitHub Pages)
- **Default Branch**: main
- **GitHub Pages**: Enabled on main branch

## Domain Information
- **Domain**: thetrendsettersindia.com
- **Registrar**: [TO BE FILLED BY CLIENT]
- **Registrar Login**: [TO BE FILLED BY CLIENT]
- **DNS Provider**: [TO BE FILLED BY CLIENT]
- **Renewal Date**: [TO BE FILLED BY CLIENT]

## Cloudflare Account (if applicable)
- **Email**: rohanpaten@gmail.com (shown in screenshot)
- **Domain Status**: Currently showing "Invalid nameservers"
- **Plan**: Free
- **Note**: Domain needs proper nameserver configuration

## Required DNS Settings
Add these at your domain registrar (NOT in Cloudflare unless using Cloudflare DNS):

**A Records** (GitHub Pages IPs):
- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

**CNAME Record**:
- Name: www
- Value: [github-username].github.io

## Email Configuration
- **Business Email**: girish.purdhani@gmail.com
- **Form Submissions**: Currently no backend - forms are decorative only
- **Future Integration**: Can use Formspree, EmailJS, or similar services

## Social Media (Placeholders - Need Real URLs)
- Facebook: #
- LinkedIn: #
- Instagram: #
- Twitter: #

## Analytics & Tracking
- **Google Analytics**: NOT CONFIGURED
- **Facebook Pixel**: NOT CONFIGURED
- **Other Tracking**: NONE

## API Keys & Services
Currently, no API keys or external services are integrated.

For future integrations:
- **Google Maps API**: Needed if adding interactive map
- **Form Handler**: Needed for contact form functionality
- **Analytics ID**: Needed for visitor tracking

## FTP/Hosting Access
- **Type**: GitHub Pages (no traditional FTP)
- **Deployment**: Automatic on push to main branch
- **Custom Domain**: Via CNAME file in repository

## Development Access

### Local Development
```bash
git clone https://github.com/[username]/Trendsetters.git
cd Trendsetters
# Open index.html in browser
```

### Push Access
- Via GitHub Desktop (recommended)
- Or via command line with proper GitHub authentication

## Important Security Notes

1. **Never commit API keys** to the repository
2. **Keep this file local** - add to .gitignore
3. **Use environment variables** for any future sensitive data
4. **Enable 2FA** on GitHub account
5. **Regularly review** repository access permissions

## Recovery Information

### If Domain is Lost:
- GitHub Pages URL will still work: https://[username].github.io/Trendsetters

### If GitHub Access is Lost:
- Contact GitHub support with proof of ownership
- Local copies serve as backup

### If Repository is Deleted:
- Check GitHub's restoration options (30-day window)
- Rebuild from local copy

---

**Last Updated**: January 2025
**Next Review**: Every 6 months or on major changes

## Checklist for New Team Members

- [ ] GitHub repository access granted
- [ ] Domain registrar access (if needed)
- [ ] Understanding of deployment process
- [ ] Local development environment setup
- [ ] Emergency contact list provided

---

**Remember**: This file contains sensitive information. Handle with care!