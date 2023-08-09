pipeline {
    agent any
 
    triggers {
        githubPush()
    }
 
    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }
 
        stage('Build') {
            steps {
                // Replace with your build steps
                sh 'echo "Building your project"'
            }
        }
 
        stage('Test') {
            steps {
                // Replace with your test steps
                sh 'echo "Running tests"'
            }
        }
    }
}
