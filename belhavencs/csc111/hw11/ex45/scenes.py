#!/usr/bin/python

from sys import exit
from random import randint
from textwrap import dedent

# Set's the Scene class
class Scene(object):

    # Creates function enter
    # This should not be seen unless a scene is called improperly
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

# Creates Shire scene - aka start
class Shire(Scene):

    # Creates enter function
    def enter(self):
        print(dedent("""
             You wake up in your bed. You open the door
             and see a sunny day in the Shire.
             Suddenly you start to hear screams of panic from
             several roads away.
             What do you do?
             """))

        # What do you do?
        action = input("> ")

        # If you investigate, you stumble into the goblin attack
        if action == "investigate":
            return 'goblin_attack'

        # If you run, you end up in the forest
        elif action == "run":
            print(dedent("""
                  You run away from your home like a coward.
                  The screams of your friends and family slowly die
                  down as you get further and further away.
                  """))
            return 'forest'

        # If you try to tell a joke, you get lucky and manage to get to the armory
        elif action == "hide":
            print(dedent("""
                  You attempt to hide in your home, but soon you realize the screams
                  were due to a band of goblins sacking the shire.
                  They find you next and set fire to your home.
                  """))
            return 'death'

        # Otherwise you just repeat this scene
        else:
            print("DOES NOT COMPUTE!")
            return 'shire'

# Creates GoblinAttack scene
class GoblinAttack(Scene):

    # Creates enter function
    def enter(self):
        print(dedent("""
              You run into the town center only to see the town ablaze
              and your neighbors slaughtered. To your horror a pack of goblins
              has raided your town. what do you do?
              """))

        # Prompts player to guess
        action = input("> ")

        # If guess is correct, you can enter the bridge
        if action == "attack":
            return 'battle'
        
        # Otherwise you get trapped and die, my dude
        else:
            print(dedent("""
                  The goblins flank you and catch you by surprise.
                  This results in your death.
                  """))
            return 'death'

# Creates Forest scene
class Forest(Scene):

    # Creates enter function
    def enter(self):
        print(dedent("""
              You make your way into a dark forest. There is a thick fog obscuring your
              vision. There are two paths. One to your left, and one to the right.
              What do you do?
              """))

        # What do you do?
        action = input("> ")

        # If you go left you end up in a clearing
        if action == "go left":
            return 'clearing'

        # If you go right, you end up in the mountains
        elif action == "go right":
            return 'mountains'
        
        # Otherwise this scene repeats
        else:
            print("DOES NOT COMPUTE!")
            return 'forest'

# Creates Clearing scene
class Clearing(Scene):

    # Creates enter function
    def enter(self):
        print(dedent("""
              You enter a clearing. There is a lake in the center.
              A lady rises from the lake and lobs Excalibur at you.
              You roll for luck.
              """))

        # What do you do?
        luck = randint(0,9)
        # If you are lucky you win
        if luck >= 7:
            print(dedent("""
            You catch the sword and become the one true king
            of Narnia. Good job!
            """))
            return 'finished'
        # Otherwise you die, you probably will die
        else:
            print(dedent("""
            You never were any good at playing catch.
            The sword impales you.
            """))
            return 'death'

# Creates Mountains scene
class Mountains(Scene):

    # Creates enter function
    def enter(self):
        print(dedent("""
              You approach a large mountain. Do you climb it,
              or go around?
              """))

        # What do you do?
        action = input("> ")

        # If you climb the mountain you end up in a very similar clearing
        if action == "climb":
            return 'clearing'

        # If you go around it, the goblins kill you
        elif action == "go around":
            print(dedent("""
                You run into the goblins that attacked your village,
                but you are unprepared so they end up killing you.
                """))
            return 'death'
        
        # Otherwise this scene repeats
        else:
            print("DOES NOT COMPUTE!")
            return "mountains"

# Creates the games final scene
class Finished(Scene):

    # Woo, you won the game
    def enter(self):
        print("You won! Good job.")
        return 'finished'

# Creates battle scene
class Battle(Scene):

    # Defines the enter method
    def enter(self):
        # Sets status to a random number between 1 and 9
        battlestatus = randint(1,9)
        
        # If this number is greater than 5, you win
        if battlestatus > 5:
            print(dedent("""
                  You get a lucky hit in and manage to kill the goblin chief.
                  The goblins panic and retreat. You chase them into the forest.                 
                  """))
            return 'Forest'
        # Otherwise you die
        else:
            print(dedent("""
                  You miss your attack and get clobbered upside your head
                  by a goblin grunt. What a pitiful death.
                  """))
            return 'death'

# This is the death scene
class Death(Scene):

    # A list of jokes for whenever you die
    quips = [
        "You died.  You kinda suck at this.",
         "Your Mom would be proud...if she were smarter.",
         "Such a loser.",
         "I have a small puppy that's better at this.",
         "You're worse than your Dad's jokes."
    ]

    # When you die it prints a random quip and then exits
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)