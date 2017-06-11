#!/usr/bin/python3
import re

text = 'aaaakkkccccccd'
pattern = 'a+kkk(cc)+d?'
match = re.match(pattern, text)

if match:
   print ("I am satisfying the Rules")
else:
   print ("Nope - The rules are not satisfied")

