node("master"){
    git credentialsId: 'git_unittest_credencialid',url:'https://github.com/ChesonHuang/Unittest_P.git'

    stage('Testing'){
        sh """
        chmod a+x run.py
        python run.py
        """
    }
    stage('archive'){
        archiveArtifacts artifacts:'Log/*'
    }

}
