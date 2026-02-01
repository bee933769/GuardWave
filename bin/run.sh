#!/bin/bash

# ===============================
# GuardWave v1 Launcher Script
# ===============================

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Path to virtual environment Python
VENV_PYTHON="$PROJECT_DIR/venv/bin/python3"

# Check if venv Python exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "Virtual environment not found. Please run:"
    echo "python3 -m venv venv"
    echo "source venv/bin/activate"
    exit 1
fi

# Activate virtual environment
source "$PROJECT_DIR/venv/bin/activate"

# Run main GuardWave app
"$VENV_PYTHON" "$PROJECT_DIR/src/guardwave.py"
