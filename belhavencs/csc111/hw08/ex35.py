#!/usr/bin/python

# Imports exit from sys module
from sys import exit

# Defines gold_room function
def gold_room():
    print("This room is full of gold.  How much do you take?")
    choice = input("> ")
    # Checks if user input is digit, if so it changes to type int
    if choice.isdigit() == True:
        how_much = int(choice)
    # Calls function dead and tells you to learn to type a number
    else:
        dead("Man, learn to type a number.")
	# Exits and tells you good job for not being greedy if number is less than 50
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    # Otherwise you die for being greedy
    else:
        dead("You greedy bastard!")

# Defines function bear_room
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # Bear has not moved
    bear_moved = False

    while True:
        choice = input("> ")
		# Bear kills you if you try to take honey
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        # Bear moves
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        # If bear has already moved, it kills you
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # If the bear has moved you go to the gold room
        elif choice == "open door" and bear_moved:
            gold_room()
        # If the bear has not moved it kills you
        elif choice == "open door" and not bear_moved:
            dead("The bear gets pissed and drowns you in honey.")
        else:
            print("I got no idea what that means.")

# Defines function cthulhu_room
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")
	# Flee restarts game
    if "flee" in choice:
        start()
    # Head kills you
    elif "head" in choice:
        dead("Well that was tasty!")
    # Else restarts this room
    else:
        cthulhu_room()

# Tells you why you died, says good job, and then exits
def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")
	# Left takes you into the bear room
    if choice == "left":
        bear_room()
    # Right takes you into cthulu room
    elif choice == "right":
        cthulhu_room()
    # Otherwise you die
    else:
        dead("You stumble around the room until you starve.")

# Tells the game to start
start()