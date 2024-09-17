# Databricks notebook source
# MAGIC %pip install mlflow -q
# MAGIC %pip 
# MAGIC %pip install --upgrade "mlflow-skinny[databricks]>=2.5.0" -q
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import mlflow
from mlflow.tracking.client import MlflowClient

# COMMAND ----------

# registry_uri = "databricks://az_mlflow:az_dev_mlops"
registry_uri = "databricks://az_mlflow_prd:az_prd_mlops"
registry_uri_local = "databricks"
mlflow.set_tracking_uri(registry_uri)
client = MlflowClient(registry_uri=registry_uri)

# COMMAND ----------

# client = MlflowClient()

# List registered models
# models = client.search_registered_models()

# # Print the models
# for model in models:
#     print(f"Name: {model.name}")
#     for version in model.latest_versions:
#         print(f"  Version: {version.version}")
#         print(f"  Stage: {version.current_stage}")
#         print(f"  Source: {version.source}")
#         print(f"  Run ID: {version.run_id}")
#     print('*'*120)

# COMMAND ----------

# logged_model = 'runs:/45adae3db29b4992a6216acd4ed2d4ba/model'
# model_python = mlflow.sklearn.load_model(logged_model)

# COMMAND ----------

MODEL_NAME = "crm_pam"
MODEL_VERSION = 1
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"
# mlflow.pyfunc.get_model_dependencies(model_uri)
model = mlflow.spark.load_model(model_uri)

# COMMAND ----------

# def get_latest_model_version(model_name):
#   client = MlflowClient()
#   model_version_infos = client.search_model_versions("name = '%s'" % model_name)
#   return max([int(model_version_info.version) for model_version_info in model_version_infos])

# COMMAND ----------

# get_latest_model_version(MODEL_NAME)

# COMMAND ----------

# import mlflow
# import mlflow.pyfunc
 
# class SampleModel(mlflow.pyfunc.PythonModel):
#   def predict(self, ctx, input_df):
#       return 7
 
# artifact_path = MODEL_NAME
# # Log a model to MLflow Tracking
# from mlflow.tracking.artifact_utils import get_artifact_uri
 
# with mlflow.start_run() as new_run:
#   mlflow.pyfunc.log_model(  
#       python_model=SampleModel(),
#       artifact_path=artifact_path,
#   )
#   run1_id = new_run.info.run_id
#   source = get_artifact_uri(run_id=run1_id, artifact_path=artifact_path)

#   # Instantiate an MlflowClient pointing to the local tracking server and a remote registry server
# from mlflow.tracking.client import MlflowClient
# client = MlflowClient(tracking_uri=None, registry_uri=uri)
 
# model = client.create_registered_model(MODEL_NAME)
# client.create_model_version(name=MODEL_NAME, source=source, run_id=run1_id)


# COMMAND ----------

# mlflow.set_registry_uri('databricks-uc')
# CATALOG_NAME = "machine_learning_dev"
# SCHEMA_NAME = "models"
# MODEL_URI_UC = f"{CATALOG_NAME}.{SCHEMA_NAME}.{MODEL_NAME}"

# mlflow.spark.log_model(model, 
#                        artifact_path=MODEL_NAME,
#                        registered_model_name=MODEL_NAME)

# COMMAND ----------


