# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a object inheriting from Animal
class Dog(Animal):
    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-a object inheriting from Animal
class Cat(Animal):
    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-a object
class Person(object):
    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# Employee is-a object inheriting from Person
class Employee(Person):
    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        # Here, we called the __init__() method of the Employee class (from the Person class)
        # instead of Employee.name = name
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a object inheriting from Fish
class Salmon(Fish):
    pass


# Halibut is-a object inheriting from Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet satan
mary.pet = satan

# frank is-a Employee and has-a name and salary
frank = Employee("Frank", 120000)

# frank has-a pet rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
