#!/usr/bin/python

# Creates class song
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Passes the following lyrics from song to happy_bday
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

# Passes the following lyrics from song to bulls_on_parade
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# Defines lyrics 2 as the following
lyrics2 = ["Beans, greens, potatoes, tomatoes",
            "Lambs, rams, hogs, dogs",
            "Chicken, turkeys, rabbit",
            "Chicken, turkeys, chicken, turkeys",
            "Beans, greens",
            "Beans, beans, beans, beans"]

# you_name_it is lyrics2 from song
you_name_it = Song(lyrics2)

# Now we print the songs
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

you_name_it.sing_me_a_song()