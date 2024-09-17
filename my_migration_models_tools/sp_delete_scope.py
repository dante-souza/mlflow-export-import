# Databricks notebook source
import requests
import json

# COMMAND ----------

url_prd = "https://2051187530458080.0.gcp.databricks.com/oidc/v1/token"

payload = 'grant_type=client_credentials&scope=all-apis&client_id=b186113a-24ae-42db-a73b-9a32b4480d80&client_secret=dosecfa23f7ed3b2237aaf9a897a0d469fb6'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response_prd = requests.request("POST", url_prd, headers=headers, data=payload)
a_tkn_sp_prd = response_prd.json()['access_token']


# COMMAND ----------



url = "https://2051187530458080.0.gcp.databricks.com/api/2.0/secrets/scopes/delete"

payload = json.dumps({
  "scope": "gcp_mlflow_dev"
})
headers = {
  'Authorization': f'Bearer {a_tkn_sp_prd}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

delete_status = response.status_code

print(delete_status)
dbutils.notebook.exit(f"Deleted scope gcp_mlflow_dev status: {delete_status}")

