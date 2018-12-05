#!/usr/bin/python3
#Defines tabby_cat as "\tI'm tabbed in." The \t is an escaped tab character.
tabby_cat = "\tI'm tabbed in."
#Defines persian_cat as "I'm split\non a line." with \n being a new line character, of course
persian_cat = "I'm split\non a line."
#Defines backslash_cat as "I'm \\ a \\ cat." The \\ escapes the back slash character so it will be read as part of the string by the interpreter
backslash_cat = "I'm \\ a \\ cat."

#Defines fat cat as a multiline, tabbed list of foods, \n enters a newline before the tab in * Grass
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

#Prints the value of tabby_cat
print(tabby_cat)
#Prints the value of persian_cat
print(persian_cat)
#Prints the value of backslash_cat
print(backslash_cat)
#Prints the value of fat_cat
print(fat_cat)
