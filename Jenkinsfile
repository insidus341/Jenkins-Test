pipeline {
 agent none
 
 environment {
  TEST_SECRET   = credentials("jenkins-test-secret-1")
 }
  
 stages {
  stage ('Lint') {
   steps {
    echo $TEST_SECRET
   }
  }
    
  stage ('Build') {
   steps {
   }
  }
 }
}
