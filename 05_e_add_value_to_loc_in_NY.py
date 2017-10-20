#!/usr/bin/python
import sys, urllib2, json, pymongo, ast
from pymongo import MongoClient
from bson import json_util
from bson.json_util import loads,dumps
import collections
import urllib

connection = MongoClient('localhost', 27017)
###Getting the DATABASE###
db = connection.test7
###Getting the Collection###
collection = db.zip_code

collection.update_many({"state":"NY"}, {"$push":{"loc": 999}})
