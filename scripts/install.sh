#!/bin/bash

echo "Installing AgentForge..."

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
fi

echo "Installation completed."
echo "To activate the environment, run: source venv/bin/activate"
