# Use official slim Python image
FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies & AWS CLI
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        libgl1-mesa-glx \
        libglib2.0-0 \
        awscli \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Add src to Python path
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
