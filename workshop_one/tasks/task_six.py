#!/usr/bin/python3
#number = int(input("Enter Number: "))

import sys

number = int(sys.argv[1])
factors = []

for i in range(1, number+1):
     if number % i == 0:
           factors.append(i)
print ("The script name is: {} ".format(sys.argv[0]))
print ("The factors of {} are: {} ".format(number, factors))

