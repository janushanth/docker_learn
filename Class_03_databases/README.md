# Class 03: Databases

This folder contains a setup for running MongoDB and Mongo-Express using Docker Compose.

## 📂 Folder Structure

```
Class_03_databases/
│── docker-compose.yml            # Docker Compose file to orchestrate MongoDB and Mongo-Express
│── README.md                     # Documentation for the database setup
```

## Description

This class demonstrates how to set up MongoDB and Mongo-Express using Docker Compose.

### `docker-compose.yml`
This is the main configuration file to define and run multi-container Docker applications. It defines the services for MongoDB and Mongo-Express.

## Requirements

- Docker
- Docker Compose

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/janushanth/docker_learn.git
   cd docker_learn/Class_03_databases
   ```

2. Build and start the Docker containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. Access Mongo-Express at `http://localhost:8081`.

## Useful Commands

- Default credentials for Mongo-Express: `admin:pass`
- Ping MongoDB from Mongo-Express:

  ```bash
  docker exec -it mongo-express ping mongodb
  ```

- Ping Mongo-Express from MongoDB:

  ```bash
  docker exec -it mongodb ping mongo-express
  ```

- View logs for MongoDB:

  ```bash
  docker logs mongodb
  ```

- View logs for Mongo-Express:

  ```bash
  docker logs mongo-express
  ```

- Access MongoDB shell:

  ```bash
  docker exec -it mongodb mongosh -u root -p example --authenticationDatabase admin --eval "show databases"
  ```

## License

This project is licensed under the MIT License.
