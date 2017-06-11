#!/usr/bin/python3

# try input : racecar, madam, sas, car, pune
def reverse_text(text):
     return text[::-1] 

def is_palindrome(text):
    if text == reverse_text(text):
         return True
    else: 
         return False 

something = input("Enter text: ")

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

