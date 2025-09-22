pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'mwaghmodepersistent'
        IMAGE_NAME     = 'calculatorapp'
        IMAGE_TAG      = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Assuming Dockerfile is in root of repo
                    sh "docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run a test: e.g. add 2 + 3 => 5
                    sh '''
                        RESULT=$(docker run --rm ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} 2 3 add)
                        echo "Output was: $RESULT"
                        echo "$RESULT" | grep -q "Result: 5"
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        always {
            sh "docker logout || true"
        }
        success {
            echo "Successfully built & pushed: ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
        }
    }
}
