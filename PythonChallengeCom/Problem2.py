#!/usr/bin/python

data = open('Problem2Data.txt', 'r')
import string
str2 = ""

for line in data:
	for let in line:
		if string.find("%$@_#^+![]()&{}*\r\n", let) == -1:
			str2 = str2 + let

print str2