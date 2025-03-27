# JFrog Artifactory Docker Setup

This repository contains the necessary configuration files to set up JFrog Artifactory OSS and PostgreSQL using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Files in this Repository

- **`docker-compose.yml`**: Defines the services for Artifactory and PostgreSQL.
- **`artifactory.key`**: Contains the master key for Artifactory encryption.
- **`system.yaml`**: Configuration file for Artifactory, including database connection details.

## Setup Instructions

1. **Generate a Master Key** (if not already present):
   ```bash
   openssl rand -hex 32 > artifactory.key
   echo $(openssl rand -hex 32) > artifactory.key

