pipeline {
    agent any

    environment {
        SSH_USER = 'root'  // Логин для сервера
        SSH_HOST = '89.104.69.234'  // IP удаленного сервера
        SSH_KEY = credentials('ssh-key')  // Jenkins credentials ID для SSH
        REPO_DIR = '/var/www/AllRussia-backend'  // Директория проекта на сервере
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'ssh-key', url: 'git@github.com:nsstnc/AllRussia-backend.git'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'chmod +x docker-bash.sh'
                    sh 'docker-compose down'
                    sh 'docker ps -aq | xargs -r docker rm -f'
                    sh 'docker-compose run --rm app python -m unittest discover -s backend/tests'
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                sshagent(['ssh-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no $SSH_USER@$SSH_HOST << 'EOF'
                        cd $REPO_DIR
                        git pull origin main
                        chmod +x docker-bash.sh
                        docker-compose down
                        docker-compose up --build -d
                        sudo systemctl restart nginx
                    EOF
                    """
                }
            }
        }
    }
}