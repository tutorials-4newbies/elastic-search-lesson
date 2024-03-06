import csv
import os

from examples.elasticclient import ElasticClient

client = ElasticClient()

index_name = "amazon_toys"
client.create_index(index_name)
filename = "amazon_co-ecommerce_sample.csv"
documents = []
with open(os.path.join("../csv_data", filename)) as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    for row in reader:
        documents.append(row)

res = client.insert_documents(index_name, documents)
print(f"Set index: '{index_name}' with {len(documents)} documents")
