from pprint import pprint

from client import ElasticClient

elastic_client = ElasticClient()

my_name = "first_index"
# res = elastic_client.show_mappings(index_name=my_name)
# pprint(res)
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

my_doc = dict(
    name="first name",
    main_text="some random text"
)
# res = elastic_client.insert_document(index_name=my_name, document=my_doc)
# pprint(res)

my_doc_id = '5183GI4Bd2ZiWoz_4w5S'
res_doc = elastic_client.retrieve_document(index_name=my_name, document_id=my_doc_id)
pprint(res_doc)


