# Start from an image containing python3.6
FROM python:3.6

# Create a directory for our code and move to it
RUN mkdir /app
WORKDIR /app

# Copy requirements file to our current directory
ADD requirements.txt ./

# Install all dependencies
RUN pip install -r requirements.txt

# Copy all code into the image
ADD ./ ./

# Default command to run when launching a container
CMD bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python manage.py'