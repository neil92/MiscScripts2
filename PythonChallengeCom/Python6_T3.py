#!/usr/python/bin
#Neil A. Patel
#20150112

import zipfile

file = zipfile.ZipFile('channel.zip', 'r')

obj = file.getinfo('90052.txt')

print obj.comment