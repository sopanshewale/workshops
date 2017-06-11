#!/usr/bin/python3

l = ['a', 'a', 'a', 'b', 'a', 'z']
d = {}

for element in l:
   d[element] = element

print (list(d.keys()))
