#!/usr/bin/python

# Defines function1
def function1(x, y):
	numbers = []
	for i in range(1, x, y):
		numbers.append(i)
	return numbers

# Prompts for value of x and converts it to type int    	    	
x = int(input("Set value for loop stop please: "))
# Prompts for value to iterate by and converts it to type int
y = int(input("Set value to increment by: "))

# Prints the string
print("The numbers: ")

# Starts a for loop that calls function 1 and prints the values of numbers
for num in function1(x, y):
	print(num)