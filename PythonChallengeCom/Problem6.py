#!/usr/bin/python
#Neil A. Patel
#20150112

import zipfile

file = open("channel/90052.txt", "r")
zfile = zipfile.ZipFile('channel.zip', 'r')
line = "nothing"

while "nothing" in line:
	for line in file:
		if "nothing" in line:
			if line[-3] == " ":
				nothingNum = line[-2:]
			elif line[-4] == " ":
				nothingNum = line[-3:]
			elif line[-5] == " ":
				nothingNum = line[-4:]
			else:
				nothingNum = line[-5:]
			file.close
			print zfile.getinfo(nothingNum+".txt").comment
			file = open(("channel/"+nothingNum+".txt"), "r")
		else:
			print line
			print zfile.getinfo(nothingNum+".txt").comment