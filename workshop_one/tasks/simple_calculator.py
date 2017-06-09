#!/usr/bin/python3
# Task: Complete  Simple Calculator

def add: TODO 
   """This function adds two numbers"""
   pass TODO

def subtract: TODO
   """This function subtracts two numbers"""
   pass TODO

def multiply: TODO
   """This function multiplies two numbers"""
   pass TODO

def divide: TODO
   """This function divides two numbers"""
   pass TODO

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#if choice == '1': TODO
if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

