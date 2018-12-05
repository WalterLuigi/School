#!/usr/bin/python

from graphviz import Digraph
import socket

# Opens a graph image named map
map = Digraph(comment='Map of DNS data')

# Opens lookupdata.txt and yanks all the lines from the file
with open("lookupdata.txt") as lookupdata:
	lines = lookupdata.readlines()

# Iterates over all the lines from the file
for line in lines:
	columns = line.split()
	domaindata = columns[0]
	columns.pop(0)
	ipdata = columns
	map.node(domaindata,domaindata)

	# Iterates over all the addresses in our IP data
	for addr in ipdata:

		# Tries to do a rDNS lookup and add it to our map
		try:
			foo = socket.gethostbyaddr(addr)
			reverseaddr = foo[0]
			map.node(reverseaddr,reverseaddr)
			map.edge(reverseaddr, domaindata)

		# If the above can't run, then it prints this
		except:
			print("No luck, skipping this address.")

# Saves and prints out our map
map.render('output/DNSmap.gv', view=True)