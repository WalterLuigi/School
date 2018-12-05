#!/usr/bin/python3
from sys import argv

# Defines script and input file from CLI input
script, input_file = argv

# Creates function print_all
def print_all(f):
	print(f.read())

# Creates function rewind	
def rewind(f):
	f.seek(0)

# Creates function print_a_line	
def print_a_line(line_count, f):
	print(line_count, f.readline())
	print(f"Current line: {current_line}")

# Sets current_file to the opened version of input_file	
current_file = open(input_file)

# Prints the following string
print("First let's print the whole file:\n")

# Prints all lines from current_file
print_all(current_file)

# Prints the following string
print("Now let's rewind, kind of like a tape.")

# Sets current placement to beginning of current_file
rewind(current_file)

# Prints the following string
print("Let's print three lines:")

# Sets current line to 1 and then prints it
current_line = 1
print_a_line(current_line, current_file)

# Sets current line to current_line + 1 and then prints
current_line += 1
print_a_line(current_line, current_file)

# Does the same as the previous block of code
current_line += 1
print_a_line(current_line, current_file)
