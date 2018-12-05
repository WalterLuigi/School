#!/usr/bin/python3
# Here's some new strange stuff, remember type it exactly.

#Defines days as "Mon Tue Wed Thu Fri Sat Sun"
days = "Mon Tue Wed Thu Fri Sat Sun"
#Defines months as Jan through Aug with a new line character after each month
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#Prints "Here are the days: " followed by the value of var days
print("Here are the days: ", days)
#Prints "Here are the months: " followed by the value of var months, note that each month name is followed by a newline character \n
print("Here are the months: ", months)

#Prints a literal, multiline string (Unlike what code academy says, it claims triple quotes are for multiline comments) 
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
Or maybe just 5 this time.
""")
