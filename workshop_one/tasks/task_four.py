#!/usr/bin/python3

even_count = 0
odd_count  = 0

for i in range(1,51):
    if i % 2 == 0:
       even_count = even_count + 1
    else: 
        odd_count = odd_count + 1

print ("Even Numbers Count: {}".format(even_count))
print ("Odd Numbers Count: {}".format(odd_count))


