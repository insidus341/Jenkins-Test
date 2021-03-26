pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build' // Run build in a docker container
        }
    }

    // stages {
    //     stage('Lint') {
    //         steps {
    //             sh "pylint3 **/*.py"
    //         }
    //     }

    //     stage('PyTest') {
    //         steps {
    //             sh "pytest"
    //         }
    //     }
    // }

    stages {
        stage ('Lint and Test') {
            parallel {
                stage('Lint') {
                    steps {
                        sh "pylint3 **/*.py"
                    }
                }

                stage('PyTest') {
                    steps {
                        sh "pytest"
                    }
                }
            }
        }
    }
}
