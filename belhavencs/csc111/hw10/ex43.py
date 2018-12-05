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


# This is the game engine
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    # Function play defines current and last scene
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        # Iterates into the next scene
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


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


# Creates Central Corridor scene
class CentralCorridor(Scene):

    # Creates enter function
    def enter(self):
        print(dedent("""
             The Gothons of Planet Percal #25 have invaded your ship and
             destroyed your entire crew.  You are the last surviving
             member and your last mission is to get the neutron destruct
             bomb from the Weapons Armory, put it in the bridge, and
             blow the ship up after getting into an escape pod.

             You're running down the central corridor to the Weapons
             Armory when a Gothon jumps out, red scaly skin, dark grimy
             teeth, and evil clown costume flowing around his hate
             filled body.  He's blocking the door to the Armory and
             about to pull a weapon to blast you.
             """))

        # What do you do to survive the Gothon attack?
        action = input("> ")

        # If you shoot, the Gothons get mad and kill you
        if action == "shoot!":
            return 'battle'

        # If you try to dodge, you hit your head and die
        elif action == "dodge!":
            print(dedent("""
                  Like a world class boxer you dodge, weave, slip and
                  slide right as the Gothon's blaster cranks a laser
                  past your head.  In the middle of your artful dodge
                  your foot slips and you bang your head on the metal
                  wall and pass out.  You wake up shortly after only to
                  die as the Gothon stomps on your head and eats you.
                  """))
            return 'death'

        # If you try to tell a joke, you get lucky and manage to get to the armory
        elif action == "tell a joke":
            print(dedent("""
                  Lucky for you they made you learn Gothon insults in
                  the academy.  You tell the one Gothon joke you know:
                  Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                  fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
                  not to laugh, then busts out laughing and can't move.
                  While he's laughing you run up and shoot him square in
                  the head putting him down, then jump through the
                  Weapon Armory door.
                  """))
            return 'laser_weapon_armory'

        # Otherwise you just repeat this scene
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


# Creates Armory scene
class LaserWeaponArmory(Scene):

    # Creates enter function
    def enter(self):
        print(dedent("""
              You do a dive roll into the Weapon Armory, crouch and scan
              the room for more Gothons that might be hiding.  It's dead
              quiet, too quiet.  You stand up and run to the far side of
              the room and find the neutron bomb in its container.
              There's a keypad lock on the box and you need the code to
              get the bomb out.  If you get the code wrong 10 times then
              the lock closes forever and you can't get the bomb.  The
              code is 3 digits.
              """))

        # Creates a random 3 digit code for the player to guess
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        # Prompts player to guess
        guess = input("[keypad]> ")
        # You have made no guesses, yet
        guesses = 1
        # Cheat code to get past this room
        cheatcode = "777"

        # If guess is wrong, add one to guess count and reprompt
        while guess != (cheatcode or code) and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        # If guess is correct, you can enter the bridge
        if guess == code or cheatcode:
            print(dedent("""
                  The container clicks open and the seal breaks, letting
                  gas out.  You grab the neutron bomb and run as fast as
                  you can to the bridge where you must place it in the
                  right spot.
                  """))
            return 'the_bridge'
        
        # Otherwise you get trapped and die, my dude
        else:
            print(dedent("""
                  The lock buzzes one last time and then you hear a
                  sickening melting sound as the mechanism is fused
                  together.  You decide to sit there, and finally the
                  Gothons blow up the ship from their ship and you die.
                  """))
            return 'death'


