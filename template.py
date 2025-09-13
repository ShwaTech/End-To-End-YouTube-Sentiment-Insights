import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    ".github/workflows/cicd.yaml",
    "flask_app/app.py",
    "yt-chrome-plugin-frontend/popup.html",
    "yt-chrome-plugin-frontend/popup.js",
    "yt-chrome-plugin-frontend/manifest.json",
    "src/__init__.py",
    "src/data/__init__.py",
    "src/data/data_ingestion.py",
    "src/data/data_preprocessing.py",
    "src/model/__init__.py",
    "src/model/model_building.py",
    "src/model/model_evaluation.py",
    "src/model/model_register.py",
    "params.yaml",
    "dvc.yaml",
    "app.py",
    "Dockerfile",
    "setup.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    
    else:
        logging.info(f"{filename} is already created")