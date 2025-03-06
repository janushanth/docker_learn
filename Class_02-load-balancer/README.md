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



Description:
1) docker-compose.yml: The main configuration file to define and run multi-container Docker applications, including the Jaffnakid, Wellawattakid, and Nginx load balancer services.
2) nginx.conf: Nginx configuration for load balancing between the two services.
3) jaffnakid/: Folder containing the Python application code, dependencies, and Dockerfile for the Jaffnakid service.
4) wellawattakid/: Folder containing the Python application code, dependencies, and Dockerfile for the Wellawattakid service.