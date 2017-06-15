#!/usr/bin/python3
import sys


def clean_str(my_str):
    number = ''
    for e in my_str:
        try:
            n = int(e)
            number = number + str(n)
        except: 
           pass 
    return number


my_number = clean_str(sys.argv[1])
print (my_number)

