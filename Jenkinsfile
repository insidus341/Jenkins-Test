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

        stage('Lint and Unittests') {
            parallel {
                stage ('PyLint') {
                    steps {
                        sh "pylint3 /app/**/*.py"
                    }
                }
                stage('PyTest') {
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
                    def docker_app
                    docker_app = docker.image(registry + ":$BUILD_NUMBER").run()
                    // docker.image(registry + ":$BUILD_NUMBER").inside {
                    docker_app.inside {
                        sh "ls -lsa"
                        sh "ls -lsa run/"
                        sh "ls -lsa /"
                        sh "ls -lsa /app"
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
