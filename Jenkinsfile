pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "madeeha2520/flask-mysql-app:latest"
        DOCKER_USER = credentials('docker-hub-username')
        DOCKER_PASS = credentials('docker-hub-password')
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/madeeha2520/flask-mysql-app'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $DOCKER_IMAGE
                '''
            }
        }
        
        stage('Deploy MySQL to Kubernetes') {
            steps {
                sh 'kubectl apply -f mysql-deployment.yaml'
                sh 'kubectl rollout status deployment/mysql'
            }
        }
        
        stage('Deploy Flask App to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
                sh 'kubectl rollout status deployment/flask-app'
            }
        }
        
        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods'
                sh 'kubectl get svc'
            }
        }
    }
}
