import re

data = "" # Again left out for clarity reasons. Get the data from
          # http://www.pythonchallenge.com/pc/def/equality.html

print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))