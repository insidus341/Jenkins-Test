pipeline {
 agent any
 
 environment {
  TEST_SECRET   = credentials("jenkins-test-secret-1")
 }
  
 stages {
  stage ('Lint') {
   steps {
    echo "HELLO"
    echo $TEST_SECRET
   }
  }
 }
}
