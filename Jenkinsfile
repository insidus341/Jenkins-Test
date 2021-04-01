pipeline {
    environment{
        registry = "insidus341/jenkins_test"
        registryCredential = "DockerHub"
    }

    agent {
        dockerfile {
            filename 'Dockerfile.build' // Run build in a docker container
            args "-u root"
            // args '-u root:root'
        }
        
        // docker {
        //     image "python:3.9"
        // }
    }

    // agent any

    stages {  
        // def app
              
        stage ('Init') {
            steps {
                script {
                    sh """
                    python -V
                    """
                }
            }
        }

        stage('Lint and run tests') {
            parallel {
                stage ('PyLint') {
                    steps {
                        sh "pylint3 /app/**/*.py"
                    }
                }
                stage('Run Tests') {
                    steps {
                        sh "pytest --cov=run /app/"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            // when {
            //     branch "development"
            // }

            steps {
                // sh "docker build -t $registry ."
                script {
                    docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Run Docker Image') {
            steps {
                script {
                    // docker_app.inside {
                    //     sh "sleep 5; cat /app/output.txt"
                    // }
                    docker.image(registry + ":$BUILD_NUMBER").inside {
                        sh "ls -lsa"
                        sh "pwd"
                        sh "sleep 5; cat /app/output.txt"
                    }
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
