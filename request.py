import json
import requests

payload = {
  "version": 'true',
  "size": 1000,
  "sort": [
    {
      "@timestamp": {
        "order": "desc",
        "unmapped_type": "boolean"
      }
    }
  ],
  "_source": {
    "excludes": []
  },
  "aggs": {
    "2": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "12h",
        "time_zone": "America/New_York",
        "min_doc_count": 1
      }
    }
  },
  "stored_fields": [
    "*"
  ],
  "script_fields": {},
  "docvalue_fields": [
    "@timestamp",
    "data.indexActions.document.associatedEntities.person.updated",
    "data.indexActions.document.associatedEntities.series.updated",
    "data.indexActions.document.documentary.premiereDateTime",
    "data.indexActions.document.episode.airDateTime",
    "data.indexActions.document.primaryEntity.contributor.updated",
    "data.indexActions.document.standAlone.premiereDateTime",
    "data.indexActions.document.updated",
    "data.page.associatedEntities.movie.movie.premiereDateTime",
    "data.page.associatedEntities.movie.updated",
    "data.page.associatedEntities.person.updated",
    "data.page.associatedEntities.series.updated",
    "data.page.associatedEntities.standAlone.updated",
    "data.page.primaryEntity.article.updated",
    "data.page.primaryEntity.contributor.updated",
    "data.page.primaryEntity.documentary.documentary.premiereDateTime",
    "data.page.primaryEntity.documentary.updated",
    "data.page.primaryEntity.episode.episode.airDateTime",
    "data.page.primaryEntity.episode.updated",
    "data.page.primaryEntity.movie.updated",
    "data.page.primaryEntity.season.updated",
    "data.page.primaryEntity.series.updated",
    "data.page.primaryEntity.standAlone.standAlone.premiereDateTime",
    "data.page.primaryEntity.standAlone.updated",
    "data.page.updated",
    "time"
  ],
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "env": {
              "query": "dotcom-v4-prod"
            }
          }
        },
        {
          "match_phrase": {
            "kubernetes.pod_name": {
              "query": "dotcom-search-worker"
            }
          }
        },
        {
          "match_phrase": {
            "level": {
              "query": "error"
            }
          }
        },
        {
          "bool": {
            "minimum_should_match": 1,
            "should": [
              {
                "match_phrase": {
                  "data.stack": "IndexManagerError"
                }
              }
            ]
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": 1572710277791,
              "lte": 1575305877791,
              "format": "epoch_millis"
            }
          }
        }
      ],
      "filter": [
        {
          "match_all": {}
        }
      ],
      "should": [],
      "must_not": [
        {
          "bool": {
            "minimum_should_match": 1,
            "should": [
              {
                "match_phrase": {
                  "data.stack": "Request Timeout after"
                }
              }
            ]
          }
        },
        {
          "bool": {
            "minimum_should_match": 1,
            "should": [
              {
                "match_phrase": {
                  "data.stack": "DocumentManagerError"
                }
              }
            ]
          }
        },
        {
          "bool": {
            "minimum_should_match": 1,
            "should": [
              {
                "match_phrase": {
                  "data.stack": "AemApiStatusError"
                }
              }
            ]
          }
        }
      ]
    }
  },
  "highlight": {
    "pre_tags": [
      "@kibana-highlighted-field@"
    ],
    "post_tags": [
      "@/kibana-highlighted-field@"
    ],
    "fields": {
      "*": {}
    },
    "fragment_size": 2147483647
  }
}
r = requests.get('https://hurley-elasticsearch-us-west-2.api.hbo.com:443/_search',json=payload)
