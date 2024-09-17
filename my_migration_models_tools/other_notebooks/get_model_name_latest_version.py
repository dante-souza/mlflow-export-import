# Databricks notebook source
# MAGIC %pip install mlflow==2.5.0 -q
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import mlflow
from mlflow.tracking import MlflowClient

# COMMAND ----------

# registry_uri_GCP_DEV = "databricks://gcp_mlflow_dev:mlflow_dev_gcp"
registry_uri_GCP_DEV = "databricks"
mlflow.set_tracking_uri(registry_uri_GCP_DEV)
mlflow.set_registry_uri(registry_uri_GCP_DEV)
client = MlflowClient()

# COMMAND ----------

registered_models = client.search_registered_models()
model_names = [model.name for model in registered_models]
model_names

# COMMAND ----------

latest_versions = {}
for model in registered_models:
    model_name = model.name
    model_versions = client.search_model_versions(f"name='{model_name}'")
    if model_versions:
        latest_version = max(model_versions, key=lambda mv: int(mv.version))
        latest_versions[model_name] = latest_version.version
    else:
        latest_versions[model_name] = None


# COMMAND ----------

latest_versions

# COMMAND ----------


