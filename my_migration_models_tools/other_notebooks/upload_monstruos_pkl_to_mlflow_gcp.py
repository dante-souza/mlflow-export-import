# Databricks notebook source
# MAGIC %pip install mlflow -q
# MAGIC %pip install --upgrade "mlflow-skinny[databricks]>=2.5.0" -q
# MAGIC %pip install feature-engine==0.6.0 -q
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import mlflow
from mlflow.tracking.client import MlflowClient
from pathlib import Path
import pickle
import pandas as pd
import feature_engine.missing_data_imputers as mdi
import feature_engine.categorical_encoders as ce

# COMMAND ----------

scope = "gcp_mlflow_prd"
scope_key = "mlflow_prd_gcp"
registry_uri_gcp_dev = f"databricks://{scope}:{scope_key}"
mlflow.set_tracking_uri(registry_uri_gcp_dev)
mlflow.set_registry_uri(registry_uri_gcp_dev)
path_experiment_dev = "/Users/dante.souza@viavarejo.com.br/crm_nbo"
path_experiment = "/dbfs/Volumes/machine_learning_prd/models/crm_nbo"
mlflow.set_experiment(path_experiment)
client = MlflowClient(registry_uri=registry_uri_gcp_dev, tracking_uri=registry_uri_gcp_dev)

# COMMAND ----------

registered_models = client.search_registered_models()

# Print model names
for model in registered_models:
    print(model.name)

# COMMAND ----------

pkl_path = "/dbfs/mnt/gen2ds/app/analytics/models/prod/"
crm_nbo_pkl_path = list(Path(pkl_path).glob("crm_nbo.pkl"))[0]
crm_nbo_pkl_path

# COMMAND ----------

model = pd.read_pickle(crm_nbo_pkl_path)
model

# COMMAND ----------

with open(crm_nbo_pkl_path, "rb") as f:
    model_from_openfile = pickle.load(f)

# COMMAND ----------

with mlflow.start_run() as run:
    # Log the scikit-learn model
    mlflow.sklearn.log_model(model_from_openfile, "crm_nbo")
    run_id = run.info.run_id
