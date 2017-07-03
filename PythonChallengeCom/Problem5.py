#!/usr/bin/python
#Neil A. Patel
#20140120

import pickle, urllib

url = "http://www.pythonchallenge.com/pc/def/banner.p"

handle = urllib.urlopen(url)
object = pickle.load(handle)
handle.close()
str = ""

for item in object:
	for i in item: 
		str = str + (i[0] * i[1])
	str = str + "\n"

print str