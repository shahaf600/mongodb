#!/usr/bin/python
import sys, pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
###Getting the DATABASE###
db = connection.test7
###Getting the Collection###
collection = db.zip_code

############## Print all the cities with population between 500 and 20000, in the states "MA" or "NH" #######

cursor = collection.find({
	'$and': [
		{"pop": {"$gt" : 500}} , 
		{"pop": {"$lt" : 20000}},
		{ '$or': [ { "state" : "MA" }, { "state" : "NH" } ] }
		]
	})


############## The printing of first query and Print the sum of the above states cities population count, per state. ############
maSum = 0
nhSum = 0
print "The cities which have population between 500 and 20000 are:"
for document in cursor:
	print document['city']
	if document['state'] == "MA":
		maSum = maSum + document['pop']
	else:
		nhSum = nhSum + document['pop']

print "The population of cities which have population between 500 and 20000 in MA is: " + str(maSum)
print "The population of cities which have population between 500 and 20000 in NH is: " + str(nhSum)

############## Print how much population there is per state except from the states above ("MA", "NH") ########3
cursor2 = collection.find({
                 'state': { '$nin': ["MA", "NH"] }
        })
dict = dict()
for document in cursor2:
	if document['state'] in dict:
		dict[document['state']] += document['pop']
	else:
		dict[document['state']] = 0
for key in dict:
	print key, dict[key]
