
======Jenkins=======
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

###Please Read the Jenkins files######
####artifactory#####
 artifactory username - jenkins  
artifactory password - Jenkins@123#
Create the Artifactory repo - docker-repo


#jenkins github id  for credentials - github-credentials

#jenkins artifactory id  for credentials - jfrog-credentials