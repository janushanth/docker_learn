# docker_learn

# Docker Basics

Docker is a containerization platform that allows developers to package applications along with their dependencies into lightweight containers. Below are some essential Docker commands with explanations.

## Installing Docker

Follow the official Docker installation guide for your OS: [Docker Installation Guide](https://docs.docker.com/get-docker/)

## Common Docker Commands

### 1. Check Docker Version
```sh
docker --version
```
**Explanation:** Checks the installed Docker version.

### 2. Pull a Docker Image
```sh
docker pull <image_name>
```
**Example:**
```sh
docker pull nginx
```
**Explanation:** Downloads the specified image from Docker Hub.

### 3. List Docker Images
```sh
docker images
```
**Explanation:** Displays all locally available Docker images.

### 4. Run a Docker Container
```sh
docker run -d --name <container_name> -p <host_port>:<container_port> <image_name>
```
**Example:**
```sh
docker run -d --name my_nginx -p 8080:80 nginx
```
**Explanation:** Runs an Nginx container in detached mode (`-d`), assigns it a name (`--name`), and maps port 8080 on the host to port 80 in the container.

### 5. List Running Containers
```sh
docker ps
```
**Explanation:** Shows all currently running containers.

### 6. List All Containers (Including Stopped)
```sh
docker ps -a
```
**Explanation:** Displays all containers, including stopped ones.

### 7. Stop a Running Container
```sh
docker stop <container_id_or_name>
```
**Example:**
```sh
docker stop my_nginx
```
**Explanation:** Stops the specified container.

### 8. Remove a Container
```sh
docker rm <container_id_or_name>
```
**Example:**
```sh
docker rm my_nginx
```
**Explanation:** Deletes the specified container. Ensure it is stopped before removing.

### 9. Remove an Image
```sh
docker rmi <image_id_or_name>
```
**Example:**
```sh
docker rmi nginx
```
**Explanation:** Deletes the specified image.

### 10. View Container Logs
```sh
docker logs <container_id_or_name>
```
**Example:**
```sh
docker logs my_nginx
```
**Explanation:** Shows logs for the specified container.

### 11. Execute Commands Inside a Running Container
```sh
docker exec -it <container_id_or_name> <command>
```
**Example:**
```sh
docker exec -it my_nginx sh
```
**Explanation:** Opens an interactive shell inside the container.

### 12. Build a Docker Image from a Dockerfile
```sh
docker build -t <image_name> .
```
**Example:**
```sh
docker build -t my_app .
```
**Explanation:** Builds an image from a `Dockerfile` in the current directory (`.`) and tags it as `my_app`.

### 13. Push an Image to Docker Hub
```sh
docker tag <image_name> <dockerhub_username>/<repo_name>
docker push <dockerhub_username>/<repo_name>
```
**Example:**
```sh
docker tag my_app mydockerhub/my_app
docker push mydockerhub/my_app
```
**Explanation:** Tags an image and pushes it to Docker Hub.

### 14. Remove Unused Containers and Images
```sh
docker system prune -a
```
**Explanation:** Cleans up unused containers, networks, and images.

## Conclusion
These are some basic Docker commands to get you started. For more details, refer to the [official Docker documentation](https://docs.docker.com/).


