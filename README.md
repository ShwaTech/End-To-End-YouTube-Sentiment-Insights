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
