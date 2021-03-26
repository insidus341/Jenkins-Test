pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build' // Run build in a docker container
        }
    }

    stages {
        stage('Lint') {
            steps {
                sh "pylink **/*.py"
            }
        }

        stage('PyTest') {
            steps {
                sh "pytest"
            }
        }
    }
}
