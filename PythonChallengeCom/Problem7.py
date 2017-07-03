#!/usr/bin/python
#Neil A. Patel
#20150112

from PIL import Image

file = Image.open('oxygen.png', 'r')
lcolor = file.getpixel((0, 45))
color = lcolor
message = str(unichr(lcolor[0]))
for x in range(0,610):
	color = file.getpixel((x, 45))
	if color[0] != lcolor[0]:
		message = message + str(unichr(color[0]))
		lcolor = color

print message