#!/usr/bin/python
#Neil A. Patel
#20150112

import os

for dirname, dirnames, filenames in os.walk('.\\channel'):
	for filename in filenames:
		file = open('.\\channel\\'+filename, 'r')
		for line in file:
			if "nothing" not in line:
				print line