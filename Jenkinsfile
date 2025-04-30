pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_DIR = "${WORKSPACE}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Containers') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
