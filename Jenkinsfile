pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Get code from GitHub repository
                git branch: 'main', url: 'https://github.com/mayurwaghmode/CalculatorApp.git'
            }
        }
        stage('Run Calculator') {
            steps {
                // Run Python script
                sh "python3 calculator.py 5 6 add"
            }
        }
    }
}
