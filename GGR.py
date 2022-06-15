

conda install -c anaconda pymongo
import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')
ggr = client.ggr
limerick_places = ggr.limerick.places

# To get more than a single document as the result of a query we use the find() method

for post in limerick_places.find():
    pprint.pprint(post)

# If we just want to know how many documents match a query we can perform a count_documents()
limerick_places.count_documents({"name": "Limerick"})

