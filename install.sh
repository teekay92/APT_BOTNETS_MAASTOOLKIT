#!/bin/bash
# NightmareForge v2.3 – Auto Installer
# @nathan_non12796 | MU | 2025-11-17

echo "NightmareForge v2.3 – Installing..."

# Update & install deps
sudo apt update -y
sudo apt install -y python3 python3-pip python3-venv gcc wget tar libssl-dev libffi-dev

# Create venv
python3 -m venv nf_env
source nf_env/bin/activate

# Install Python deps
pip install --upgrade pip
pip install PyQt6 pycryptodome requests
# run

chmod +x nightmareforge.py

echo "Launching GUI..."
python nightmareforge.py --gui
