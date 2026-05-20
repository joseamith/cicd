pipeline {
    agent any

    environment {
        IMAGE_NAME = "joseamith/task-api"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'

                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG ./app'
            }
        }

        stage('DockerHub Login') {
            steps {

                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'

                }
            }
        }

        stage('Push Docker Image') {
            steps {

                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'

            }
        }

    }
}
