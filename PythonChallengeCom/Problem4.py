#!/usr/bin/python
#Neil A. Patel
#20140117

import urllib

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=25357'

for i in range(0, 400):
	urlFile = urllib.urlopen(url)
	line = urlFile.readline()
	if len(line) > 30 or 'nothing' not in line:
		print line
	url = url[:-5] + line[-5:]
	urlFile.close()