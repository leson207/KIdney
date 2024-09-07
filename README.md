# Kidney

## Create environment

Clone the repository
```bash
git clone https://github.com/leson207/Kidney.git
```

Change directory
```bash
cd Kidney
```
Create conda environemnt
```bash
conda create -p venv python=3.9 -y
```
Active conda environment
``` bash
conda activate venv/
```
Install dependency packages
```bash
pip install -r requirements.txt
```

# Workflow
1. Update config/config.yaml
2. Update secretes.yaml [optional]
3. update params
4. update entity
5. update src/config/configuration.py/ConfigurationManager
6. update unpdate components
7. update pipeline
8. update main.py
9. update dvc.yaml
10. app.py

# Data Ingestion
Data link #link[https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone]

"https://drive.google.com/file/d/1vlhZ5c7abUKF8xXERIw6m9Te8fW7ohw3/view?usp=sharing"

# Dagshub

```bash
export MLFLOW_TRACKING_URI=

export MLFLOW_TRACKING_USER_NAME=

export MLFLOW_TRACKING_PASSWORD=
```

import dagshub
dagshub.init(repo_owner='leson207', repo_name='Kidney', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)