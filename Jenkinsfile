node("master"){
    git credentialsId: 'git_unittest_credencialid',url:'https://github.com/ChesonHuang/Unittest_P.git',branch:env.BRANCH_NAME

    stage('Testing'){
        sh "python3 run.py"
    }
    stage('archive'){
        archiveArtifacts allowEmptyArchive:true,artifacts:'Log/*'
    }

}