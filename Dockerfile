# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]
