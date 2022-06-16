conda install -c anaconda pymongo
import pymongo
from pymongo import MongoClient
import pprint



client = MongoClient('mongodb://localhost:27018/')
ggr = client.ggr
limerick_places = ggr.limerick.places
limerick_posts = ggr.limerick.posts

# To get more than a single document as the result of a query we use the find() method

for post in limerick_places.find():
    pprint.pprint(post)

# If we just want to know how many documents match a query we can perform a count_documents()
limerick_places.count_documents({"name": "Limerick"}) # 6
limerick_places.count_documents({"country": "Irlanda"}) # 1314

### Indexing
# MongoDB provides a text index type that supports searching for string content in a collection.
# Indexes can improve the efficiency of read operations.
