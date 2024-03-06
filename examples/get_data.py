from pprint import pprint

from examples.elasticclient import ElasticClient

client = ElasticClient()

index_name = "my_index"
document_id = "2FSQFY4B82VwloqZRxtW"

res = client.retrieve_document(index_name, document_id)
pprint(res.get("_source"))

search_res = client.search(index_name, {
    "query": {
        "match": {
            "name":
                {"query": "my_name"}
        }
    }
})
hits = search_res.body.get('hits')
total = hits.get('total')
pprint(f"Total: {total}")
for item in hits.get("hits"):
    document = item.get("_source")
    pprint(f"Document: {document}")
