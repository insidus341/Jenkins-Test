node {
    def app
    agent any

    stage('Clone respositry') {
        checkout svm
    }

    stage('Build image') {
        app = docker.build("insidus341/jenkins-test")
    }

    stage('Run Pylint3') {
        app.inside {
            sh "pylint3 **/*.py"
        }
    }

    stage('Run Tests') {
        app.inside {
            sh "pytest --cov=run"
        }
    } 
}