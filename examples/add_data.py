from pprint import pprint

from examples.elasticclient import ElasticClient

client = ElasticClient()

index_name = "my_index"
mappings = {
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
client.create_index(index_name, mappings)

my_data = dict(
    name="my_name",
    main_text="some random text"
)

res = client.insert_document(index_name, my_data)
pprint(res.body)
