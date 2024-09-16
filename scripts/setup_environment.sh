#!/bin/bash

# Check and install required dependencies
echo "Checking and installing required dependencies..."
if ! command -v python3 &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

if ! command -v node &> /dev/null; then
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

if ! command -v gcloud &> /dev/null; then
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
    sudo apt-get update && sudo apt-get install -y google-cloud-sdk
fi

# Set up virtual environments for Python
echo "Setting up virtual environment for Python..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install Node.js and npm packages
echo "Installing Node.js packages..."
npm install

# Configure Google Cloud SDK
echo "Configuring Google Cloud SDK..."
gcloud init

# Set up environment variables
echo "Setting up environment variables..."
cat << EOF > .env
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials.json
GOOGLE_CLOUD_PROJECT=your-project-id
FLASK_APP=app.py
FLASK_ENV=development
EOF

echo "Environment setup complete!"