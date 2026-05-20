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

        stage('Push Docker Image') {
            steps {
                echo 'Pushing image to DockerHub...'

                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

    }
}
