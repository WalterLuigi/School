#!/usr/bin/python

import scenes as myScene
from scenes import Shire, GoblinAttack, Forest, Clearing, Mountains, Battle, Death, Finished
from random import randint
from textwrap import dedent


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




# Creates the game map
class Map(object):

    # Creates a dictionary "scenes"
    scenes = {
        'shire': myScene.Shire(),
        'goblin_attack': myScene.GoblinAttack(),
        'forest': myScene.Forest(),
        'clearing': myScene.Clearing(),
        'mountains': myScene.Mountains(),
        'battle': myScene.Battle(),
        'death': myScene.Death(),
        'finished': myScene.Finished(),
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
a_map = Map('shire')
# Start map is passed to game engine and then assigned to a_game
a_game = Engine(a_map)
# Start the game
a_game.play()