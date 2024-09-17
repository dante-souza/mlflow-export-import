# Databricks notebook source
# MAGIC %pip install rich -q

# COMMAND ----------

import requests
import json
from rich import print as pprint

# COMMAND ----------

# url = "https://adb-1873160625132853.13.azuredatabricks.net/api/2.0/mlflow/registered-models/list"
url = "https://adb-1873160625132853.13.azuredatabricks.net/api/2.0/mlflow/experiments/list"

payload = json.dumps({
  "url": "https://github.com/viavarejo-internal/workshop_casper_structure_0",
  "provider": "gitHub",
  "path": "/Repos/teste_willy/workshop_casper_structure_0",
  "sparse_checkout": {
    "patterns": [
      "parent-folder/child-folder"
    ]
  }
})
headers = {
  'Authorization': 'Bearer <az_token>',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

# COMMAND ----------

"transtion_collection_curto" in json.dumps(response.text)

# COMMAND ----------

if response.status_code == 200:
    pprint(json.loads(response.text))
else:
    print(response.status_code)
