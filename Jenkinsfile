pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build' // Run build in a docker container
        }
 
//  environment {
//  }
  
    stages {
        stage ('Lint') {
            steps {
                sh """
                pylint **/*.py
                """
            }
        }

        stage ('PyTest') {
            steps {
                sh """
                pytest
                """
            }
        }
    }
}
