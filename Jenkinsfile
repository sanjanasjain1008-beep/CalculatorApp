pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', url: 'https://github.com/mayurwaghmode/CalculatorApp.git'
            }
        stage('Run Calculator') {
            steps {
                script {
                    // Run Python script with Jenkins parameters
                    sh "python3 calculator.py 5 6 add"
                }
            }
        }            
        }
    }
}
