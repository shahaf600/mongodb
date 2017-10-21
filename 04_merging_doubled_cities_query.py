#!/usr/bin/python
import sys, pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads

connection = MongoClient('localhost', 27017)
###Getting the DATABASE###
db = connection.test7
###Getting the Collection###
collection = db.zip_code

cities = db.zip_code.aggregate([{ "$group": {"_id": '$city'}}])
print cities
new_docs = []

for i in cities:
    doc = {}
    doc['city'] = i['_id']
    documents = db.zip_code.find({"city": i['_id']})
    doc['loc'] = []
    doc['pop'] = 0

    for d in documents:
        doc['pop'] = doc['pop'] + d['pop']
        doc['loc'].append(d['loc'])
    doc['state'] = d['state']
    new_docs.append(doc)

# Instead of removing all the documents one by one, 
# dropping the collection is much faster
db.zip_code.drop()

db.zip_code.insert(new_docs)
