#!/usr/bin/python
import sys, urllib2, json, pymongo, ast
from pymongo import MongoClient
from bson import json_util
from bson.json_util import loads,dumps
import collections
import urllib

connection = MongoClient('localhost', 27017)
###Getting the DATABASE###
db = connection.test5
###Getting the Collection###
collection = db.zip_code
#users.find({"age": {"$gt": 20}})
print "The number of cities with a populattion grater than 10000 is: " + str(collection.find({"pop": {"$gt" : 10000}}).count())
