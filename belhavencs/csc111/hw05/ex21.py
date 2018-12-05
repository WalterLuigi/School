#!/usr/bin/python

# Defines function add
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# Defines function subtract
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# Defines function multiply
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

# Defines function divide
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# Prints a basic string
print("Let's do some math with just functions!")

# Passes arguments to the called functions and assigns the result to age, height, weight, and iq
age = add(20, 6)
height = multiply(12, 6)
weight = subtract(200, 25)
iq = divide(200, 2)

# Prints the following line and the values for the substitution fields
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# Original version
what = add(age, subtract(weight, multiply(height, divide(iq, 2))))
# My modified version that does the inverse
what2 = (age + (weight - (height * (iq / 2))))

#Prints out the following line and the value of what
print("That becomes: ", what, "Can you do it by hand?", what2)
