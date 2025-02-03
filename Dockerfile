# Use official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Ensure Pip is updated
RUN pip install --upgrade pip

# Check if requirements.txt exists before copying
COPY requirements.txt /app/

# Run pip install only if requirements.txt exists
RUN test -f "/app/requirements.txt" && pip install --no-cache-dir -r /app/requirements.txt || echo "⚠️ Skipping pip install: requirements.txt not found."

# Copy the rest of the app files
COPY . /app/

# Default command (Can be overridden in docker-compose)
CMD ["python", "/app/producer.py"]
