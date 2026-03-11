#!/bin/bash
#Variables
SA_NAME="dev-deployer"
PROJECT_ID="gcp-cloud-engineer-curso01"

#Create Service Account
gcloud iam service-accounts create $SA_NAME --display-name "Deployer SA"
#Grant permissions to the Service Account
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member "serviceAccount:$SA_NAME@$PROJECT_ID.iam.gserviceaccount.com"\
    --role "roles/compute.viewer"
    