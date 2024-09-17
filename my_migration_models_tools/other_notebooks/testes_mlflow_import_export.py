# Databricks notebook source
# MAGIC %pip install git+https:///github.com/mlflow/mlflow-export-import/#egg=mlflow-export-import --force-reinstall
# MAGIC # %pip install mlflow-export-import tabulate
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

from mlflow_export_import.common import mlflow_utils 
from mlflow_export_import.experiment.export_experiment import export_experiment
from mlflow_export_import.model.export_model import export_model
from mlflow_export_import.model.import_model import import_model
# from mlflow_export_import.experiment.export_experiment import export_experiment
import mlflow
from mlflow.tracking import MlflowClient

# COMMAND ----------

mlflow.__version__

# COMMAND ----------

experiment_id = "2513832432344512"
mlflow_tracking_uri = "databricks://az_mlflow:az_dev_mlops"
mlflow.set_tracking_uri(mlflow_tracking_uri)

# COMMAND ----------

experiment = mlflow.get_experiment(experiment_id)
output_dir = f"temp/{experiment.experiment_id}"
run_start_date = "2023-04-05"

# COMMAND ----------

export_experiment(
    experiment_id_or_name = experiment_id,
    output_dir = output_dir,
    run_start_time = None,
    export_permissions = False,
)

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -lh temp/2513832432344512/ed5e900dfd18429997a0f151f4b8bf60

# COMMAND ----------

model_name = "crm_aov"
output_dir = f"temp/{model_name}"
export_model(
    model_name = model_name,
    output_dir = output_dir
)

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -lh temp/crm_aov

# COMMAND ----------

CATALOG_NAME = "machine_learning_dev"
SCHEMA_NAME = "models"
MODEL_NAME = f"{CATALOG_NAME}.{SCHEMA_NAME}.{model_name}"
tracking_uri = 'databricks-uc'
tracking_uri_state = 'databricks'
uc_experiment_id = "1664714799102254"
mlflow.set_tracking_uri(tracking_uri_state)
# client = MlflowClient(tracking_uri=tracking_uri)
import_model(
    model_name,
    # experiment_name=f"/{model_name}",
    experiment_name=f"/Users/dante.souza@viavarejo.com.br/crm_aov",
    input_dir=output_dir,
    # client=client
)

# COMMAND ----------


