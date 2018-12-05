#!/usr/bin/python

potatoes = "Beans, greens, potatoes, tomatoes"
lambs = "Lambs, rams, hogs, dogs"
chicken = "Chicken, turkeys, rabbit"
turkeys = "Chicken, turkeys, chicken, turkeys"
greens = "Beans, greens"
beans = "Beans, beans, beans, beans\n"

def NameIt(n):
	print("You name it!\n" * n)

def Chorus(a, b, c, d, e):
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)

def Song(count):
	while count >= 1:
		print("I got ")
		Chorus(potatoes, lambs, potatoes, chicken, "\n")
		NameIt(1)
		Chorus(potatoes, lambs, potatoes, turkeys, "\n")
		Chorus(potatoes, lambs, potatoes, chicken, "\n")
		NameIt(1)
		Chorus(potatoes, potatoes, greens, greens, beans)
		Chorus(potatoes, turkeys, potatoes, turkeys, "\n")
		NameIt(4)
		count -= 1 
		
print("Look!\n")		
Song(2)
	


