# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Run the Django development server
CMD python manage.py runserver 0.0.0.0:8000
