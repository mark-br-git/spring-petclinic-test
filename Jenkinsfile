pipeline {
    agent any
    
    stages {
        stage('Checkout') {
          steps {
        // Checkout your source code from version control
        // For example, using Git:
           git url: 'https://github.com/mark-br-git/spring-petclinic-test.git'
         }
    }
        stage('Build') {
            steps {
                // Build the project using Maven
                // Make sure to use the correct Maven installation name from step 2
                sh 'mvn clean install'
            }
        }
        
        stage('Generate Code Style Report') {
            steps {
                // Generate the code style report using Checkstyle (or any other tool you prefer)
                tool 'Maven'
                sh 'mvn checkstyle:checkstyle'
            }
            post {
                // Archive the code style report as a job artifact
                always {
                    archiveArtifacts 'target/checkstyle-result.xml'
                }
            }
        }
    }
}
