pipeline {
 agent any
 
 environment {
  TEST_SECRET   = credentials("jenkins-test-secret-1")
 }
  
 stages {
  stage ('Lint') {
   steps {
    echo "HELLO"
   }
  }
  stage ('Build') {
   agent {
    dockerfile true
   }
   steps {
    sh 'echo $CUSTOM_ENV'
   }
  }
 }
}
