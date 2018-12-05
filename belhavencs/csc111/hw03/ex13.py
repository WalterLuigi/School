#!/usr/bin/python3
#Imports the argv library/module
from sys import argv
# read the WYSS section for how to run this
# Allows arguments to be set from command line
#script, first, second, third = argv
script, fourth = argv

#Prints "The script is called:" and then the script name
print("The script is called:", script)
#Prompts for user input for var first
first = input("What is your first variable? ")
#Prints "Your first variable is:" and then the first argument
print("Your first variable is:", first)
#Prompts for user input for var second
second = input("What is your second variable? ")
#Prints "Your second variable is:" then the second argument
print("Your second variable is:", second)
#Prompts for user input for var third
third = input("What is your third variable? ")
#Prints "Your third variable is:" then the third argument
print("Your third variable is:", third)
#Prints "Your fourth variable is:" then the fourth argument
print("Your fourth variable is:", fourth)

