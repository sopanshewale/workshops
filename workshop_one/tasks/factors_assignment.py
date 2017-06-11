#!/usr/bin/python3
import sys
import time

################## Assignment: Memoization ###################
# Memoization is an optimization technique used primarily to speed up computer
# programs by storing the results of expensive function calls and returning the 
# cached result when the same inputs occur again. 
#
# One important use of dictionaries from Python is for memoization, in which a 
# previously computed result is stored in the table and retrieved later. 
# Memoization is a powerful technique for building efficient algorithms, especially in a functional language.
#
#            Expected Results are as follow:
# Enter Number:>12345678912345
# You entered: 12345678912345
# Working to find factors of 12345678912345 ...
# --- 2.0262882709503174 seconds ---
# Enter Number:>12345678912345
# You entered: 12345678912345
# Working to find factors of 12345678912345 ...
# --- 0.00011229515075683594 seconds ---
# 
############################################

# global dictionary of  factors
# number --> List consisting of Factors 

catched_factors = {} 


def factors(number):

    if number == 1: 
       catched_factors[1] = [1]
       return catched_factors[1]

    for n in range(1, number):                         # Remember, range starts with 0
                                                       # upper bound is number-1
        if number % (n+1) == 0:
           if n+1 < number:                            # Case: The number has smaller divisor  
              quotient = int(number /(n+1))
                                                       # TODO - Enable Memoization the Programmer 
              quotient_factors            = factors(quotient)
              n_factors                   = factors(n+1)
              factors_list                = quotient_factors + n_factors + [number]
              sorted_factors_list         = sorted(unify_list(factors_list))
              catched_factors[number]     = sorted_factors_list
              return catched_factors [number]    
           if n+1 == number:                           # Case - number is Prime Number 
             catched_factors[number] = [1, n+1]
             return  catched_factors[number] 

def unify_list(mylist):
    # TODO - develop function to return sorted list
    return mylist.keys() 

if __name__ == '__main__':
   number = 'number'
   while (number !='0'):
       number = input("Enter Number:>") 
       print ("You entered: " + number) 
       print ("Working to find factors of %s ..." % (number))
       
       # Time it
       start_time = time.time()
       L = factors(int(number))
       print("--- %s seconds ---" % (time.time() - start_time)) 
