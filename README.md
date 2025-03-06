# docker_learn


# Flask Multi-Service Docker Setup

This repository contains a Docker-based setup for running multiple Flask services (`jaffnakid` and `wellawattakid`) behind an Nginx reverse proxy.

## 📂 Project Structure
#Folder Structure

project-root/
│── docker-compose.yml
│── nginx.conf
│── jaffnakid/
│   ├── app.py
│   ├── Dockerfile
│── wellawattakid/
│   ├── app.py
│   ├── Dockerfile
