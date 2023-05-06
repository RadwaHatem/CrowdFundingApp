pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git(url: 'https://github.com/RadwaHatem/CrowdFundingApp', branch: 'main')
            }
        }
        stage('List files') {
            steps {
                sh 'ls'
            }
        }
    }
}

