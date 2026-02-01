# GuardWave v1 — BlueRing Security

**Slogan:** NO DAYS OFF!  

GuardWave is a lightweight, local-first security CLI designed to help you monitor, classify, and log suspicious events instantly. Built by BlueRing Security — inspired by the intelligence and resilience of the deadliest octopus.  

## Features
- Classify alerts automatically: Account Logins, Phishing, App Permission Changes
- Timeline logging & PDF export for offline review
- Fast, minimal dependencies, Python 3.9+ compatible
- Secure local-first operation — no cloud dependencies

## Installation
# Clone the repo
git clone https://github.com/bee933769/GuardWave.git
cd GuardWaveBundle

# Install dependencies in virtual environment
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install fpdf2 pillow fonttools defusedxml

# Make scripts executable
chmod +x bin/*.sh src/*.py

## Usage
# Launch the GuardWave CLI
./bin/run.sh
# or
python3 src/guardwave.py

## Contributing
- Fork the repo, make your changes, and submit a pull request.
- Please review SECURITY.md for responsible disclosure policies.

## License
MIT License — see LICENSE file.

