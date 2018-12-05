#!/usr/bin/python

# Creates list the_count
the_count = [1, 2, 3, 4, 5]
# Creates list fruits
fruits = ['apples', 'oranges', 'pears', 'apricots']
# Creates list change
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# assigns range(0, 6) to elements
elements = range(0, 6)

# iterates over elements and prints each individual element
for i in elements:
    print(f"Element was: {i}")
