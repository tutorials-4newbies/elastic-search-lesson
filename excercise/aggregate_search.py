from pprint import pprint

from examples.elasticclient import ElasticClient

client = ElasticClient()

index_name = "bad_reviews"

search_query = {
    "categories": {
        "categorize_text": {
            "field": "content"
        }
    },

    "last_names": {
        "terms": {
            "field": "last_name.keyword",
            "size": 20
        }
    },
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-string-stats-aggregation.html
    "content_stats": {
        "string_stats": {
            "field": "content.keyword"
        }
    }

}

search_res = client.search(index_name, aggs=search_query)

aggregations_result = search_res.body.get("aggregations")

content_result = aggregations_result.get("content_stats")
print(f"Content: {content_result}\n\n")

last_names_buckets = aggregations_result.get("last_names").get("buckets")
for bucket in last_names_buckets:
    pprint(bucket)
