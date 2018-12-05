#!/usr/bin/python3
#Defines types_of_people as int 10
types_of_people = 10
#Defines x as the following string with a variable inside it - String with int in it
x = f"There are {types_of_people} types of people."

#Defines binary as the string "binary"
binary = "binary"
#defines do_not as "don't"
do_not = "don't"
#Prints strings within the string pt 1
y = f"Those who know {binary} and those who {do_not}."

#Println x
print(x)
#Println y
print(y)

#Prints string y within the string - Nested strings pt 2
print(f"I said: {x}")
#Prints string y within the string - Nested strings pt 3
print(f"I also said: '{y}'")

#Sets boolean value for punny to bool True
punny = True
#Sets joke_evaluation to "Isn't that joke so funny" and adds a replacement field
joke_evaluation = "Isn't that joke so funny?! {}"

#Prints the joke_evaluation string and replaces the field with the value for "punny"
#Prints more strings in strings pt 4
print(joke_evaluation.format(punny))

#Sets var w to "This is the left side of..."
w = "This is the left side of..."
#Sets var e to "a string with a right side."
e = "a string with a right side."

#Combines the two strings and prints both
print(w + e)
