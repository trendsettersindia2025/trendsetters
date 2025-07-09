# Fix DNS Configuration in Namecheap

## Steps to Fix:

### 1. Login to Namecheap
Go to namecheap.com and login to your account

### 2. Go to Domain List
Click on "Domain List" in your dashboard

### 3. Find trendsettersindia.com
Click "Manage" next to your domain

### 4. Check Nameservers
In the domain details, look for "NAMESERVERS"
- Make sure it's set to "Namecheap BasicDNS" 
- If it shows "Custom DNS", change it back to "Namecheap BasicDNS"

### 5. Go to Advanced DNS
Click on "Advanced DNS" tab

### 6. Delete All Existing Records
Remove any existing A, CNAME, or other records

### 7. Add These Records:

**For the main domain (trendsettersindia.com):**
| Type | Host | Value | TTL |
|------|------|-------|-----|
| A Record | @ | 185.199.108.153 | Automatic |
| A Record | @ | 185.199.109.153 | Automatic |
| A Record | @ | 185.199.110.153 | Automatic |
| A Record | @ | 185.199.111.153 | Automatic |

**For www subdomain:**
| Type | Host | Value | TTL |
|------|------|-------|-----|
| CNAME Record | www | trendsettersindia2025.github.io | Automatic |

### 8. Save Changes
Click "Save All Changes"

### 9. Wait for Propagation
- Changes can take 30 minutes to 48 hours
- You can check propagation at: https://www.whatsmydns.net/

## Important Notes:
- Do NOT use both A records and CNAME for the same host
- The @ symbol means the root domain (trendsettersindia.com)
- Make sure there are no typos in the GitHub Pages URL