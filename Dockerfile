# FROM --platform=linux/amd64 python:3.10 as build
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the redo_erm files into the container at /app
COPY ["./app.py", "./requirements.txt", "./"]

# Install any needed packages specified in rag_requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
# FastAPI default port is 8000
EXPOSE 8000

# Run app.py when the container launches
# CMD ["flask", "run"]
# CMD ["python", "app.py"]
# CMD ["fastapi", "dev", "app.py"]
CMD ["fastapi", "run", "app.py"]
