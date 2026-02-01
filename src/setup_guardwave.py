#!/usr/bin/env python3
import os

# Auto-create required directories
dirs = ["data", "assets"]
for d in dirs:
    path = os.path.join(os.path.dirname(__file__), d)
    os.makedirs(path, exist_ok=True)

print("GuardWave directories ready:")
for d in dirs:
    print(f" - {d}")
