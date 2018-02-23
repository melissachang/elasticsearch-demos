## How to run a Kibana/Elasticsearch demo on Google Cloud Platform
Load a BigQuery table into Elasticsearch running in a Google Compute Engine VM. Run Kibana on App Engine Flex that talks to Elasticsearch.
- You must have read permission the BigQuery table.
- Create index in Elasticsearch running on Google Compute Engine. We can't run on App Engine Flex because those instances are [restarted every week](https://cloud.google.com/appengine/docs/the-appengine-environments#comparing_the_flexible_environment_to_compute_engine) and we would lose our index.
  - Create a Debian instance.
  - ssh to the instance and run elasticsearch. The `&` keeps docker running after the SSH connection closes.
    `docker run -d -p 9200:9200 elasticsearch:5.0.2` &
  - Index table.
    - Copy `Dockerfile`, `requirements.txt`, `indexer.py` to VM.
    - In `indexer.py`, change Elasticsearch address and BigQuery table.
    - `docker build -t indexer . && docker run indexer &`
    - [If docker crashes, you need to give your VM more CPU and/or memory.](https://github.com/docker/for-mac/issues/1941#issuecomment-367876842)
    - TODO(melissachang): Write index to persistent disk so it persists across reboots.
- Run Kibana.
  - In `kibana-app-engine-flex/Dockerfile`, change IP to the internal IP of the Elasticsearch VM.
  - From `kibana-app-engine-flex` directory:
     `gcloud app deploy`
