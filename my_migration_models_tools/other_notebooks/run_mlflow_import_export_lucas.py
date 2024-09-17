# Databricks notebook source
# MAGIC %md
# MAGIC # Installation

# COMMAND ----------

# instalacao precisa ser do repo do git. a wheel esta desatualizada. mas nao se descarta o uso dela. 
%pip install git+https:///github.com/mlflow/mlflow-export-import/#egg=mlflow-export-import --force-reinstall
# forca a instalacao da versao 1.26.4 do numpy. 
# a versao 2.0.0 do mlflow-export-import esta com problemas com o numpy
%pip install numpy==1.26.4 --force-reinstall
# lib para ver prints mais bonitos no console
%pip install rich
# %pip install mlflow-export-import tabulate
# opcional. o restartPython da uma atualizacao das libs recem instaladas da memoria do driver do cluster
# dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC # Imports

# COMMAND ----------

from mlflow_export_import.model.export_model import export_model
from mlflow_export_import.model.import_model import import_model
import mlflow
import subprocess
from rich import print as pprint

# COMMAND ----------

# MAGIC %md
# MAGIC # Export

# COMMAND ----------

# para exportar o modelo, seta o tracking_uri para o databricks da azure. aqui no caso o mlflow do dbsworkspace-dev.
mlflow_tracking_uri = "databricks://az_mlflow:az_dev_mlops"
mlflow.set_tracking_uri(mlflow_tracking_uri)
mlflow.set_registry_uri(mlflow_tracking_uri)


model_name = "ltv_receita"
# model_name = "modelo_cancelamento_compras_online"
# preciso de um caminho temporario valido para a exportacao
output_dir = f"temp/{model_name}"
export_model(
    model_name = model_name,
    output_dir = output_dir
)

# COMMAND ----------

# MAGIC %md
# MAGIC # View artifacts in local folder

# COMMAND ----------

# so para ver se ta td na pasta
command = f"ls -lh temp/{model_name}"
pprint(subprocess.run(command, shell=True, capture_output=True, text=True).stdout)

# COMMAND ----------

# MAGIC %md
# MAGIC # Import

# COMMAND ----------

# troca o mlflow para o local
tracking_uri_state = 'databricks'
mlflow.set_tracking_uri(tracking_uri_state)
mlflow.set_registry_uri(tracking_uri_state)
# importa o modelo a partir da pasta temporaria usada para o exporet do modelo anteriormente setada
import_model(
    model_name,
    experiment_name=f"/Users/dante.souza@viavarejo.com.br/{model_name}",
    input_dir=output_dir,
)

# COMMAND ----------

# MAGIC %md
# MAGIC # Plus

# COMMAND ----------

# MAGIC %md
# MAGIC ## MLFlow Installation

# COMMAND ----------

# MAGIC %pip install mlflow==2.5.0 -q
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Load spark model from mlflow de dev da azure

# COMMAND ----------

import mlflow
mlflow.set_tracking_uri("databricks://az_mlflow:az_dev_mlops")
mlflow.spark.load_model("models:/crm_leadscoring_ctd/2"
                        )

# COMMAND ----------

# MAGIC %md
# MAGIC ## Load python model from local mlflow

# COMMAND ----------

import mlflow
mlflow.set_tracking_uri('databricks')
mlflow.pyfunc.load_model("models:/ltv_receita/10"
                        )
