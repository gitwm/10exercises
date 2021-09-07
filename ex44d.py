"""Inheritance All Three Combined"""

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

# Implicit Inheritance
print("Implicit Inheritance")
dad.implicit()
son.implicit()

# Override Explicitly
print("Override Explicitly")
dad.override()
son.override()

# All Three Combined
print("All Three Combined")
dad.altered()
son.altered()
