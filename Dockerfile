# Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copies your entire project structure into the container
COPY . . 

# Set environment variables for Flask (e.g., for config.py)
# Tells Flask where to find your app
ENV FLASK_APP=src.prediction_api 
ENV FLASK_RUN_HOST=0.0.0.0
 # Set to 1 for development
ENV FLASK_DEBUG=0

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask application using Gunicorn for production
# (Install gunicorn in requirements.txt)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.prediction_api:app"]

# Or for simple development:
# CMD ["flask", "run"]