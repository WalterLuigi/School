#!/usr/bin/python3
#Imports argv module
from sys import argv

#Assigns values to script and filename
script, filename = argv

#Prints We're going to erase and the value of filename
print(f"We're going to erase {filename}.")
#Tells user to hit CTRL-C to kill process
print("If you don't want that, hit CTRL-C (^C).")
#Prints If you want to do that hit RETURN
print("If you do want that, hit RETURN.")

#Uses ? as an input prompt
input("?")

#Prints that it's Opening the file...
print("Opening the file...")
#Assigns the value of filename to target, and 'w' enables write access
target = open(filename, 'w')
#Prints the following string
print("Truncating the file.  Goodbye!")
#Truncates the contents of target
target.truncate()

#Prints that it will prompt user for input
print("Now I'm going to ask you for three lines.")

#Prompts for input on line1
line1 = input("line 1: ")
#Prompts for input on line2
line2 = input("line 2: ")
#Prompts for input on line3
line3 = input("line 3: ")

#Prints "I'm going to write these to the file."
print("I'm going to write these to the file.")

#Writes val of line1, line2, and line3 to file with newline characters after each
target.write(f"{line1}\n{line2}\n{line3}\n")
#Writes new line
#target.write("\n")
#Writes val of line2 to file
#target.write(line2)
#Writes new line to file
#target.write("\n")
#Writes val of line3 to file
#target.write(line3)
#Writes new line to file
#target.write("\n")
#Closes target
target.close()
#Opens file with read access
read = open(filename, 'r')
print("Next we read the file for validity")
print(read.read())

#Prints And finally, we close it
print("And finally, we close it.")
#Closes target
read.close()
