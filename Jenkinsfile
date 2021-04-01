if (env.BRANCH_NAME == "jenkins_file_tests") {
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
                when {
                    expression {
                        (env.CHANGE_ID && env.BRANCH_NAME.startsWith("PR-")) || env.BRANCH_NAME == development_branch || env.BRANCH_NAME == main_branch
                    }
                }

                steps {
                    script {
                        dockerImage = docker.build registry + ":beta-$BUILD_NUMBER"
                    }
                }
            }

            stage('Run Docker Image') {
                when {
                    expression {
                        (env.CHANGE_ID && env.BRANCH_NAME.startsWith("PR-")) || env.BRANCH_NAME == development_branch || env.BRANCH_NAME == main_branch
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

            stage ('Push container to Docker Hub') {
                when {
                    expression {
                        env.BRANCH_NAME == development_branch || env.BRANCH_NAME == main_branch
                    }
                }

                steps {
                    script {
                        if (env.BRANCH_NAME == development_branch) {
                            docker.withRegistry('', registryCredential) {
                                dockerImage.push("beta-$BUILD_NUMBER")
                                dockerImage.push("beta")
                            }
                        }

                        if (env.BRANCH_NAME == main_branch) {
                            docker.withRegistry('', registryCredential) {
                                dockerImage.push("$BUILD_NUMBER")
                                dockerImage.push("latest")
                            }
                        }
                    }
                }
            }
        }
    }
}