#!/usr/bin/python

# Prints the following multiline string
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

# Sets the value of door based on prompted user input
door = input("> ")

# Starts an if statement for if user input 1
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
	# Sets bear based on user input
    bear = input("> ")
	# If bear is 1 it prints the string
    if bear == "1":
        print("The bear eats your face off.  Good job!")
	# If bear is 2 it prints the string
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
	# Otherwise, this sequence starts
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away. Good job!")
        print("You are left in the room.")
        print("What do?")
        print("1. Eat the cake.")
        print("2. Leave the room.")
        
		# Prompts user for input for whatdo
        whatdo = input("> ")
        
		# If 1, the cake is a lie
        if whatdo == "1":
        	print("The cake is a lie. Good job!")
		# If 2, you die
        elif whatdo == "2":
        	print("You fall into an endless abyss never to be seen again. Good job!")
		# Otherwise, wait what?
        else:
        	print("Your keyboard is infested by bees. Good job!")   

# If door is 2, this sequence starts
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

	# Prompts user input for insanity
    insanity = input("> ")

	# If insanity is 1 or 2, these lines print
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    # Otherwise this runs
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

# This runs if the initial input is not 1 or 2
else:
    print("You stumble around and fall on a knife and die.  Good job!")
