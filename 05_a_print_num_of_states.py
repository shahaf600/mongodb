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

print "The number of distinct states in this file is: " + str(len(collection.distinct("state")))
