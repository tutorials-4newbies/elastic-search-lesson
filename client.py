from pprint import pprint
from elasticsearch import Elasticsearch, BadRequestError


class ElasticClient:
    def __init__(self):
        self.elastic_client = Elasticsearch("http://localhost:9200")
        client_info = self.elastic_client.info()
        pprint(client_info.body)

    def create_index(self, index_name: str, mappings: dict):
        try:
            self.elastic_client.indices.create(index=index_name, mappings=mappings)
        except BadRequestError:
            print(f"'{index_name}' already exists, skipping creation")

    def insert_document(self, index_name: str, document: dict):
        return self.elastic_client.index(index=index_name, body=document)

    def show_mappings(self, index_name: str):
        return self.elastic_client.indices.get_mapping(index=index_name)

    def retrieve_document(self, index_name: str, document_id: str):
        return self.elastic_client.get(index=index_name, id=document_id)
