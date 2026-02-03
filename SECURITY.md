# Security Policy — GuardWave v1

**Maintainer:** BlueRing Security
**Slogan:** NO DAYS OFF!

---

## Reporting a Vulnerability

If you discover a security vulnerability in GuardWave:

1. **Do NOT open a public issue** — this is sensitive.  
2. Send a private email to: bee933769@gmail.com 
3. Include:
   - Description of the issue
   - Steps to reproduce
   - Impact assessment (if possible)
   - Environment details (OS, Python version, dependencies)

We will acknowledge receipt within 48 hours and provide a timeline for patching.

---

## Safe Usage

- GuardWave is a **local-first CLI tool**.  
- Do **not run on untrusted environments** without proper permissions.  
- Only run scripts from the `bin/` folder included in this repo.  
- Always keep your Python virtual environment isolated (`venv`).  

---

## Dependencies

- `fpdf2`  
- `pillow`  
- `fonttools`  
- `defusedxml`  

**Security notes:**
- Only install dependencies in a virtual environment.  
- Update packages regularly to avoid known vulnerabilities.  

---

## Responsible Disclosure

We aim to **resolve security issues quickly and transparently**. Contributions and reports are welcome via private channels only until a fix is released.
