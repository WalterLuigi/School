#!/usr/bin/python

# Creates parent class
class Parent(object):

    # Override function
    def override(self):
        print("PARENT override()")

    # Implicit function
    def implicit(self):
        print("PARENT implicit()")

    # ALtered function
    def altered(self):
        print("PARENT altered()")

# Creates child class
class Child(Parent):

    # Override function
    def override(self):
        print("CHILD override()")

    # Altered function
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

# dad is a parent
dad = Parent()
# son is a child
son = Child()

# not override
dad.implicit()
# not override
son.implicit()

# not override
dad.override()
# override
son.override()

# not override
dad.altered()
# override
son.altered()