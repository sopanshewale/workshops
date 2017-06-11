#!/usr/bin/python3

with open('simple_data.txt', 'r') as f:
     for l in f:
        print (l)

print ("----------->")

with open('simple_data.txt', 'r') as f:
       print (f.read()) 


