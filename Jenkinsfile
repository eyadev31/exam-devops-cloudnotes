pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'echo "Construction de l image Docker cloudnotes:v1"'
                sh 'echo "docker build -t cloudnotes:v1 ."'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo "Installation des dépendances Python"'
                sh 'echo "pip install -r requirements.txt"'
                sh 'echo "Exécution des tests Python"'
                sh 'echo "pytest"'
                sh 'echo "Tests réussis"'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'echo "Déploiement simulé de CloudNotes"'
                sh 'echo "Application déployée avec succès"'
            }
        }
    }
}