# Creates Bridge scene
class TheBridge(Scene):

    # Creates enter function
    def enter(self):
        print(dedent("""
              You burst onto the Bridge with the netron destruct bomb
              under your arm and surprise 5 Gothons who are trying to
              take control of the ship.  Each of them has an even uglier
              clown costume than the last.  They haven't pulled their
              weapons out yet, as they see the active bomb under your
              arm and don't want to set it off.
              """))

        # What do you do?
        action = input("> ")

        # If you panic and throw the bomb, you die
        if action == "throw the bomb":
            print(dedent("""
                  In a panic you throw the bomb at the group of Gothons
                  and make a leap for the door.  Right as you drop it a
                  Gothon shoots you right in the back killing you.  As
                  you die you see another Gothon frantically try to
                  disarm the bomb. You die knowing they will probably
                  blow up when it goes off.
                  """))
            return 'death'

        # If you slowly place the bomb, you manage to escape
        elif action == "slowly place the bomb":
            print(dedent("""
                  You point your blaster at the bomb under your arm and
                  the Gothons put their hands up and start to sweat.
                  You inch backward to the door, open it, and then
                  carefully place the bomb on the floor, pointing your
                  blaster at it.  You then jump back through the door,
                  punch the close button and blast the lock so the
                  Gothons can't get out.  Now that the bomb is placed
                  you run to the escape pod to get off this tin can.
                  """))

            return 'escape_pod'
        
        # Otherwise this scene repeats
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


# Creates the Escape Pod scene
class EscapePod(Scene):

    # Defines the scene enter function
    def enter(self):
        print(dedent("""
              You rush through the ship desperately trying to make it to
              the escape pod before the whole ship explodes.  It seems
              like hardly any Gothons are on the ship, so your run is
              clear of interference.  You get to the chamber with the
              escape pods, and now need to pick one to take.  Some of
              them could be damaged but you don't have time to look.
              There's 5 pods, which one do you take?
              """))

        # Randomly assigns the good pod to 1-5
        good_pod = randint(1,5)
        # Let's the user guess which pod is good
        guess = input("[pod #]> ")
        # Cheat code to get past this scene
        cheatcode = 777

        # If you don't guess the good pod, you die
        if int(guess) != (cheatcode or good_pod):
            print(dedent(f"""
                  You jump into pod {guess} and hit the eject button.
                  The pod escapes out into the void of space, then
                  implodes as the hull ruptures, crushing your body into
                  jam jelly.
                  """))
            return 'death'
        
        # Otherwise you win and go to finished scene
        else:
            if int(guess) == good_pod:
                print(dedent(f"""
                    You jump into pod {good_pod} and hit the eject button.
                    The pod easily slides out into space heading to the
                    planet below.  As it flies to the planet, you look
                    back and see your ship implode then explode like a
                    bright star, taking out the Gothon ship at the same
                    time.  You won!
                    """))
                return 'finished'
            else:
                print(dedent("""
                    You're a dirty cheater, but you won!
                    Your mother must be really proud!
                    """))
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
                  Quick on the draw you yank out your blaster and fire
                  it at the Gothon.  His clown costume is flowing and
                  moving around his body, which throws off your aim.
                  You get lucky and your laser hits his costume, but also
                  pierces his squishy clown body. The other Gothons stand
                  around in shock as you rush through the Weapon Armory
                  door.                  
                  """))
            return 'laser_weapon_armory'
        # Otherwise you die
        else:
            print(dedent("""
                  Quick on the draw you yank out your blaster and fire
                  it at the Gothon.  His clown costume is flowing and
                  moving around his body, which throws off your aim.
                  Your laser hits his costume but misses him entirely.
                  This completely ruins his brand new costume his mother
                  bought him, which makes him fly into an insane rage
                  and blast you repeatedly in the face until you are
                  dead.  Then he eats you.
                  """))
            return 'death'



# Creates the games final scene
class Finished(Scene):

    # Woo, you won the game
    def enter(self):
        print("You won! Good job.")
        return 'finished'


# Creates the game map
class Map(object):

    # Creates a dictionary "scenes" with central corridor, laser weapon armory, the bridge, the escape pod, death, and finished
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'battle': Battle(),
        'death': Death(),
        'finished': Finished(),
    }

    # Sets the start scene
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # Sets the next scene and returns the value
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    # Returns the opening scene
    def opening_scene(self):
        return self.next_scene(self.start_scene)




# Start map is central corridor
a_map = Map('central_corridor')
# Start map is passed to game engine and then assigned to a_game
a_game = Engine(a_map)
# Start the game
a_game.play()