# Databricks notebook source
# MAGIC %md
# MAGIC # Install

# COMMAND ----------

# MAGIC %pip install mlflow==2.5.0 -q
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC # Imports

# COMMAND ----------

import mlflow
from mlflow.tracking import MlflowClient

# COMMAND ----------

# MAGIC %md # Run SP scope creation

# COMMAND ----------

# %run ./sp_create_scope

# COMMAND ----------

# MAGIC %md
# MAGIC # Setting up

# COMMAND ----------

# registry_uri_GCP_DEV = "databricks://gcp_mlflow_dev:mlflow_dev_gcp"
# mlflow.set_tracking_uri(registry_uri_GCP_DEV)
# mlflow.set_registry_uri(registry_uri_GCP_DEV)
# client = MlflowClient()

# COMMAND ----------

# MAGIC %md # Get models names in gcp_dev

# COMMAND ----------

# registered_models = client.search_registered_models()
# model_names = [model.name for model in registered_models]

# COMMAND ----------

mlflow.set_tracking_uri("databricks")
mlflow.set_registry_uri("databricks")
# client = MlflowClient()
client = MlflowClient(tracking_uri="databricks", registry_uri="databricks")

# COMMAND ----------

models = {
    'classificador_mktp_dsdepartamento': '1',
 'crm_churn': '1',
 'crm_churn_cb': '1',
 'crm_churn_ex': '1',
 'crm_churn_pf': '1',
 'crm_leadscoring': '1',
 'crm_melhor_horario_hartb': '1',
 'crm_pam': '1',
 'fraud_cpf_model': '1',
 'fraud_detection': '1',
 'LGBMFraudNoBankRetrain2_3': '1',
 'ltv_receita': '10',
 'modelo_cancelamento_compras_online': '1',
 'modelo_cesta_departamento': '1',
 'modelo_cesta_familia': '1',
 'modelo_cesta_produto': '1',
 'modelo_cesta_setor': '1',
 'modelo_credito_pre_aprovado_com_historico_cdc': '1',
 'modelo_credito_pre_aprovado_sem_historico_cdc': '1',
 'modelo_propensao_cdc_marketing': '1',
 'modelo_similaridade_produto': '1',
 'modelo_transbordo_canais_especiais': '1',
 'modelos_collection_ciclo_curto_1': '1',
 'modelos_collection_ciclo_curto_2': '1',
 'modelos_collection_ciclo_curto_3': '1',
 'modelos_collection_ciclo_curto_4': '1'}

# COMMAND ----------

data = {}
for model in models:
    print(f"run for {model}:")
    try:
        result = client.create_registered_model(model)
    except Exception as e:
        data[model] = e
    else:
        data[model] = result
    print(f"model {model} done")

# COMMAND ----------

data

# COMMAND ----------

# %run ./sp_delete_scope
