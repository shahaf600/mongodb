#!/usr/bin/python
import sys, pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
###Getting the DATABASE###
db = connection.test5
###Getting the Collection###
collection = db.zip_code
#users.find({"age": {"$gt": 20}})
print "The number of cities with a populattion grater than 10000 is: " + str(collection.find({"pop": {"$gt" : 10000}}).count())
