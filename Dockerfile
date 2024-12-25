# Use the official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file to the container.
COPY subdir/requirements.txt /app/requirements.txt


# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Expose the application port.
EXPOSE 5000

# Run the application.
CMD ["python", "app.py"]
