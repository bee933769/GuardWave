#!/bin/bash
# Navigate to src and run guardwave.py with the virtual environment
cd "$(dirname "$0")/../src" || exit 1
../venv/bin/python3 guardwave.py
