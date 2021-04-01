pipeline {
    environment{
        registry = "insidus341/jenkins_test"
        registryCredential = "DockerHub"
        main_branch = "main"
        development_branch = "development"
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
                echo "CHANGE_ID = ${env.CHANGE_ID}"
                echo "BRANCH_NAME = ${env.BRANCH_NAME}"
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
            // when {

            // }

            steps {
                // sh "docker build -t $registry ."
                script {
                    dockerImage = docker.build registry + ":beta-$BUILD_NUMBER"
                }
            }
        }

        stage('Run Docker Image (Pull request)') {
            when {
                expression {
                    env.CHANGE_ID && env.BRANCH_NAME.startsWith("PR-")
                }
            }

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
                expression {
                    env.BRANCH_NAME == development_branch
                }
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
