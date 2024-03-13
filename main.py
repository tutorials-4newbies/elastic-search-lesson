from pprint import pprint

from client import ElasticClient

elastic_client = ElasticClient()

my_name = "first_index"


def setup():
    my_index_mappings = {
        "dynamic": "strict",
        "properties": {
            "name": {"type": "text"},
            "main_text": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256,
                    }
                },
            },
        }
    }
    elastic_client.create_index(index_name=my_name, mappings=my_index_mappings)


def add_docs():
    my_doc = dict(
        name="first name",
        main_text="some random text"
    )
    add_doc_res = elastic_client.insert_document(index_name=my_name, document=my_doc)
    print("Document was added")
    pprint(add_doc_res)


def get_document_with_id():
    my_doc_id = '5183GI4Bd2ZiWoz_4w5S'
    res_doc = elastic_client.retrieve_document(index_name=my_name, document_id=my_doc_id)
    pprint(res_doc)


def search():
    pass


if __name__ == "__main__":
    setup()
    add_docs()
