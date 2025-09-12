# End-To-End-YouTube-Sentiment-Insights

An End-To-End DL Project From Data Ingestion, Preprocessing, EDA, Baseline Model,  TF-IDF, BOW, HPT, Data Version With (DVC), Experiment Tracking With (MLFlow), Flask App With Simple UI, Dockerizing The Entire Project, Start Deployment Using CI/CD Pipelines With (GitHub Actions) On AWS.

## Project Structure

```
End-To-End-YouTube-Sentiment-Insights
├── notebooks
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

## MLflow on AWS Setup:

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
export MLFLOW_TRACKING_URI=ec2-52-90-171-209.compute-1.amazonaws.com:5000
```
