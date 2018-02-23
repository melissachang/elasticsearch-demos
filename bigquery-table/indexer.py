"""Loads BigQuery table into Elasticsearch."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import pandas as pd
import time


def main():
  print('Hello world')

  es = Elasticsearch(['http://192.168.9.2:9200'],timeout=600)

  # This will fail fast if Elasticsearch isn't up. Do this before
  # BigQuery -> pandas, because that can take a long time.
  es.cluster.health()

  start_time = time.time()
  concept = pd.read_gbq(
    "SELECT * FROM `google.com:api-project-360728701457.omop.concept`",
    project_id='google.com:api-project-360728701457', dialect='standard')
  elapsed_time = time.time() - start_time
  elapsed_time_str = time.strftime("%Hh:%Mm:%Ss", time.gmtime(elapsed_time))

  print('BigQuery -> pandas took %s' % elapsed_time_str)
  print('concept has %d rows' % len(concept))

  try:
    es.indices.delete(index='concept')
  except Exception:
    pass
  es.indices.create(index='concept',body={})
  documents = concept.to_dict(orient='records')
  start_time = time.time()
  bulk(es, documents, index='concept', doc_type='doc_type', raise_on_error=True)
  elapsed_time = time.time() - start_time
  elapsed_time_str = time.strftime("%Hh:%Mm:%Ss", time.gmtime(elapsed_time))

  print('pandas -> ElasticSearch index took %s' % elapsed_time_str)


if __name__ == '__main__':
  main()
