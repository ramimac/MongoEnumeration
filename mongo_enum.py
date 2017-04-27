#! /usr/bin/env python
import pymongo, sys, argparse
# TODO: add output redirection via flag
	# then add back in progress printing if redirected

def getIP(addr, size):
	print "TARGET  " + str(addr)
	db_connect = pymongo.MongoClient(addr, 27017)
	try:
		listofnames = db_connect.database_names()
		for name in listofnames:
			print "    DB NAME:" + name
			database = db_connect[name]
			collections = database.collection_names(include_system_collections=False)
			for collection in collections:
				if size:
					collectSize = database.get_collection(collection).count()
					print "         " + collection + "---- count:" + str(collectSize)
				else:	
					print "         " + collection
	except:
		pass

def main(file,ip,size):
	if file is not None:
		#num_lines = sum(1 for line in open('myfile.txt'))
		with open(file) as fileinput:
			#print "1/{}".format(num_lines)
			for ip_address in fileinput:
				getIP(ip_address, size)
	elif ip is not None:
		getIP(ip, size)
	else:
		sys.exit('please specify a file or IP address')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()                                               
	parser.add_argument("-f", type=str, dest="file")
	parser.add_argument("-ip", type=str)
	parser.add_argument('-s', action='store_true')
	args = parser.parse_args()
	main(args.file,args.ip,args.s)