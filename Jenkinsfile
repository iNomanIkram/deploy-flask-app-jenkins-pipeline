pipeline {
    agent any
    stages {
        stage('docker build') {
            steps {
                sh 'docker build . -t nomanikram/flask-app'
            }
        }

        stage('docker stop running') {
            steps {
                sh 'docker rm -f flask || echo "container does not exist"'
            }
        }

        stage('docker run') {
            steps {
                sh 'docker run --name flask --rm -d -p 5000:5000 nomanikram/flask-app'
            }
        }
    }
}
