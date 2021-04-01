pipeline {
    environment{
        registry = "insidus341/jenkins_test"
        registryCredential = "DockerHub"
    }

    // Run test steps in a docker container
    agent {
        dockerfile {
            filename 'Dockerfile.build' 
            args "-u root"
        }
    }

    stages {  
        def docker_image
        
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
                    docker_image = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Run Docker Image') {
            steps {
                script {
                    docker.image(registry + ":$BUILD_NUMBER").withRun('-u root --entrypoint /bin/bash') {
                        sh """
                        cd app/
                        pwd
                        ls -lsa
                        python3 app.py &
                        sleep 5; cat output.txt
                        """
                    }
                }
            }
        }

        stage ('Push container to Docker Hub') {
            steps {
                script {
                    docker_image.push()
                }
            }
        }
    }
}
