# Databricks notebook source
# MAGIC %md
# MAGIC # Imports

# COMMAND ----------

import requests
import json

# COMMAND ----------

# MAGIC %md
# MAGIC # Get token from SP

# COMMAND ----------

url_prd = "https://2051187530458080.0.gcp.databricks.com/oidc/v1/token"
url_dev = "https://3717318023485255.5.gcp.databricks.com/oidc/v1/token"
payload = 'grant_type=client_credentials&scope=all-apis&client_id=b186113a-24ae-42db-a73b-9a32b4480d80&client_secret=dosecfa23f7ed3b2237aaf9a897a0d469fb6'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response_prd = requests.request("POST", url_prd, headers=headers, data=payload)
a_tkn_sp_prd = response_prd.json()['access_token']

response_dev = requests.request("POST", url_dev, headers=headers, data=payload)
a_tkn_sp_dev = response_dev.json()['access_token']

# COMMAND ----------

# MAGIC %md # Criar scope apontando p dev

# COMMAND ----------

url = "https://2051187530458080.0.gcp.databricks.com/api/2.0/secrets/scopes/create"

payload = json.dumps({
  "scope": "gcp_mlflow_dev"
})
headers = {
  'Authorization': f'Bearer {a_tkn_sp_prd}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)


# COMMAND ----------

# MAGIC %md
# MAGIC # Adicionar o host de dev no scope

# COMMAND ----------

url = "https://2051187530458080.0.gcp.databricks.com/api/2.0/secrets/put"

payload = json.dumps({
  "scope": "gcp_mlflow_dev",
  "key": "mlflow_dev_gcp-host",
  "string_value": "https://3717318023485255.5.gcp.databricks.com/"
})


response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)


# COMMAND ----------

# MAGIC %md
# MAGIC # Adicionar acess token do SP conseguir acessar o ambiente de dev

# COMMAND ----------

url = "https://2051187530458080.0.gcp.databricks.com/api/2.0/secrets/put"

payload = json.dumps({
  "scope": "gcp_mlflow_dev",
  "key": "mlflow_dev_gcp-token",
  "string_value": f"{a_tkn_sp_dev}"
})


response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)


# COMMAND ----------

# MAGIC %md
# MAGIC # Adicionar workspace-id no scope

# COMMAND ----------

url = "https://2051187530458080.0.gcp.databricks.com/api/2.0/secrets/put"

payload = json.dumps({
  "scope": "gcp_mlflow_dev",
  "key": "mlflow_dev_gcp-workspace-id",
  "string_value": "3717318023485255"
})


response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)

