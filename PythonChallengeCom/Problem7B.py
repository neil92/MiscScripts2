#!/usr/bin/python
#Neil A. Patel
#20150112

arr = [105, 10, 16, 101, 103, 14, 105, 16, 121]
m = ""

for i, val in enumerate(arr):
	m = m + str(unichr(arr[i]))

print m