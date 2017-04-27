#! /usr/bin/env python
import pymongo, sys, argparse

def getIP(addr, size, outputFile):
	output = ""
	output += "TARGET  " + str(addr)
	db_connect = pymongo.MongoClient(addr, 27017)
	try:
		listofnames = db_connect.database_names()
		for name in listofnames:
			output += "\n    DB NAME:" + name
			database = db_connect[name]
			collections = database.collection_names(include_system_collections=False)
			for collection in collections:
				if size:
					collectSize = database.get_collection(collection).count()
					output += "\n         " + collection + "---- count:" + str(collectSize)
				else:   
					output += "\n         " + collection
	except:
		pass
	if outputFile is None:
		print output
	else:
		with open(outputFile, 'w') as output_file:
			output_file.write(output)

def progress(part, whole):
	progStr = "Processing target "+str(part)+"/"+str(whole)+"\n"
	sys.stderr.write(progStr)

def main(file, ip, size, outputFile):
	if file is not None:
		num_lines = sum(1 for line in open(file))
		count = 1
		with open(file) as fileinput:
			for ip_address in fileinput:
				progress(count, num_lines)
				count += 1
				getIP(ip_address, size, outputFile)
	elif ip is not None:
		getIP(ip, size, outputFile)
	else:
		sys.exit('Please specify a file or IP address')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()                                               
	parser.add_argument("-f", type=str, dest="file", help="File of targets")
	parser.add_argument("-ip", type=str, help="Single IP target")
	parser.add_argument('-s', action='store_true', help="Toggle enumerating size")
	parser.add_argument("-o", type=str, dest="output", help="Directs the output to a name of your choice")
	args = parser.parse_args()
	main(args.file,args.ip,args.s,args.output)