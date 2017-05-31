#!/usr/bin/python
import re
import sys

pattern = '\w[\w\.-]*@\w[\w\.-]+\.\w+'
#It allows alphanumeric characters, _, . and -.

text =  sys.argv[1]

match = re.search(pattern, text)

if match:
   print ("Email Address is valid")
else:
   print ("Not an email address")

