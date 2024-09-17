# Databricks notebook source
# MAGIC %pip install mlflow -q
# MAGIC %pip install --upgrade "mlflow-skinny[databricks]>=2.5.0" -q
# MAGIC %pip install numpy==1.26.4 --force-reinstall
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import mlflow
from mlflow.tracking.client import MlflowClient

# COMMAND ----------

registry_uri_local = "databricks"
mlflow.set_tracking_uri(registry_uri_local)
mlflow.set_registry_uri(registry_uri_local)
client = MlflowClient(registry_uri=registry_uri_local)

# COMMAND ----------

# # DBS_DEV
# registry_uri = "databricks://az_mlflow:az_dev_mlops"
# # MLOPSDBS
# # registry_uri = "databricks://az_mlopsdbs_prd:az_mlops_dbss"
# # MLFLOWDBS
# # registry_uri = "databricks://az_mlflowdbs_prd:az_mlflow_dbs"
# mlflow.set_tracking_uri(registry_uri)
# mlflow.set_registry_uri(registry_uri)
# client = MlflowClient(registry_uri=registry_uri)

# COMMAND ----------

# logged_model = 'runs:/45adae3db29b4992a6216acd4ed2d4ba/model'
# model_python = mlflow.sklearn.load_model(logged_model)

# COMMAND ----------

MODEL_NAME = "ltv_receita"
MODEL_VERSION = 10
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"
# mlflow.pyfunc.get_model_dependencies(model_uri)
model = mlflow.spark.load_model(model_uri)

# COMMAND ----------

# MODEL_NAME = "crm_aov"
# MODEL_VERSION = 2
# model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"
# # mlflow.pyfunc.get_model_dependencies(model_uri)
# model = mlflow.spark.load_model(model_uri)

# COMMAND ----------


