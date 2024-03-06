from pprint import pprint
from typing import List, Optional

from elasticsearch import Elasticsearch


class ElasticClient:
    def __init__(self):
        self.elastic_client = Elasticsearch("http://localhost:9200")
        client_info = self.elastic_client.info()
        print('Connected to Elasticsearch!')
        # pprint(client_info.body)

    def create_index(self, index_name: str, mappings: Optional[dict] = None):
        self.elastic_client.indices.delete(index=index_name, ignore_unavailable=True)
        if mappings:
            self.elastic_client.indices.create(index=index_name, mappings=mappings)
        else:
            self.elastic_client.indices.create(index=index_name)

    def insert_document(self, index_name: str, document: dict):
        return self.elastic_client.index(index=index_name, body=document)

    def insert_documents(self, index_name: str, documents: List[dict]):
        operations = []
        for document in documents:
            operations.append({'index': {'_index': index_name}})
            operations.append(document)
        return self.elastic_client.bulk(operations=operations)

    def retrieve_document(self, index_name: str, document_id: str):
        return self.elastic_client.get(index=index_name, id=document_id)

    def search(self, index_name: str, query_args):
        return self.elastic_client.search(index=index_name, **query_args)
