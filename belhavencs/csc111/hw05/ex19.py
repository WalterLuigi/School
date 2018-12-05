#!/usr/bin/python3
# Creates function cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
	
def wine(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("You want some wine with that?")
	print("You were supposed to laugh.\n")
	
# Prints the following line	
print("We can just give the function numbers directly:")
# Passes the values 20 and 30 to the function cheese_and_crackers
cheese_and_crackers(20, 30)

# Prints the following line	
print("Or, we can use variables from our script:")
# amount_of_cheese is defined as 10
amount_of_cheese = 10
# amount_of_crackers is defined as 50
amount_of_crackers = 50

# Passes the falue of amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints the following string
print("We can even do math inside too:")
# Passes the values of 30 and 11 to the underlying vars in cheese_and_crackers
cheese_and_crackers(10 + 20, 5 + 6)

# Prints the following string
print("And we can combine the two, variables and math:")
# Adds 100 to amount_of_cheese and 1000 to amount_of_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#1
wine(amount_of_cheese, amount_of_crackers)
#2
wine(10, 20)
#3
wine(5 + 2, 10 + 2)
#4
wine(amount_of_cheese + 20, amount_of_crackers + 30)
#5
wine(amount_of_cheese - amount_of_crackers, amount_of_crackers - amount_of_cheese)
#6
wine(amount_of_cheese - 1, amount_of_crackers - 1)
#7
wine(amount_of_cheese * 1, amount_of_crackers * 2)
#8
wine(5 * 2, 8 * 30)
#9
wine(5 % 2, 40 % 3)
#10
wine(7 / 2, 40 * 3)

