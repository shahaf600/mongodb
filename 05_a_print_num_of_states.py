#!/usr/bin/python
import sys, pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
###Getting the DATABASE###
db = connection.test7
###Getting the Collection###
collection = db.zip_code

print "The number of distinct states in this file is: " + str(len(collection.distinct("state")))
