#!/bin/bash
# GuardWave macOS/Linux Launcher

if [ -d "../venv" ]; then
    source ../venv/bin/activate
fi

python3 ../src/guardwave.py
