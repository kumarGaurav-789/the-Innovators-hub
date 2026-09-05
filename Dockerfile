# Use lightweight official Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Set working directory
WORKDIR /app

# Install system dependencies if any
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies first for efficient Docker layer caching
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all application code
COPY . .

# Expose server port
EXPOSE 8000

# Run uvicorn server (respects dynamic PORT env var for Render/Cloud Run)
CMD ["sh", "-c", "python -m uvicorn backend.server:app --host 0.0.0.0 --port ${PORT:-8000}"]
