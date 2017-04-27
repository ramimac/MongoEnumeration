#!/usr/bin/env python

import csv, json, re, collections

with open('shodan_data.csv', 'rb') as filecsv:
	readerA = csv.reader(filecsv, delimiter=',')
	first = False
	ban = {}
	for row in readerA:
		if first:
			banner = row[2][:-1]
			ip = row[0]
			if 'totalSize' in banner:
				regex = re.compile(r"\"totalSize\": ([0-9]+.[0-9]+),")
				result = regex.search(banner)
				if not (result == None):
					size = result.group(1)
					ban[float(size)] = (banner,ip)
		else:
			first = True
	od = collections.OrderedDict(sorted(ban.items(), reverse=True))
	for k, v in od.iteritems():
		#print "size",k,"ip",v[1]
		print v[1]

