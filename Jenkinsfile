// pipeline {
//   agent any
    
//     environment {
//         PYTHON_VERSION = '3.9'
//     }
    
//     options {
//         buildDiscarder(logRotator(numToKeepStr: '10'))
//         timeout(time: 30, unit: 'MINUTES')
//     }
    
//   stages {
//         stage('Git Checkout') {
//             steps {
//                 echo '📥 Checking out code from Git...'
//                 checkout scm
                
//                 script {
//                     env.GIT_COMMIT_SHORT = sh(
//                         script: 'git rev-parse --short HEAD',
//                         returnStdout: true
//                     ).trim()
                    
//                     env.GIT_BRANCH = sh(
//                         script: 'git rev-parse --abbrev-ref HEAD',
//                         returnStdout: true
//                     ).trim()
//                 }
                
//                 echo "✅ Checked out commit: ${env.GIT_COMMIT_SHORT} from branch: ${env.GIT_BRANCH}"
//             }
//         }
        
//         stage('Environment Setup') {
//             steps {
//                 echo '🔧 Setting up Python environment...'
                
//                 sh '''
//                     # Check if Python is available
//                     if ! command -v python3 &> /dev/null; then
//                         echo "Python3 not found. Trying to install Python..."
                        
//                         # Try to install Python without sudo (for Docker/containerized Jenkins)
//                         if command -v apt-get &> /dev/null; then
//                             echo "Installing Python3 using apt-get (no sudo)..."
//                             apt-get update
//                             apt-get install -y python3 python3-pip python3-venv
//                         # Try to install Python on CentOS/RHEL without sudo
//                         elif command -v yum &> /dev/null; then
//                             echo "Installing Python3 using yum (no sudo)..."
//                             yum install -y python3 python3-pip
//                         # Try to install Python on Alpine without sudo
//                         elif command -v apk &> /dev/null; then
//                             echo "Installing Python3 using apk (no sudo)..."
//                             apk add --no-cache python3 py3-pip
//                         else
//                             echo "❌ Cannot install Python automatically. Please install Python 3.9+ manually."
//                             echo "Available commands:"
//                             which apt-get yum apk brew || echo "No package manager found"
//                             exit 1
//                         fi
//                     fi
                    
//                     python3 --version
//                     python3 -m venv venv
//                     source venv/bin/activate
//                     pip install --upgrade pip
//                 '''
                
//                 echo '✅ Environment setup completed'
//             }
//         }
        
//         stage('Install Dependencies') {
//             steps {
//                 echo '📦 Installing dependencies...'
                
//                 sh '''
//                     source venv/bin/activate
                    
//                     # Install pytest and basic dependencies
//                     pip install pytest pytest-cov pytest-html
                    
//                     # Install project dependencies if requirements.txt exists
//                     if [ -f "requirements.txt" ]; then
//                         echo "Installing project requirements..."
//                         pip install -r requirements.txt
//                     fi
                    
//                     # Install test dependencies if test-requirements.txt exists
//                     if [ -f "test-requirements.txt" ]; then
//                         echo "Installing test requirements..."
//                         pip install -r test-requirements.txt
//                     fi
//                 '''
                
//                 echo '✅ Dependencies installed successfully'
//             }
//         }
        
//         stage('Run Tests') {
//             steps {
//                 echo '🧪 Running pytest tests...'
                
//                 sh '''
//                     source venv/bin/activate
                    
//                     # Check if tests directory exists
//                     if [ -d "tests" ]; then
//                         echo "Running tests from tests directory..."
//                         python -m pytest tests/ \
//                             --junitxml=test-results.xml \
//                             --html=test-report.html \
//                             --self-contained-html \
//                             --cov=. \
//                             --cov-report=xml:coverage.xml \
//                             --cov-report=html:htmlcov \
//                             -v
//                     else
//                         echo "No tests directory found. Creating a simple test..."
//                         mkdir -p tests
//                         cat > tests/test_basic.py << 'EOF'
// import pytest

// def test_basic():
//     """Basic test to ensure pytest is working."""
//     assert True

// def test_addition():
//     """Test basic arithmetic."""
//     assert 2 + 2 == 4

// def test_string():
//     """Test string operations."""
//     assert "hello" == "hello"

// def test_list():
//     """Test list operations."""
//     my_list = [1, 2, 3]
//     assert len(my_list) == 3
//     assert 2 in my_list
// EOF
                        
//                         echo "Running basic tests..."
//                         python -m pytest tests/ \
//                             --junitxml=test-results.xml \
//                             --html=test-report.html \
//                             --self-contained-html \
//                             -v
//                     fi
//                 '''
//             }
            
//             post {
//                 always {
//                     publishTestResults testResultsPattern: 'test-results.xml'
//                     publishHTML([
//                         allowMissing: false,
//                         alwaysLinkToLastBuild: true,
//                         keepAll: true,
//                         reportDir: '.',
//                         reportFiles: 'test-report.html',
//                         reportName: 'Test Report'
//                     ])
//                 }
//             }
//         }
        
//         stage('Build Artifacts') {
//             steps {
//                 echo '🏗️ Creating build artifacts...'
                
