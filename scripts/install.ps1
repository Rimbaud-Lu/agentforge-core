Write-Output "Installing AgentForge..."

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file if it doesn't exist
if (!(Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
}

Write-Output "Installation completed."
Write-Output "To activate the environment, run: .\venv\Scripts\activate"
