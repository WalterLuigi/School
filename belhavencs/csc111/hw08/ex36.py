#!/usr/bin/python
import random

# Creates the bugroom
def bugroom():
	print("You enter a room full of swarming bugs")
	print("What do you do?")
	print("1. Enter swarm?")
	print("2. Offer honey?")
	choice = input("> ")
	
	# If you pick 1 you die
	if choice == "1":
		dead("You entered a swarm of angry bugs. That was smart.")
	# Choice 2 sends you back to start
	elif choice == "2":
		print("The bugs let you pass, and you wander into a clearing.")
		start()
	# All other options kill you
	else:
		dead("You wander aimlessly and fall into a pit. Good job!")

# Creates cloudroom
def cloudroom():
	print("You end up in a cloudy wooded area.")
	print("What do you do?")
	print("1. Walk around?")
	print("2. Go swimming in the clouds?")
	print("3. Go fish.")
	choice2 = input("> ")
	
	# If 1, you die
	if choice2 == "1":
		dead("You walk off a cliff. Good job!")
	# If 2, you also die
	elif choice2 == "2":
		dead("You jump right off a cliff. Good job!")
	# If 3, you go fishing
	elif choice2 == "3":
		fish()
	# Otherwise, you die	
	else:
		dead("Not sure what that was supposed to be. Good job!")

# Creates fish
def fish():
	catch_status = False
	while catch_status == False:
		fish = rng()
		if fish == 7:
			catch_status = True
			print("You caught a fish. Good job!")
			print("What do you do?")
			print("1. Eat the fish")
			print("2. Release the fish")
			choice3 = input("> ")
			
			if choice3 == "1":
				dead("The fish was poisonous. Good job!")
			elif choice3 == "2":
				print("The fish was magical. It rewards you with a map out of the mist. Good job!")
				exit()
			else:
				dead("You wander around aimlessly until a fish eats your head.")
		else:
			print("The fish got away.")
			print("Do you try again?")
			choice4 = input("y/n? ")
			
			if choice4 == "y":
				continue
			else:
				dead("The fish comes back with its mother and she eats you. Good job!")
			
			
def rng():
	fish_var = random.randint(5, 9)
	return fish_var

# Tells you why you died, says good job, and then exits
def dead(why):
	print(why)
	exit(0)

# Defines the game start function
def start():
	print("You are in a shrouded wood.")
	print("There is one path to your left and another to your right.")
	print("Which way do you go?")
	direction = input("> ")
	
	# If direction is right you go to bugroom
	if direction == "right":
		bugroom()
	# If direction is left you go to cloud room
	elif direction == "left":
		cloudroom()
	# Otherwise you die
	else:
		dead("You wander aimlessly and fall into a pit. Too bad you never learned to read.")

# Tells the game to start	
start()