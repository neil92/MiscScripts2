#!/usr/bin/python
#K - M; O - Q; E - G

import string

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str2 = ""

for let in str:
	if string.find(string.ascii_letters, let) != -1: 
		asciiLet = ord(let)
		asciiLet = asciiLet + 2
		str2 = str2 + chr(asciiLet)
	else:
		str2 = str2 + let
print str2
