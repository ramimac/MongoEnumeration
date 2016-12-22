import pymongo
import sys
import argparse

parser = argparse.ArgumentParser()                                               
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

with open(args.file) as fileinput:
	for ip_address in fileinput:
		print "\nTARGET" + str(ip_address)
		db_connect = pymongo.MongoClient(ip_address, 27017)
		try:
			listofnames = db_connect.database_names()
			for name in listofnames:
				print "    DB NAME:" + name
				database = db_connect[name]
				collection = database.collection_names(include_system_collections=False)
				for collect in collection:
					print "         " + collect
		except:
			pass
