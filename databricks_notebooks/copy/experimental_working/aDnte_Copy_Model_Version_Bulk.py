# Databricks notebook source
# MAGIC %md ## Copy Model Version
# MAGIC
# MAGIC #### Overview
# MAGIC
# MAGIC * Copies a model version and its run (deep copy) to a new model version.
# MAGIC * The new model version can be either in the same workspace or in another.
# MAGIC * Supports both standard Workspace registry and the new Unity Catalog (UC) model registry.
# MAGIC * Databricks registry URIs should be Databricks secrets tuples per [Specify a remote registry](https://docs.databricks.com/en/machine-learning/manage-model-lifecycle/multiple-workspaces.html).
# MAGIC   * Example: `registry_uri = f'databricks://<scope>:<prefix>'`
# MAGIC
# MAGIC
# MAGIC #### Widgets
# MAGIC
# MAGIC * `1. Source Model` - Source model name.
# MAGIC * `2. Source Version` - Source model version.
# MAGIC * `3. Destination Model` - Destination model name.
# MAGIC * `4. Destination experiment name` - Destination experiment name. 
# MAGIC   * If specified, copies source version's run to a new run which the new model version points to.
# MAGIC   * If not specified, the new run uses the source version's run.
# MAGIC * `5. Source Run Workspace` - Workspace for the run of the source model version. 
# MAGIC   * If copying from current workspace, then leave blank or set to `databricks`.
# MAGIC   * If copying from another workspace, then specify secrets scope and prefix per [Set up the API token for a remote registry](https://docs.databricks.com/en/machine-learning/manage-model-lifecycle/multiple-workspaces.html#set-up-the-api-token-for-a-remote-registry). 
# MAGIC     * Example: `databricks://MY-SCOPE:MY-PREFIX`.
# MAGIC * `6. Copy lineage tags` - Add source lineage info to destination version as tags starting with 'mlflow_exim'.
# MAGIC * `7. Verbose`
# MAGIC * `8. Return result` for automated testing.

# COMMAND ----------

# MAGIC %md ### Diagrams
# MAGIC
# MAGIC In the two diagram below, the left shallow copy is **_bad_**, and the right deep copy is **_good_**.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Unity Catalog Model Registry
# MAGIC
# MAGIC  <img src="https://github.com/mlflow/mlflow-export-import/blob/issue-138-copy-model-version/diagrams/Copy_Model_Version_UC.png?raw=true"  width="700" />

# COMMAND ----------

# MAGIC  %md ### Workspace Model Registry
# MAGIC
# MAGIC  <img src="https://github.com/mlflow/mlflow-export-import/blob/issue-138-copy-model-version/diagrams/Copy_Model_Version_NonUC.png?raw=true"  width="700" />
# MAGIC

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ./Common

# COMMAND ----------

# MAGIC %run ./aDnte_create_scope

# COMMAND ----------

# MAGIC %pip install numpy==1.26.4 --force-reinstall

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import mlflow 
from mlflow_export_import.common.dump_utils import obj_to_dict, dict_to_json, dump_obj_as_json

def assert_widget(value, name):
    if len(value.rstrip())==0: 
        raise Exception(f"ERROR: '{name}' widget is required")

from mlflow.utils import databricks_utils
mlflow_client = mlflow.MlflowClient()

_host_name = databricks_utils.get_browser_hostname()
print("host_name:", _host_name)

def display_registered_model_version_uri(model_name, version):
    if _host_name:
        if "." in model_name: # is unity catalog model
            model_name = model_name.replace(".","/")
            uri = f"https://{_host_name}/explore/data/models/{model_name}/version/{version}"
        else:
            uri = f"https://{_host_name}/#mlflow/models/{model_name}/versions/{version}"
        displayHTML("""<b>Registered Model Version URI:</b> <a href="{}">{}</a>""".format(uri,uri))

def display_run_uri(run_id):
    if _host_name:
        run = mlflow_client.get_run(run_id)
        uri = f"https://{_host_name}/#mlflow/experiments/{run.info.experiment_id}/runs/{run_id}"
        displayHTML("""<b>Run URI:</b> <a href="{}">{}</a>""".format(uri,uri))

def copy_model_version(
        src_model_name,
        src_model_version,
        dst_model_name,
        dst_experiment_name, 
        src_run_workspace = "databricks",
        copy_lineage_tags = False,
        verbose = False 
    ):
    from mlflow_export_import.common.model_utils import is_unity_catalog_model 
    from mlflow_export_import.copy.copy_model_version import copy
      
    def mk_registry_uri(model_name):
        return "databricks-uc" if is_unity_catalog_model(model_name) else "databricks"
    
    if src_run_workspace in [ "databricks", "databricks-uc"]:
        src_registry_uri = mk_registry_uri(src_model_name)
    elif is_unity_catalog_model(src_model_name):
        src_registry_uri = "databricks-uc"
    else:
        src_registry_uri = src_run_workspace
        
    dst_registry_uri = mk_registry_uri(dst_model_name)

    return copy(
        src_model_name,
        src_model_version,
        dst_model_name,
        dst_experiment_name, 
        src_tracking_uri = src_run_workspace,
        dst_tracking_uri = "databricks",
        src_registry_uri = src_registry_uri, 
        dst_registry_uri = dst_registry_uri,
        copy_lineage_tags = copy_lineage_tags,
        verbose = verbose 
    )

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


registry_uri_GCP_DEV = "databricks://gcp_mlflow_dev:mlflow_dev_gcp"

src_run_workspace = registry_uri_GCP_DEV

copy_lineage_tags = False
verbose = True
return_result = True

# COMMAND ----------

# MAGIC %md #### Copy Model Version

# COMMAND ----------

status = {}
for model_name, model_version in models.items():
    print(f"model {model_name} starting")
    src_model_name = model_name
    src_model_version = model_version

    dst_model_name = src_model_name
    # dst_model_name = "modelos_collection_ciclo_curto_4"
    dst_experiment_name = f"/dbfs/Volumes/machine_learning_prd/models/files/models/artifacts/{dst_model_name}"
    # dst_experiment_name = f"/Users/dante.souza@viavarejo.com.br/{src_model_name}"
    try:
        src_model_version, dst_model_version = copy_model_version(
            src_model_name,
            src_model_version,
            dst_model_name,
            dst_experiment_name,
            src_run_workspace = src_run_workspace,
            copy_lineage_tags = copy_lineage_tags,
            verbose = verbose
        )
    except Exception as e:
        status[model_name] = e
    else:
        status[model_name] = f"OK - {dst_model_version}"
    finally:
        print(f"model {model_name} ended")

status

# COMMAND ----------



# COMMAND ----------

# MAGIC %environment
# MAGIC "client": "1"
# MAGIC "base_environment": ""
