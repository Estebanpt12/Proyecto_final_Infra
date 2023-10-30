from pymongo import MongoClient

MONGO_URI = 'mongodb://root:password@localhost/admin'

client = MongoClient(MONGO_URI)

db = client['uq']
collection = db['users']

print(collection.find_one({ "_id": 1 }))
