FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create virtual environment entry point
ENV PATH="/app/venv/bin:$PATH"

# Expose ports
EXPOSE 8000 6379 6333

# Default command
CMD ["python", "-m", "agentforge_core.cli.cli"]
