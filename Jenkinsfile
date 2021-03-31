pipeline {
    environment{
        registry = "insidus341/jenkins_test"
        registryCredential = "DockerHub"
    }

    agent {
        dockerfile {
            filename 'Dockerfile.build' // Run build in a docker container
        }
    }

    stages {
        stage('Lint') {
            steps {
                sh "pylint3 **/*.py"
            }
        }
        stage('Run Tests') {
            steps {
                sh "pytest --cov=run"
            }
        }            
        stage ('Build') {
            steps {
                script {
                    docker.build registry + ":$BUILD_NuMBER"
                }
            }
        }
    }
}
