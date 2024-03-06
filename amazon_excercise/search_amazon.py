from examples.elasticclient import ElasticClient

client = ElasticClient()

index_name = "amazon_toys"
# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html
query = {
    "size": 50,
    "query": {
        "bool": {
            "must": {
                "term": {'average_review_rating.keyword': '5.0 out of 5 stars'}
            },
            "filter": {
                "match": {
                    "product_name": {
                        "query": "cat",
                        "fuzziness": "AUTO"
                    }
                }
            }
        },
    },
    "aggs": {
        "manufacturers": {
            "terms": {
                "field": 'manufacturer.keyword'
            }
        }
    }
}

search_res = client.search(index_name, query)

hits = search_res.body.get('hits')
total = hits.get('total').get("value")
print(f"Total: {total}")
