#!/usr/bin/env python3
import subprocess
import os

# Paths
APP_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "guardwave.py")
VENV_PYTHON = os.path.join(os.path.dirname(__file__), "..", "venv", "bin", "python3")

# Run GuardWave
try:
    subprocess.run([VENV_PYTHON, APP_PATH], check=True)
except KeyboardInterrupt:
    print("\nSession closed safely.")
except FileNotFoundError:
    print("\nError: Python executable or app not found.")
