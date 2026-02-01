# Security Policy — GuardWave

## Reporting a Vulnerability

If you discover a security issue in GuardWave, please report it responsibly:

- Send an email to: security@blueringsecurity.com
- Include:
  - Steps to reproduce the issue
  - Version of GuardWave
  - Any relevant screenshots/logs

We take security seriously and will respond within 48 hours.

## Supported Versions

Only the latest release branch (`main`) is officially supported. Older versions may not receive security updates.

## Security Best Practices

- Always run GuardWave in its Python virtual environment (`venv`) to isolate dependencies.
- Do not share sensitive credentials in logs or config files.
- Keep dependencies updated:
\`\`\`bash
pip install --upgrade pip fpdf2 pillow fonttools defusedxml
\`\`\`

## Disclaimer

GuardWave is provided as-is. Users are responsible for safe operation within their environments.
