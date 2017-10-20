#!/usr/bin/python
import sys, pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
###Getting the DATABASE###
db = connection.test7
###Getting the Collection###
collection = db.zip_code

cursor2 = collection.find()
dict = dict()
for document in cursor2:
	if document['city'] in dict:
		dict[document['city']] += document['pop']
	else:
		dict[document['city']] = 0
city = ""
max = 0 #Because we talk about population it can't be under 0, so 0 is the starting point
for key in dict:
	if dict[key] > max:
		max = dict[key]
		city = key

print city + " has the most population with " + str(max) + " people"
