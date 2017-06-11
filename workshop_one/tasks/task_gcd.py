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

def get_gcd(n, m):
    f_one = get_factors(n)
    f_two = get_factors(m)
    common_factors = get_common_members(f_one, f_two)
    common_factors.sort() # factors sorted
    return common_factors[-1]


numbers = sys.argv[1:]
numbers = list(map(int, numbers))

hcf = numbers[0]
for n in numbers[1:]:
    tmp =  get_gcd(hcf, n)
    hcf = tmp

print ("The HCF of {} is {}".format(numbers, hcf))
