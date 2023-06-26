# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 4040

# Set the entrypoint command to run the Gunicorn server
CMD ["gunicorn", "-b", "0.0.0.0:4040", "app:app"]
