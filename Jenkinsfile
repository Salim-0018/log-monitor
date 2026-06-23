pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Salim-0018/log-monitor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t log-monitor .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop log-monitor || true'
                sh 'docker rm log-monitor || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name log-monitor log-monitor'
            }
        }
    }
}
