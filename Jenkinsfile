pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build' // Run build in a docker container
        }
    }

    stages {
        stage('Lint') {
            steps {
                sh "pylint /app/**/*.py"
                sh "pylint /tests/**/*.py"
            }
        }

        stage('PyTest') {
            steps {
                sh "pytest"
            }
        }
    }
}
