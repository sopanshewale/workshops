#!/usr/bin/python
import re
s = "The   fox jumped   over    the log."
new_s = re.sub("\s\s+" , " ", s)

print (new_s)

