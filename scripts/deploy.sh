#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Authenticate with Google Cloud
echo "Authenticating with Google Cloud..."
gcloud auth activate-service-account --key-file=${GCP_SERVICE_ACCOUNT_KEY}
gcloud config set project ${GCP_PROJECT_ID}

# Build and push Docker images
echo "Building and pushing Docker images..."
docker build -t gcr.io/${GCP_PROJECT_ID}/backend:latest ./backend
docker push gcr.io/${GCP_PROJECT_ID}/backend:latest

# Deploy backend to Google Cloud Run
echo "Deploying backend to Google Cloud Run..."
gcloud run deploy backend \
    --image gcr.io/${GCP_PROJECT_ID}/backend:latest \
    --platform managed \
    --region ${GCP_REGION} \
    --allow-unauthenticated

# Deploy frontend to Google Cloud Storage
echo "Deploying frontend to Google Cloud Storage..."
gsutil rsync -R ./frontend/build gs://${GCP_FRONTEND_BUCKET}

# Update load balancer and DNS settings
echo "Updating load balancer and DNS settings..."
gcloud compute url-maps import ${GCP_URL_MAP_NAME} --source=${GCP_URL_MAP_CONFIG}
gcloud dns record-sets transaction start --zone=${GCP_DNS_ZONE}
gcloud dns record-sets transaction add ${BACKEND_IP} --name=${BACKEND_DOMAIN} --ttl=300 --type=A --zone=${GCP_DNS_ZONE}
gcloud dns record-sets transaction add ${FRONTEND_IP} --name=${FRONTEND_DOMAIN} --ttl=300 --type=A --zone=${GCP_DNS_ZONE}
gcloud dns record-sets transaction execute --zone=${GCP_DNS_ZONE}

# Run post-deployment tests
echo "Running post-deployment tests..."
# HUMAN ASSISTANCE NEEDED
# Add specific post-deployment test commands here. These could include:
# - Curl commands to check if endpoints are responding
# - Integration tests
# - Performance tests
# Example:
# curl -f https://${BACKEND_DOMAIN}/health
# npm run integration-tests
# ./performance-test.sh

echo "Deployment completed successfully!"