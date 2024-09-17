# Databricks notebook source
# MAGIC %pip install rich -q

# COMMAND ----------

import requests
import json
from rich import print as pprint

# COMMAND ----------

url = "https://3717318023485255.5.gcp.databricks.com/api/2.0/secrets/scopes/list"

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
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("GET", 
                            url, 
                            headers=headers, 
                            data=payload
                            )


# COMMAND ----------

print(response.status_code)

# COMMAND ----------

pprint(json.loads(response.text))

# COMMAND ----------


