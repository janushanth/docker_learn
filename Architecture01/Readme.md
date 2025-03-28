
### Jenkins #####
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
Jenkins Login username - jenkinsadmin 
Jenkins Login password - jenkinsadmin
#default plugin install with git
Install plungin - Docker Pipeline ,Artifactory
Find the Artifactory section and click Add Artifactory Server.
Provide the necessary Artifactory URL, credentials, and repository details.

    2  apt-get update
    3  apt-get install -y docker.io
    4  docker --version

### Please Read the Jenkins files ######
#### artifactory #####
artifactory username - jenkins  
artifactory password - Jenkins@123#
Create the Artifactory repo - docker-repo


# jenkins github id  for credentials - github-credentials
# jenkins artifactory id  for credentials - jfrog-credentials
# nexus artifactory id  for credentials - nexus-credentials


### Nexus ####
docker exec nexus cat /nexus-data/admin.password
default username - admin
new password -nexusadmin
# Repository Typ - Hosted / Store your own Docker images (Push & Pull)
 Nexus artifactory username - jenkins  
nexus artifactory password - Jenkins@123#

Create the Artifactory repo - docker-repo
Create the Artifactory repo - helm-repo

docker login -u admin -p <your-password> http://localhost:8083
docker login -u admin -p nexusadmin http://localhost:8083
docker login -u jenkins -p Jenkins@123# http://localhost:8083



### Helm chart 

helm create python-app
#helm install nginx-ingress ingress-nginx/ingress-nginx

kubectl create namespace ingress-nginx
helm install nginx-ingress ingress-nginx/ingress-nginx --namespace ingress-nginx
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx

helm install python-app ./python-app
helm upgrade python-app ./python-app
helm uninstall python-app
helm list --all

kubectl get ingress
kubectl describe ingress python-app-ingress
kubectl get svc
kubectl port-forward svc/python-app 5000:5000
curl http://localhost:5000/api