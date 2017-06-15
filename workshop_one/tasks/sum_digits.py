#!/usr/bin/python3
import sys

def sum_numbers(number):
       s = str(number)
       sum = 0
       for e in s:
           sum = sum + int(e)
       return sum


number = int(sys.argv[1])
print (sum_numbers(number))

