# Databricks notebook source
# MAGIC %pip install rich -q
# MAGIC %pip install --upgrade "mlflow-skinny[databricks]>=2.5.0" -q
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import mlflow
from mlflow.tracking.client import MlflowClient
from rich import print as pprint

# COMMAND ----------

# registry_uri_MLFowDBS = "databricks://az_mlflowdbs_prd:az_mlflow_dbs"
az_dev_tracking_uri = "databricks://az_dbswks_dev:az_dbswks"
mlflow.set_tracking_uri(az_dev_tracking_uri)
mlflow.set_registry_uri(az_dev_tracking_uri)
# client = MlflowClient(registry_uri=az_dev_tracking_uri, tracking_uri=az_dev_tracking_uri)

# COMMAND ----------

# Search for all experiments
experiments = mlflow.search_experiments()
experiments_dict = {}
# Print the experiment details
for experiment in experiments:
    experiments_dict[experiment.name] = f"ID: {experiment.experiment_id}, Name: {experiment.name}, Artifact Location: {experiment.artifact_location}"
    # print(f"ID: {experiment.experiment_id}, Name: {experiment.name}, Artifact Location: {experiment.artifact_location}")


# COMMAND ----------

pprint(sorted([exp_name.split('/')[-1] for exp_name in experiments_dict.keys()])[::-10])

# COMMAND ----------


