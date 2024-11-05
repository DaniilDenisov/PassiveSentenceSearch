# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files to the container
COPY PassiveSentenceSearch.py PassiveNLPFunctions.py requirements-docker.txt /app/

# Install the service-specific dependencies
RUN pip install --no-cache-dir -r requirements-docker.txt

# Install the spaCy model
RUN python -m spacy download en_core_web_sm

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_ENV=development

# Run the flask service when the container launches
CMD ["python", "PassiveSentenceSearch.py"]
