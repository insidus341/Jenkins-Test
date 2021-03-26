pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build' // Run build in a docker container
        }
    }

    // stages {
    //     

    //     stage('PyTest') {
    //         steps {
    //             sh "pytest"
    //         }
    //     }
    // }

    stages {
        stage('Lint') {
            steps {
                sh "pylint3 **/*.py"
            }
        }
        stage ('PyTest') {
            parallel {
                stage('Run PyTest') {
                    steps {
                        sh "pytest"
                    }
                }
                stage('Test Coverage') {
                    steps {
                        sh "pytest --cov=run"
                    }
                }
            }
        }
    }
}
