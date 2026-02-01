#!/bin/bash
# GuardWave Quick Installer

echo "🚀 Initializing GuardWave installation..."

# Check Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.9+ first."
    exit 1
fi

# Check venv
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements if any
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo "✅ GuardWave setup complete!"
echo "Run GuardWave: ./bin/launch.sh"
