#!/usr/bin/python
#Neil A. Patel
#20150115

import pickle

file = open("pickledum.p", "r")
object = pickle.load(file)

print "Object:"
print object

print "\nItems:"
for item in object:
	print item
	
print "\nI in item:"
for item in object:
	for i in item:
		print i
	