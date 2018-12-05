#!/usr/bin/python

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    print("I'm a dog. Woof woof!")

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    print("I'm a cat. Meow!")

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## person has-a salary
        self.salary = salary

    print("Let's get this bread y'all!")

## Fish is-a object
class Fish(object):
    def __init__(self, name):
        ## ??
        self.name = name

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a pet cat named Satan
mary.pet = satan

## Frank is-an employee with a salary of 120000
frank = Employee("Frank", 120000)

## Frank has-a pet dog named Rover
frank.pet = rover

## flipper is-a fish
flipper = Fish("Flipper")

## crouse is-a salmon
crouse = Salmon("Crouse")

## harry is-a halibut
harry = Halibut("Harry")

## dinner is a salmon named Fredrick, a halibut named Harold, and a generic fish named Foobar
dinner = [Salmon("Fredrick"), Halibut("Harold"), Fish("Foobar")]

## pets are Satan and Rover
pets = {mary: mary.pet, frank: frank.pet}