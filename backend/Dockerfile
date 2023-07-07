# Use a lightweight Python image
FROM python:3.11-slim-buster

WORKDIR /root/.postgresql

COPY root.crt .

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY main.py .

# Start the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]