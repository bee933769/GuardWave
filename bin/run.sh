#!/bin/bash
# Run GuardWave CLI

# Go to the folder where this script lives
cd "$(dirname "$0")/../src"

# Run the app using the venv Python
../venv/bin/python3 guardwave.py
