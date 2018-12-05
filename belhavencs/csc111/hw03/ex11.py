#!/usr/bin/python3
#Starts a while loop
while True:
	#Prompts for user's name
	name = input("Hello, what is your name? ")
	#Prints Nice to meet you and then name
	print(f"Nice to meet you {name}.")
	#Prompts for user age
	age = input("How old are you? ")
	#Prompts for user height
	height = input("How tall are you? ")
	#Prompts for user weight
	weight = input("How much do you weigh? ")
	#Prints users name, height, and weight
	print(f"So, {name} you're {age} old, {height} tall and {weight} heavy.")
	#Asks user if data is correct
	a = input("Is this correct? y/n ")
	#If user says data is correct, loop breaks
	if a =="y":
		break
	#If user says data is incorrect, loop continues
	elif a=="n":
		continue
	#If user enters character other than y or n, it tells them to please enter y or n, then continues loop
	else:
		print("Please enter y/n ")
