project-root/
│── docker-compose.yml            # Docker Compose file to orchestrate services
│── nginx.conf                    # Nginx configuration file for load balancing
│── jaffnakid/                    # Service folder for the Jaffna Small Kids application
│   ├── app.py                    # Python application for Jaffnakid
│   ├── Dockerfile                # Dockerfile to build the Jaffnakid service image
│   ├── requirements.txt          # Dependencies for Jaffnakid service
│── wellawattakid/                 # Service folder for the Wellawatta Small Kids application
│   ├── app.py                    # Python application for Wellawattakid
│   ├── Dockerfile                # Dockerfile to build the Wellawattakid service image
│   ├── requirements.txt          # Dependencies for Wellawattakid service

## Description

### `docker-compose.yml`
This is the main configuration file to define and run multi-container Docker applications. It defines the services for Jaffnakid, Wellawattakid, and an Nginx load balancer that balances traffic between the two services.

### `nginx.conf`
This file contains the Nginx configuration for load balancing between the Jaffnakid and Wellawattakid services.

### `jaffnakid/`
This folder contains the Python application code, the required dependencies (`requirements.txt`), and the `Dockerfile` to build the Docker image for the Jaffnakid service.

### `wellawattakid/`
This folder contains the Python application code, the required dependencies (`requirements.txt`), and the `Dockerfile` to build the Docker image for the Wellawattakid service.

## Requirements

- Docker
- Docker Compose

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/docker_learn.git
   cd docker_learn
