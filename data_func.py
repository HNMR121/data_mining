import pymongo

db_client = pymongo.MongoClient('mongodb://localhost:27017')
db = db_client['data_mining']
collection = db['magnit_products']

# for product in collection.find({'title': 'Дари играя'}):
# for product in collection.find({'title': {'$regex':'[Ш|ш]околад'}}):
for product in collection.find({'title': {'$regex':'[Ш|ш]околад','promo_name':'Дари играя'}}):
    print(product)