# Databricks notebook source
# MAGIC %pip install git+https:///github.com/mlflow/mlflow-export-import/#egg=mlflow-export-import --force-reinstall
# MAGIC %pip install numpy==1.26.4 --force-reinstall
# MAGIC %pip install rich
# MAGIC # %pip install mlflow-export-import tabulate
# MAGIC # dbutils.library.restartPython()

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from mlflow_export_import.model.export_model import export_model
from mlflow_export_import.model.import_model import import_model
import mlflow
import subprocess
from rich import print as pprint

# COMMAND ----------

mlflow_tracking_uri = "databricks://az_mlflow:az_dev_mlops"
mlflow.set_tracking_uri(mlflow_tracking_uri)
mlflow.set_registry_uri(mlflow_tracking_uri)

model_name = "ltv_receita"
# model_name = "modelo_cancelamento_compras_online"
output_dir = f"temp/{model_name}"
export_model(
    model_name = model_name,
    output_dir = output_dir
)

# COMMAND ----------

command = f"ls -lh temp/{model_name}"
pprint(subprocess.run(command, shell=True, capture_output=True, text=True).stdout)

# COMMAND ----------

tracking_uri_state = 'databricks'
mlflow.set_tracking_uri(tracking_uri_state)
mlflow.set_registry_uri(tracking_uri_state)
import_model(
    model_name,
    experiment_name=f"/Users/dante.souza@viavarejo.com.br/{model_name}",
    input_dir=output_dir,
)

# COMMAND ----------


