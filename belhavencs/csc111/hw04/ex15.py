#!/usr/bin/python3
#Imports argv module
from sys import argv

#Defines argv variables via user input at terminal
script, filename = argv

#Passes the data in filename to txt
txt = open(filename)
print("Please type your filename again for verification.")
#Prompts for user input to verify file is correct
filename2 = input("> ")
#Determines if values match
boolvar = filename == filename2
#Prints out Here's your file and then what the user input
print(f"Here's your file {filename}: ")
#Prints out verification status
print(f"Verification: {boolvar}")
#Prints out the data from the file the user input
print(txt.read())
#Closes out file
txt.close()

#Asks for the filename again
#print("Type the filename again:")
#Assigns file again to user input, uses "> " as the prompt
#file_again = input("> ")

#Assigns data from file_again to txt_again
#txt_again = open(file_again)

#Prints out the data from the user input file
#print(txt_again.read())
#txt_again.close()
