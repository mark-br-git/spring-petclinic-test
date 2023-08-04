pipeline {
    agent any
    
    stages {
        stage('Checkout') {
          steps {
          // Checkout your source code from version control
                checkout([$class: 'GitSCM',
                     branches: [[name: 'main']],
                     userRemoteConfigs: [[url: 'https://github.com/mark-br-git/spring-petclinic-test.git']]])
          }
        }
          
        stage('Build Docker Image') {
            steps {
                script {
                    // Define Docker Hub repository and image name
                    def dockerRepo = 'mark67br/main'
                    def imageName = "${dockerRepo}:${env.GIT_COMMIT.take(7)}"

                    // Build the Docker image with the GIT_COMMIT (short) tag
                    sh "docker build -t ${imageName} ."

                    // Log in to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh "docker login -u ${DOCKERHUB_USERNAME} -p ${DOCKERHUB_PASSWORD}"
                    }

                    // Push the Docker image to Docker Hub repository
                    sh "docker push ${imageName}"
                }
            }
        }
    }
}
