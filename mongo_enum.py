#! /usr/bin/env python
import pymongo
import sys
import argparse

parser = argparse.ArgumentParser()                                               
parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument('-s', action='store_true')
args = parser.parse_args()

with open(args.file) as fileinput:
	for ip_address in fileinput:
		print "\nTARGET  " + str(ip_address)
		db_connect = pymongo.MongoClient(ip_address, 27017)
		try:
			listofnames = db_connect.database_names()
			for name in listofnames:
				print "    DB NAME:" + name
				database = db_connect[name]
				collections = database.collection_names(include_system_collections=False)
				for collection in collections:
					if args.s:
						collectSize = database.get_collection(collection).count()
						print "         " + collection + "---- count:" + str(collectSize)
					else:	
						print "         " + collection
		except:
			pass
