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
        stage ('Init') {
            steps {
                script {
                    sh """
                    python -V
                    """
                }
            }
        }

        stage('Lint and Test') {
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
            when {

            }

            steps {
                // sh "docker build -t $registry ."
                script {
                    dockerImage = docker.build registry + ":beta-$BUILD_NUMBER"
                }
            }
        }

        stage('Run Docker Image (Pull request)') {
            // when {
            //     env.CHANGE_ID != null
            // }

            steps {
                script {
                    dockerImage.inside {
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

        stage ('Push container to Docker Hub (Development)') {
            when {
                branch "development"
            }

            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                        dockerImage.push("beta")
                    }
                    // docker.image(registry + ":$BUILD_NUMBER").push()
                }
            }
        }
    }
}
