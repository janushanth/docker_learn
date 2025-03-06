# Class 01: Basic Python Dockerfile

This folder contains a basic setup for containerizing a simple Flask application using Docker.

## 📂 Folder Structure

```
Class_01-basic-python-dockerfile/
│── app.py                        # Python application for a basic Flask app
│── Dockerfile                    # Dockerfile to build the Flask app image
│── requirements.txt              # Dependencies for the Flask app
│── README.md                     # Documentation for the basic Flask app
```

## Description

This class demonstrates how to containerize a simple Flask application using Docker.

## Requirements

- Docker

## Getting Started

1. Navigate to the `Class_01-basic-python-dockerfile` directory:

   ```bash
   cd Class_01-basic-python-dockerfile
   ```

2. Build the Docker image:

   ```bash
   docker build -t basic-flask-app .
   ```

3. Run the Docker container:

   ```bash
   docker run -p 5000:5000 basic-flask-app
   ```

4. Access the Flask application at `http://localhost:5000`.

## License

This project is licensed under the MIT License.