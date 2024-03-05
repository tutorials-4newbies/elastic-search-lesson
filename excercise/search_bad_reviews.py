from pprint import pprint

from examples.elasticclient import ElasticClient

client = ElasticClient()

index_name = "bad_reviews"

# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html
match_query = {
    "match":
        {
            "content": "1935"
        }
}

# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-regexp-query.html
regex_query = {
    "regexp":
        {
            "content": "193\d"
        }
}

# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-fuzzy-query.html
fuzzy_query = {
    "fuzzy": {
        "content": "Camerol"
    }
}

search_res = client.search(index_name, query=fuzzy_query)

hits = search_res.body.get('hits')

for item in hits.get("hits"):
    document = item.get("_source")
    doc_id = item.get("_id")
    score = item.get("_score")
    content = item.get("_source")
    print(f"Id: {doc_id}, score: {score}, \n  content: {content}\n")

total = hits.get('total')
print(f"Total: {total}")
