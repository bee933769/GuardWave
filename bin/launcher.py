#!/usr/bin/env python3
import os
import sys
import subprocess

# ===============================
# GuardWave v1 Python Launcher
# ===============================

# Get project root directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

# Path to virtual environment Python
VENV_PYTHON = os.path.join(PROJECT_DIR, "venv", "bin", "python3")
MAIN_APP = os.path.join(PROJECT_DIR, "src", "guardwave.py")

# Check if virtual environment Python exists
if not os.path.isfile(VENV_PYTHON):
    print("Virtual environment not found. Please run:")
    print("python3 -m venv venv")
    print("source venv/bin/activate")
    sys.exit(1)

# Run GuardWave using venv Python
subprocess.run([VENV_PYTHON, MAIN_APP])
