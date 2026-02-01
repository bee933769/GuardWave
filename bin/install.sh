#!/bin/bash
echo "Installing GuardWaveBundle..."
cd "$(dirname "$0")"/..
source venv/bin/activate
pip install -r requirements.txt
echo "✅ Installation complete. Run bin/launch.sh to start GuardWave."
