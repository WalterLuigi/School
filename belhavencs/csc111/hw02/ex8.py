#!/usr/bin/python3
#Defines formatter to "{} {} {} {}" these four braces are replacement fields
formatter = "{} {} {} {}"

#Calls the formatter command and fills the replacement fields with 1, 2, 3, and 4 then prints them
print(formatter.format(1, 2, 3, 4))
#Largely does the same as the above line, but instead prints the text one, two, three, and four
print(formatter.format("one", "two", "three", "four"))
#This time the replacement fields have boolean values inserted and printed
print(formatter.format(True, False, False, True))
#This time the function calls itself and simply prints the substitution fields within the substitution fields as though they are simple strings.
print(formatter.format(formatter, formatter, formatter, formatter))
#Prints Foo Bar BarFoo and KungFoo too
print(formatter.format(
    "Foo",
    "Bar",
    "BarFoo",
    "and KungFoo too"
))
