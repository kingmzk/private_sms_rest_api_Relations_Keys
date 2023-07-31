pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your_username/your_python_app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                // Perform any other build-related steps here if necessary
                // For example, you can create directories, compile assets, etc.
                sh 'echo "Building the Python application..."'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }
    }

    post {
        always {
            // Clean up artifacts or perform any other cleanup tasks if needed
        }

        success {
            archiveArtifacts artifacts: 'your_python_app/**', excludes: 'your_python_app/.git/**'
            // Archive the entire contents of the 'your_python_app' directory, excluding the .git folder
        }
    }
}
