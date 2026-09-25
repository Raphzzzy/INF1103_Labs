# Use an official lightweight Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy auditor.py from local folder into the container working directory
COPY auditor.py .

# Define the default command to run when the container starts
CMD ["python", "auditor.py"]
