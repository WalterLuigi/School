#!/usr/bin/python

# Prints a line
print("Let's practice everything.")
# Prints a line
print('You\'d need to know \'bout escapes with \\ that do:')
# Prints a line
print('\n newlines and \t tabs.')

# This is just ugly, but it proves a point. Tabs and new lines can be inserted anywhere in a string via escapes
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Prints another string
print("--------------")
# Prints the poem
print(poem)
# Prints a string
print("--------------")
# Does some math and defines it to five
five = 10 - 2 + 3 - 6
# Prints out that five is 5
print(f"Thise should be five: {five}")

# Defines function secret_formula
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
	
# Sets start_point to 10000	
start_point = 10000
# Passes start_point to function secret_formula and returns the results to variables
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
# Passes start_point to the replacement field
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
# Passes values to the fields
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# I prefer to do this, this way
start_point /= 10

# Prints a line
print("We can also do that this way:")
# passes the value to formula
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# Passes the list from within formula to the string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
