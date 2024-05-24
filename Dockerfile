# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update pip and setuptools
RUN pip install --upgrade pip setuptools

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Copy requirements.txt to the container
COPY ./requirements.txt /code/requirements.txt

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
