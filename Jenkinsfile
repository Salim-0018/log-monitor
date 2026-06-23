pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                echo 'Pulling code from GitHub'
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/log-monitor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image'
                sh 'docker build -t log-monitor .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop log-monitor-app || true'
                sh 'docker rm log-monitor-app || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name log-monitor-app log-monitor'
            }
        }
    }
}
