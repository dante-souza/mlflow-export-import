# Databricks notebook source
# MAGIC %md
# MAGIC # Installation

# COMMAND ----------

# MAGIC %pip install --upgrade "mlflow-skinny[databricks]>=2.5.0" -q
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC # Imports

# COMMAND ----------

import mlflow
from mlflow.tracking.client import MlflowClient

# COMMAND ----------

# MAGIC %md
# MAGIC # Testing scopes connectivity

# COMMAND ----------

# MAGIC %md
# MAGIC ### MLFowDBS Workspace

# COMMAND ----------

registry_uri_MLFowDBS = "databricks://az_mlflowdbs_prd:az_mlflow_dbs"
mlflow.set_tracking_uri(registry_uri_MLFowDBS)
client = MlflowClient(registry_uri=registry_uri_MLFowDBS)

# List registered models
models = client.search_registered_models()

# Print the models
for model in models:
    print(f"Name: {model.name}")
    for version in model.latest_versions:
        print(f"  Version: {version.version}")
        print(f"  Stage: {version.current_stage}")
        print(f"  Source: {version.source}")
        print(f"  Run ID: {version.run_id}")
    print('*'*120)

# COMMAND ----------

# MAGIC %md
# MAGIC ### MLOpsDBS Workspace

# COMMAND ----------

registry_uri_MLOpsDBS = "databricks://az_mlopsdbs_prd:az_mlops_dbs"
mlflow.set_tracking_uri(registry_uri_MLOpsDBS)
client = MlflowClient(registry_uri=registry_uri_MLOpsDBS)

# List registered models
models = client.search_registered_models()

# Print the models
for model in models:
    print(f"Name: {model.name}")
    for version in model.latest_versions:
        print(f"  Version: {version.version}")
        print(f"  Stage: {version.current_stage}")
        print(f"  Source: {version.source}")
        print(f"  Run ID: {version.run_id}")
    print('*'*120)

# COMMAND ----------

# MAGIC %md
# MAGIC # DSDBSWorkspace

# COMMAND ----------

registry_uri_DBSWKS = "databricks://az_mlflow_dbswks:az_dbswks"
mlflow.set_tracking_uri(registry_uri_DBSWKS)
client = MlflowClient(registry_uri=registry_uri_DBSWKS)

# List registered models
models = client.search_registered_models()

# Print the models
for model in models:
    print(f"Name: {model.name}")
    for version in model.latest_versions:
        print(f"  Version: {version.version}")
        print(f"  Stage: {version.current_stage}")
        print(f"  Source: {version.source}")
        print(f"  Run ID: {version.run_id}")
    print('*'*120)