//                 sh '''
//                     mkdir -p build
                    
//                     # Copy test results
//                     cp test-results.xml build/ 2>/dev/null || echo "No test results found"
//                     cp test-report.html build/ 2>/dev/null || echo "No test report found"
//                     cp coverage.xml build/ 2>/dev/null || echo "No coverage report found"
                    
//                     # Copy project files
//                     cp package.json build/ 2>/dev/null || echo "No package.json found"
//                     cp requirements.txt build/ 2>/dev/null || echo "No requirements.txt found"
                    
//                     # Create build info
//                     echo "Build completed at $(date)" > build/build-info.txt
//                     echo "Git Commit: ${GIT_COMMIT_SHORT}" >> build/build-info.txt
//                     echo "Git Branch: ${GIT_BRANCH}" >> build/build-info.txt
//                     echo "Build Number: ${BUILD_NUMBER}" >> build/build-info.txt
//                 '''
                
//                 echo '✅ Build artifacts created successfully'
//             }
            
//             post {
//                 always {
//                     archiveArtifacts artifacts: 'build/**/*', fingerprint: true
//                     archiveArtifacts artifacts: 'test-results.xml', fingerprint: true
//                     archiveArtifacts artifacts: 'test-report.html', fingerprint: true
//                     archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
//                 }
//             }
//         }
//     }
    
//     post {
//         always {
//             echo '🧹 Cleaning up workspace...'
//         }
        
//         success {
//             echo '🎉 Pipeline completed successfully!'
            
//             script {
//                 def successMessage = """
//                 ✅ Automated Testing Success!
                
//                 Build Number: ${env.BUILD_NUMBER}
//                 Git Commit: ${env.GIT_COMMIT_SHORT}
//                 Git Branch: ${env.GIT_BRANCH}
//                 Build URL: ${env.BUILD_URL}
                
//                 All tests passed successfully!
//                 """
                
//                 echo successMessage
//             }
//         }
        
//         failure {
//             echo '💥 Pipeline failed!'
            
//             script {
//                 def failureMessage = """
//                 ❌ Automated Testing Failed!
                
//                 Build Number: ${env.BUILD_NUMBER}
//                 Git Commit: ${env.GIT_COMMIT_SHORT}
//                 Git Branch: ${env.GIT_BRANCH}
//                 Build URL: ${env.BUILD_URL}
                
//                 Please check the build logs for details.
//                 """
                
//                 echo failureMessage
//             }
//         }
        
//         unstable {
//             echo '⚠️ Pipeline completed with warnings!'
//         }
//   }
// }


pipeline {
  agent any
  options { timestamps() }
  triggers { pollSCM('H/5 * * * *') }   // switch to webhook later if you want

  environment {
    IMAGE      = 'myapp'
    TAG_LATEST = 'latest'
    CONTAINER  = 'myapp'
    HOST_PORT  = '8000'
    APP_PORT   = '8000'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'pwd && ls -la'
      }
    }

    stage('Test: pytest (in Python container)') {
      steps {
        sh '''
          set -eux
          mkdir -p reports
          # Ensure there is at least one test so JUnit exists
          [ -d tests ] || (mkdir -p tests && echo "def test_ok(): assert True" > tests/test_smoke.py)
          docker run --rm -v "$PWD":/work -w /work python:3.11-slim sh -lc "
            python -V &&
            python -m pip install --upgrade pip &&
            if [ -f requirements.txt ]; then pip install -r requirements.txt; else pip install pytest pytest-cov flask build; fi &&
            pytest -q --maxfail=1 --disable-warnings --junitxml=reports/junit.xml
          "
        '''
      }
    }

    stage('Build (optional Python package)') {
      steps {
        sh '''
          set -eux
          docker run --rm -v "$PWD":/work -w /work python:3.11-slim sh -lc "
            python -m pip install --upgrade pip build || pip install build &&
            if [ -f pyproject.toml ] || [ -f setup.cfg ] || [ -f setup.py ]; then
              python -m build
            else
              echo 'No Python packaging files; skipping.'
            fi
          "
        '''
      }
    }

    stage('Build Docker image') {
      steps {
        sh '''
          if [ -f Dockerfile ]; then
            docker build -t '"${IMAGE}:${BUILD_NUMBER}"' -t '"${IMAGE}:${TAG_LATEST}"' .
          else
            echo "No Dockerfile found; skipping image build."; exit 1
          fi
        '''
      }
    }

    stage('Deploy (run container)') {
      steps {
        sh '''
          docker rm -f '"${CONTAINER}"' || true
          docker run -d --name '"${CONTAINER}"' -p '"${HOST_PORT}:${APP_PORT}"' '"${IMAGE}:${TAG_LATEST}"'
        '''
      }
    }
  }

  post {
    always {
      junit testResults: 'reports/*.xml', allowEmptyResults: true
      archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
    }
    success { echo "✅ Git → pytest → build → Docker deploy → done. Open http://localhost:${HOST_PORT}/" }
    failure { echo "❌ Failed. Scroll up to the first error (Checkout/Test/Build)." }
  }
}
