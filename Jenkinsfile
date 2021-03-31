pipeline {
    environment{
        registry = "insidus341/jenkins_test"
        registryCredential = "DockerHub"
    }

    agent {
        // dockerfile {
        //     filename 'Dockerfile.build' // Run build in a docker container
        // }
        
        docker {
            image "python:3.9"
            args '-u root:root'
        }
    }

    stages {
        stage ('Init') {
            steps {
                script {
                    sh "apt-get update && apt-get install pylint3 python3-pip -y"
                }
            }
        }
        stage ('Checkout') {
            steps {
                checkout scm
                script {
                    sh "ls -lsa"
                }
            }
        }
        stage ('Install Dependencies') {
            steps {
                script {
                    sh "pip3 install -r /deployment/requirements.txt"
                }
            }
        }
        stage('Lint') {
            steps {
                sh "pylint3 /app/**/*.py"
            }
        }
        stage('Run Tests') {
            steps {
                sh "pytest --cov=run /app/"
            }
        }            
        stage ('Build') {
            steps {
                script {
                    docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
    }
}
