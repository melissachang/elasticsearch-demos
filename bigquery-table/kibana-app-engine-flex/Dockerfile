# Test locally:
# docker build -t kibana-app-engine-flex .
# --init is so Ctrl-C works with "docker run"
# docker run --init -p 8080:8000 kibana-app-engine-flex

# Do you have X-Pack? If so, you can use any of the official images at
# docker.elastic.co/kibana.
# If not using X-Pack:
# - If ElasticSearch 6.*, use official image at docker.elastic.co/kibana.
#   Use one with "-oss"; those don't have X-Pack.
# - If ElasticSearch 5.*, use deprecated images at docker.elastic.co/kibana
#   The official images only have oss versions for 6.*.
# See https://github.com/elastic/kibana-docker/issues/27
FROM kibana:5.0.2

CMD ["kibana", "-e", "http://10.142.0.2:9200", "-p", "8080"]
