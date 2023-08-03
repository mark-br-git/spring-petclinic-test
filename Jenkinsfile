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
  
        stage('Build') {
            steps {
                // Build the project using Maven
                sh 'mvn clean install'
            }
        }
    }
}
