# End-To-End-YouTube-Sentiment-Insights

An End-To-End DL Project From Data Ingestion, Preprocessing, EDA, Baseline Model,  TF-IDF, BOW, HPT, Data Version With (DVC), Experiment Tracking With (MLFlow), Flask App With Simple UI, Dockerizing The Entire Project, Start Deployment Using CI/CD Pipelines With (GitHub Actions) On AWS.

## Project Structure

```bash
End-To-End-YouTube-Sentiment-Insights
├── .dvc
│   ├── .gitignore
│   └── config
├── .github
│   └── workflows
│       └── cicd.yml
├── notebooks
│   ├── 01_Preprocessing_&_EDA.ipynb
│   ├── 02_Experiments_1_Baseline_Model.ipynb
│   ├── 03_Experiments_2_BoW_&_TF-IDF.ipynb
│   ├── 04_Experiments_3_TF-IDF_TriGram_MaxFeatures.ipynb
│   ├── 05_Experiments_4_Handling_Imbalanced_Data.ipynb
│   ├── 06_Experiments_5_XGBoost_With_HPT.ipynb
│   ├── 07_Experiments_6_LightGBM_Detailed_HPT.ipynb
│   └── 08_Stacking.ipynb
├── src
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   └── data_preprocessing.py
│   └── model
│       ├── __init__.py
│       ├── model_building.py
│       ├── model_evaluation.py
│       └── model_register.py
├── artifacts
├── flask_app
│   └── app.py
├── yt-chrome-plugin-frontend
│   ├── popup.html
│   ├── popup.js
│   └── manifest.json
├── setup.py
├── template.py
├── dvc.yaml
├── params.yaml
├── Dockerfile
├── .gitignore
├── README.md
└── requirements.txt
```

## Create a virtual environment

```bash
conda create -n mlops-env python=3.11 -y
conda activate mlops-env
pip install uv
uv pip install -r requirements.txt
```

## MLflow on AWS Setup ->

1. Login to AWS console.
2. Create IAM user with AdministratorAccess
3. Export the credentials in your AWS CLI by running "aws configure"
4. Create a s3 bucket
5. Create EC2 machine (Ubuntu) & add Security groups 5000 port

Run the following command on EC2 machine

```bash
sudo apt update

sudo apt install python3-pip

sudo apt install pipenv

sudo apt install virtualenv


mkdir mlflow

cd mlflow

pipenv install mlflow

pipenv install awscli

pipenv install boto3

pipenv shell


## Then set aws credentials
aws configure


#Finally 
mlflow server -h 0.0.0.0 --default-artifact-root s3://shwa-mlflow


#open Public IPv4 DNS to the port 5000


#set uri in your local terminal and in your code 
export MLFLOW_TRACKING_URI=ec2-54-227-97-154.compute-1.amazonaws.com:5000
```

## DVC Commands ->

```bash
dvc init

dvc repro

dvc dag
```

## Postman APIs Testing ->

```bash
https://web.postman.co/workspace/My-Workspace~dec3738d-d4c5-4633-8cd1-2766b8cddcbf/collection/31642766-a0e7066e-79aa-4648-a2a5-d89ac60e86fb?action=share&source=copy-link&creator=31642766
```

## Chrome Pulgin

1. Go to chrome://extensions/
2. Enable Developer mode
3. Click on Load unpacked
4. Select the yt-chrome-plugin-frontend folder
5. Open any youtube video and click on the extension icon
6. You should see the comment analysis summary and sentiment analysis results

## AWS-CICD-Deployment-with-Github-Actions

### 1. Login to AWS console

### 2. Create IAM user for deployment

#### Policy

 1. AmazonEC2ContainerRegistryFullAccess

 2. AmazonEC2FullAccess

#### with specific access

 1. EC2 access : It is virtual machine

 2. ECR : Elastic Container registry to save your docker image in aws

#### Description: About the deployment

 1. Build docker image of the source code

 2. Push your docker image to ECR

 3. Launch Your EC2

 4. Pull Your image from ECR in EC2

 5. Lauch your docker image in EC2

### 3. Create ECR repo to store/save docker image

- Save the URI: 047719640457.dkr.ecr.us-east-1.amazonaws.com/yt-sentiment

### 4. Create EC2 machine (Ubuntu)

### 5. Open EC2 and Install docker in EC2 Machine

#### Run the following commands in EC2 ->

```bash
 sudo apt-get update -y

 sudo apt-get upgrade -y
```

#### Required commands to install docker in EC2 ->

```bash
 curl -fsSL https://get.docker.com -o get-docker.sh

 sudo sh get-docker.sh

 sudo usermod -aG docker ubuntu

 newgrp docker
```

### 6. Configure EC2 as self-hosted runner

 1. Go to github > setting > actions > runner > new self-hosted runner
 2. Choose the os machine (Linux)
 3. Run the commands one by one
 4. Make Sure When You Run (Enter the name of runner -> self-hosted)

### 7. Setup github secrets

 AWS_ACCESS_KEY_ID = From >> yt-sentiment_accessKeys.csv

 AWS_SECRET_ACCESS_KEY = From >> mlflow.pem

 AWS_REGION = us-east-1

 AWS_ECR_LOGIN_URI = demo>>  047719640457.dkr.ecr.us-east-1.amazonaws.com

 ECR_REPOSITORY_NAME = yt-sentiment

 git config --global user.name "ShwaTech"
