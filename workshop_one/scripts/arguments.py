#!/usr/bin/python3

import sys

print (type(sys.argv))
print (sys.argv)

# Let us iterate through iterated via a for loop:

for i in range(len(sys.argv)):
    if i == 0:
        print ("script name: {}".format(sys.argv[0]))
    else:
        print ("{}. argument: {}".format(i,sys.argv[i]))
