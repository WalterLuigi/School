#!/usr/bin/python
# Creates a string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Takes the previous string, splits it at the white space, and turns it into a list
stuff = ten_things.split(' ')
# Creates another list
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

# Takes the string and turns it into another list
new_stuff = ten_things.split(' ')
# Creates a new list
more_new_stuff = ["One", "Two", "Red", "Blue", "Three", "Four", "Giant", "Door"]

# While stuff has doesn't have 10 items, a new item is added to the list from more_stuff
#while len(stuff) != 10:
 #   next_one = more_stuff.pop()
 #   print("Adding: ", next_one)
 #   stuff.append(next_one)
 #   print(f"There are {len(stuff)} items now.")

# Roughly the same as above, but 12 instead of 10 and adds from more_new_stuff
while len(new_stuff) != 12:
    another_one = more_new_stuff.pop()
    print("Adding: ", another_one)
    new_stuff.append(another_one)
    print(f"There are {len(new_stuff)} items now.")

print("There we go: ", new_stuff)

print("Let's do some things with stuff.")

print(new_stuff[1])
print(new_stuff[-1]) # whoa! fancy
print(new_stuff.pop())
print(' '.join(new_stuff)) # what? cool!
print('#'.join(new_stuff[3:5])) # super stellar!