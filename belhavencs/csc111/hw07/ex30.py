#!/usr/bin/python

# Sets people to 30
people = 30
# Sets cars to 40
cars = 40
# Sets trucks to 15
trucks = 15

# If there are more cars than people the following string prints
if cars > people:
	print("We should take the cars.")
# If there are less cars than people the following string prints
elif cars < people:
	print("We should not take the cars.")
# If neither of the above conditions are met, the following string prints
else:
	print("We can't decide.")

# If trucks is greater than cars the following string prints	
if trucks > cars:
	print ("That's too many trucks.")
# If trucks is less than cars the following string prints
elif trucks < cars:
	print("Maybe we could take the trucks.")
# If the previous conditions aren't met, then this string prints
else:
	print("We still can't decide.")

# If people is greater than trucks, the following string prints	
if people > trucks:
	print("Alright, let's just take the trucks.")
elif people < trucks and people > cars:
	print("What should we do? Just take the trucks?")
# Otherwise this string prints
else:
	print("Fine, let's stay home then.")

