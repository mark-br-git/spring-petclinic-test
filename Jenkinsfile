pipeline {
    agent any
    
    stages {
        stage('Checkout') {
          steps {
          // Checkout your source code from version control
                checkout([$class: 'GitSCM',
                     branches: [[name: 'test']],
                     userRemoteConfigs: [[url: 'https://github.com/mark-br-git/spring-petclinic-test.git']]])
          }
        }
    
        stage('Generate Code Style Report') {
            steps {
                // Generate the code style report using Checkstyle 
                sh 'mvn checkstyle:checkstyle'
            }
            post {
                // Archive the code style report as a job artifact
                always {
                    archiveArtifacts 'target/checkstyle-result.xml'
                }
            }
        }
  
        stage('Tests') {
            steps {
                // Test the project using Maven
                sh 'mvn clean test'
            }
        }
      
        stage('Build without Tests') {
            steps {
                // Buduje projekt Maven pomijając testy
                sh 'mvn clean package -DskipTests=true'
            }
        }


          stage('Check User') {
            steps {                
                 sh 'echo $whoami'
            }
        }
    



        
        stage('Build Docker Image') {
            steps {
                script {
                    // Define Docker Hub repository and image name
                    def dockerRepo = 'mark67br/mr'
                    def imageName = "${dockerRepo}:${env.GIT_COMMIT.take(7)}"

                    // Build the Docker image with the GIT_COMMIT (short) tag
                    sh "docker build -t ${imageName} ."

                    // Log in to Docker Hub
       //             withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
        //            sh "docker login -u ${DOCKERHUB_USERNAME} -p ${DOCKERHUB_PASSWORD}"
         //           }

                    // Push the Docker image to Docker Hub repository
           //         sh "docker push ${imageName}"
                }
            }
        }
    }
}
