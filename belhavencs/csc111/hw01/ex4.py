#!/usr/bin/python3
#These lines assign values to the variables
cars = 100 #Defines cars as int with a value of 100
space_in_a_car = 4.0 #Sets as floating point instead of interger
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #Does math with interger value assigned to var cars and drivers
cars_driven = drivers #Defines cars_driven as equal to drivers
carpool_capacity = cars_driven * space_in_a_car #multiplies cars_driven by space_in_a_car and assigns to var carpool_capacity
average_passengers_per_car = passengers / cars_driven

#These lines print out the values of the previous variables
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
