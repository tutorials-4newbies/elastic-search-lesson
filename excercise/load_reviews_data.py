from pprint import pprint
import os
from examples.elasticclient import ElasticClient
from faker import Faker
from faker.providers import internet, date_time, person, color
import random
from datetime import date
fraud_ip = "1.1.1.1"
fake = Faker()
fake.add_provider(internet)
fake.add_provider(date_time)
fake.add_provider(person)
fake.add_provider(color)

client = ElasticClient()

index_name = "bad_reviews"
client.create_index(index_name=index_name)


documents = []

files_path = "../data"
files = os.listdir(files_path)
for file in files:
    with open(os.path.join(files_path, file)) as f:
        ip = fraud_ip if random.randint(0,20) > 17 else fake.ipv4()
        documents.append({
            "content": f.read(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.ascii_safe_email(),
            "ipv4": ip,
            "color": fake.color(),
            "likes": random.randint(0,1000),
            "created_at": fake.date_between_dates(date_start=date(year=2024, month=1, day=1))
        })
print(f"Set index: '{index_name}' with {len(files)} documents")
res = client.insert_documents(index_name, documents)
