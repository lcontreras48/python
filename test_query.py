import requests

headers = {
    'Content-Type': 'application/json',
}

data = """
{
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "level": "error"
            }
          },
          {
            "match": {
              "env": "dotcom-v4-prod"
            }
          },
          {
            "match": {
              "kubernetes.pod_name": "dotcom-search-worker"
            }
          },
          {
            "range": {
              "@timestamp": {
                "gte": "16-11-2019",
                "lte": "23-11-2019",
                "format": "dd-MM-yyyy"
              }
            }
          },
          {
          "match": {
            "data.stack": "DocumentManagerError"
            }
          }
        ]
      }
    }
  }
"""

response = requests.post('https://hurley-elasticsearch-us-west-2.api.hbo.com:443/_search', headers=headers, data=data)