from pprint import pprint

from examples.elasticclient import ElasticClient

client = ElasticClient()

index_name = "bad_reviews"

search_query = {
    "content": [
        {
            "type": "value",
            "name": "if_count",
            "sort": {"count": "desc"},
            "size": 10
        }
    ]
}

search_res = client.search(index_name, facets=search_query)
x =1