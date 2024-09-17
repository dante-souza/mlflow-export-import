# Databricks notebook source
# MAGIC %pip install git+https:///github.com/mlflow/mlflow-export-import/#egg=mlflow-export-import --force-reinstall
# MAGIC %pip install numpy==1.26.4 --force-reinstall
# MAGIC %pip install rich
# MAGIC # %pip install mlflow-export-import tabulate
# MAGIC # dbutils.library.restartPython()

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from mlflow_export_import.experiment.export_experiment import export_experiment
from mlflow_export_import.experiment.import_experiment import import_experiment
import mlflow
import subprocess
from rich import print as pprint

# COMMAND ----------

# mlflow_tracking_uri = "databricks://az_dbswks_dev:az_dbswks"
mlflow_tracking_uri = "databricks://az_dbswks_dev:az_dbswks"
mlflow.set_tracking_uri(mlflow_tracking_uri)
mlflow.set_registry_uri(mlflow_tracking_uri)

# model_id = "4098205243317881"
# model_name = "modelo_cesta"
# model_name = "modelo_cancelamento_compras_online"
experiment_name = "transtion_collection_curto"
experiment_id = "3227642808760404"
output_dir = f"temp/{experiment_name}"
experiment_path = f"/Users/dante.souza@viavarejo.com.br/{experiment_name}"
experiment_owner = f"/Users/willy.hsu@viavarejo.com.br/{experiment_name}"
export_experiment(
    experiment_id_or_name = experiment_id,
    output_dir = experiment_owner
)

# COMMAND ----------

command = f"ls -lh temp/{experiment_name}/b5a481220ee34116819061ff12486117/artifacts/modelos_collection_ciclo_curto_2"
pprint(subprocess.run(command, shell=True, capture_output=True, text=True).stdout)

# COMMAND ----------

tracking_uri_state = 'databricks'
mlflow.set_tracking_uri(tracking_uri_state)
mlflow.set_registry_uri(tracking_uri_state)
import_experiment(
    experiment_name=experiment_path,
    input_dir=experiment_owner,
)

# COMMAND ----------


