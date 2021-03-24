pipeline {
 agent none
 
  environment {
    TEST_SECRET   = credentials("jenkins-test-secret-1")
  }
  
  stages {
    stage ('Lint') {
      echo $TEST_SECRET
    }
  }
}
