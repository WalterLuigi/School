#!/usr/bin/python3
#Prints the string "Mary had a little lamb."
print("Mary had a little lamb.")
#Prints the string "Its fleece was white as snow." 'snow' is substituted into the replacement field
print("Its fleece was white as {}.".format('snow'))
#Prints the string "And everywhere that Mary went."
print("And everywhere that Mary went.")
#Prints out 10 periods
print("." * 10)  # what'd that do?

#Defines end1 as C
end1 = "C"
#Defines end2 as h
end2 = "h"
#Defines end3 as e
end3 = "e"
#Defines end4 as e
end4 = "e"
#Defines end5 as s
end5 = "s"
#Defines end6 as e
end6 = "e"
#Defines end7 as B
end7 = "B"
#Defines end8 as u
end8 = "u"
#Defines end9 as r
end9 = "r"
#Defines end10 as g
end10 = "g"
#Defines end11 as e
end11 = "e"
#Defines end12 as r
end12 = "r"

# watch end = ' ' at the end.  try removing it to see what happens
#Prints Cheese with an extra space at the end, removing end = ' ' prints Burger on a new line
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
#Prints Burger
print(end7 + end8 + end9 + end10 + end11 + end12)
