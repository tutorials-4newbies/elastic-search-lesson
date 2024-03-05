# Elasticsearch lesson

Documentation - https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

## Setup steps to complete before the lesson

1. Create the virtualenv using poetry:

   ```shell
    poetry install
   ```

2. Build and run the influxdb docker container:
   ```shell
   docker compose up
   ```
3. Check that elasticsearch is running:
    * http://127.0.0.1:9200/
    * Try to log in, good luck finding the credentials!