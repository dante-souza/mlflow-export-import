# Databricks notebook source
# MAGIC %pip install /Volumes/machine_learning_dev/models/files/mlflow_export_import-1.2.0-py3-none-any.whl
# MAGIC %pip install numpy==1.26.4 --force-reinstall

# COMMAND ----------

from mlflow_export_import.copy.copy_run import copy
import mlflow

# COMMAND ----------

src_mlflow_uri = "databricks://az_dbswks_dev:az_dbswks"
dst_mlflow_uri = "databricks"

# COMMAND ----------

mlflow.set_tracking_uri(dst_mlflow_uri)
mlflow.set_registry_uri(dst_mlflow_uri)

# COMMAND ----------

src_run_id = "b5a481220ee34116819061ff12486117"
dst_experiment_name = "transtion_collection_curto"

# COMMAND ----------

copy(src_run_id, 
        dst_experiment_name, 
        src_mlflow_uri, 
        dst_mlflow_uri)

# COMMAND ----------


