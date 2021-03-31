pipeline {
    environment{
        registry = "insidus341/jenkins_test"
        registryCredential = "DockerHub"
    }

    agent {
        dockerfile {
            filename 'Dockerfile.build' // Run build in a docker container
            // args '-u root:root'
        }
    }

    stages {        
        stage ('Init') {
            steps {
                script {
                    sh """
                    pwd
                    """
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

        stage('Build for Development') {
            // when {
            //     branch "development"
            // }
            agent none

            steps {
                // sh "docker build -t $registry ."
                script {
                    docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }       
        // stage ('Build') {
        //     agent any
        //     steps {
        //         script {
        //             docker.build registry + ":$BUILD_NUMBER"
        //         }
        //     }
        // }
    }
}
