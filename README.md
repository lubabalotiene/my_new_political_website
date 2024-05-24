# Monwabisi Xhegwana's Political Website

Welcome to Monwabisi Xhegwana's Political Website! This website serves as a platform for Monwabisi Xhegwana's political campaign, providing information about their candidacy, policies, and ways to get involved.

## Django Capstone Project
Table of Contents
   Introduction   
   Requirements   
   Setup
      Virtual Environment
      Docker
Database Migration
Running the Server
Contributing
License

## Introduction
This is a Django project developed for the capstone project. This guide will help you set up and run the project using a virtual environment and Docker.

## Requirements
Python 3.9+
Django 5.0.4
Docker
Docker Compose (optional)

## Setup
   Virtual Environment

1. Clone the repository:
   git clone https://github.com/lubabalotiene/my_new_political_website.git
   cd my_new_political_website

2. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   pip install --upgrade pip
   pip install -r requirements.txt


## Getting Started  - Docker


1. Section for Docker:

   ## Docker Instructions

   ### Prerequisites

   - [Docker](https://docs.docker.com/get-docker/) installed on your machine.

   ### Building the Docker Image

   1.1 **Clone the repository**:
   ```bash
   git clone https://github.com/lubabalotiene/my_new_political_website.git
   cd my_new_political_website


2. Build the Docker image:
   '''bash
   docker build -t my_new_political_website

## Running the Docker Container

1. Run the Docker container:
   '''bash
   docker run -d -p 8000:8000 my_new_political_website

2. Access the application:
   Open your web browser and navigate to http://localhost:8000.

## Building and Running for Development

   1. Build the Docker image for development:
      '''bash
      docker build -f Dockerfile.dev -t my_new_political_website.

   2. Run the Docker container for development:
      '''bash
      docker run -v $(pwd):/app --env-file .env -d -p 8000:8000 my_new_political_website

## Database Migration
   1.  Apply migrations:
      python manage.py makemigrations
      python manage.py migrate
      
## If you are using Docker, you can run these commands inside the Docker container:
   1. Start an interactive shell in the container:
      docker run -it myapp /bin/sh

   2. Apply migrations:
      python manage.py makemigrations
      python manage.py migrate

## Running the Server
   Virtual Environment:

   1.  To run the server locally using a virtual environment, execute:
      python manage.py runserver

## Stopping the Docker Container

   1. List running containers:
      '''bash:
      docker ps

   2. Stop the container:
      '''bash:
      docker stop QJI56F

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Contact
For inquiries or feedback, please contact Monwabisi, @ monwabisi@gmail.com.

## License
This project is licensed under the Monwabisi'srights.


This README provides clear instructions for setting up and running the political website locally, along with optional Docker instructions. It also includes sections for contributing, contacting the candidate, and licensing information.



