#!/usr/bin/python3
import sys

def get_factors(number):
    factors = []
    for i in range(1, number+1):
         if number %i == 0:
               factors.append(i)
    return factors
     

def get_common_members(l_one, l_two):
     common = []
     for e in l_one:
           if e in l_two:
               common.append(e)
 
     return common 



number_one = int(sys.argv[1])
number_two = int(sys.argv[2])

f_one = get_factors(number_one)
f_two = get_factors(number_two)

common_factors = get_common_members(f_one, f_two)

common_factors.sort() # factors sorted
hcf = common_factors[-1]

print ("The HCF of {} and {} are: {}".format(number_one, number_two, hcf))
