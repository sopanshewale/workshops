#!/usr/bin/python3

number_one = int(input("Enter First Number: "))
number_two = int(input("Enter Second Number: "))

try: 
    d = number_one / number_two
    print ("The division is: {0:.1f} ".format(d))
except ZeroDivisionError:
    print ("You tried to divide {} by zero".format(number_one))

