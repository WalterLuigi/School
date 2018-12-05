#!/usr/bin/python3
#Imports argv module
from sys import argv

#Unpacks to script, name, and age
script, name, age = argv
#Sets var prompt to "$ "
prompt = '$ '

#Prints the following string for the user
print(f"Hi {name}, I'm the {script} script.")
#Prints "I'd like to ask you a few questions."
print("I'd like to ask you a few questions.")
#Asks the user if they like the script
print(f"Do you like me {name}?")
#Defines likes as value entered for prompt
likes = input(prompt)

#Asks user where they live
print(f"Where do you live {name}?")
#Assigns value to lives based on user input
lives = input(prompt)

#Asks what type of computer you have
print("What kind of computer do you have?")
#Assigns value to computer based on user input
computer = input(prompt)

#Prints a multiline string with variable values inside
print(f"""
Alright, so {name} you are {age} years old. 
You live in {lives}.  Not sure where that is.
You have a {computer} computer.  Nice.
And you said {likes} about liking me.
""")
