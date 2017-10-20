#!/usr/bin/python
import sys, pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
###Getting the DATABASE###
db = connection.test7
###Getting the Collection###
collection = db.zip_code
#users.find({"age": {"$gt": 20}})
collection.delete_many({"pop": {"$lt" : 1000}})
