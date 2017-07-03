#!/usr/bin/python

import re

data = open('Problem3Data.txt', 'r')
result = None
result2 = None
resultLWChar = ""
for line in data:
	result = re.search("[^A-Z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][^A-Z]", line)
	if result is not None:
		result2 = re.search('[a-z]', result.group(0))
		resultLWChar = resultLWChar + result2.group(0)
		result = None
		result2 = None

print resultLWChar