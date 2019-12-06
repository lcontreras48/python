#!/usr/bin/env python3

"""

    Script para

    by Dorance <dorancemc@gmail.com>

"""

import json
import requests

# functions
def main(command_line=None):
  term = {
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

  print(search("https://hurley-elasticsearch-us-west-2.api.hbo.com:443/dotcom-v4-cms-logs/_search",term))

def search(uri, term):
  """Simple Elasticsearch Query"""
  headers = { 'Accept': 'application/json' }
  query = json.dumps(term)
  response = requests.get(uri,headers=headers,data=query)
  results = json.loads(response.text)
  return results

# main
if __name__ == '__main__':
  main()
