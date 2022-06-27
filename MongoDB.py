conda install -c anaconda pymongo
import pymongo
from pymongo import MongoClient
import pprint
import pandas as pd
from pandas import DataFrame



client = MongoClient('localhost', 27018)
db = client['ggr']
collection = db['limerick']

# To get more than a single document as the result of a query we use the find() method

for post in limerick.places.find():
    pprint.pprint(post)

# If we just want to know how many documents match a query we can perform a count_documents()
limerick.places.count_documents({"name": "Limerick"}) # 6
limerick.places.count_documents({"country": "Irlanda"}) # 1314

### Indexing
# MongoDB provides a text index type that supports searching for string content in a collection.
# Indexes can improve the efficiency of read operations.
collection.posts.index_information() # to know which index are present

collection.posts.find({"$text":{"$search":"nature"}}) # return a Cursor  -> transform it in a list
nature = collection.posts.find({"$text":{"$search":"ilovelimerick"}})
nature_list = list(nature) # 31301
limerick = collection.posts.find({"$text":{"$search":"limerick"}})
limerick_list = list(limerick) #979143

limerick_nature = collection.posts.find({"$text":{"$search":"\"limerick\" \"nature\""}})
limerick_nature_list = list(limerick_nature) #2381
df_lim_nat = pd.DataFrame(limerick_nature_list)

df_lim_nat.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2381 entries, 0 to 2380
# Data columns (total 12 columns):
#   Column               Non-Null Count  Dtype 
# ---  ------               --------------  ----- 
# 0   _id                  2381 non-null   object
# 1   created_at           2381 non-null   object
# 2   id                   2381 non-null   object
# 3   author_id            2381 non-null   object
# 4   lang                 2381 non-null   object
# 5   conversation_id      2381 non-null   object
# 6   entities             2376 non-null   object
# 7   public_metrics       2381 non-null   object
# 8   text                 2381 non-null   object
# 9   attachments          998 non-null    object
# 10  context_annotations  1179 non-null   object
# 11  geo                  228 non-null    object

# Df with 
df_green = pd.DataFrame(collection.posts.find({"$and" : 
                                               [{"$text":{"$search": "shannon nature ballyhoura Thomond Park Westfields peoplespark TedRussell Adare Wetlands shelbourne"}},
                                                {"geo": {"place_id": "54e862bb3ff2f749"}}]} )) # 1102 post
df_green1 = pd.DataFrame(collection.posts.find({ "$text":{"$search": "\"shannon\" \"limerick\""}} )) # 21636
df_green1_2 = pd.DataFrame(collection.posts.find({ "$text":{"$search": "\"shannon estuary\" \"limerick\""}} )) # 345
df_green1_3 = pd.DataFrame(collection.posts.find({ "$text":{"$search": "\"shannon river\" \"limerick\""}} )) # 776
df_green2 = pd.DataFrame(collection.posts.find({ "$text":{"$search": "\"park\" \"limerick\""}} )) # 20595
df_green3 = pd.DataFrame(collection.posts.find({ "$text":{"$search": "\"ballyhoura\" \"limerick\""}} )) # 1866
df_green4 = pd.DataFrame(collection.posts.find({ "$text":{"$search": "\"westfields\" \"limerick\""}} )) # 666
df_green5 = pd.DataFrame(collection.posts.find({ "$text":{"$search": "\"ted russel\" \"limerick\""}} )) # 69


df_limerick = pd.concat([df_lim_nat,df_green, df_green1, df_green1_2, df_green1_3, 
                         df_green2, df_green3, df_green4, df_green5 ]).drop_duplicates(subset = ["id"]).reset_index(drop=True)


