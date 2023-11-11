#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the requests library using pip
pip install requests

# Run the script
python $HOME/1337-find-peers/src/find_peers.py

# Deactivate the virtual environment
deactivate

# Remove the virtual environment
rm -rf venv
