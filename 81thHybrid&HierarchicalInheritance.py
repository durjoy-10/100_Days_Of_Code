
# Hybrid Inheritance:
'''In Python, hybrid inheritance can involve combinations like 
multiple inheritance and multilevel inheritance.'''

# Parent class
class Animal:
    def speak(self):
        return "Animal speaks"

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return "Dog barks"

# Child class inheriting from both Animal and Dog
class Labrador(Dog):
    def fetch(self):
        return "Labrador fetches"

# Child class inheriting from both Animal and Labrador
class GuideDog(Labrador):
    def assist(self):
        return "Guide dog assists"

# Creating an instance of the GuideDog class
guide_dog = GuideDog()

# Calling methods
print(guide_dog.speak())  # Output: "Animal speaks"
print(guide_dog.bark())   # Output: "Dog barks"
print(guide_dog.fetch())  # Output: "Labrador fetches"
print(guide_dog.assist()) # Output: "Guide dog assists"




# Hierarchical Inheritance:
'''Hierarchical inheritance involves multiple subclasses inheriting from a single parent class.'''

class Vehicle:
    def move(self):
        return "Vehicle moves"

# Child class 1 inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        return "Car drives"

# Child class 2 inheriting from Vehicle
class Bike(Vehicle):
    def ride(self):
        return "Bike rides"

# Creating instances of the child classes
car = Car()
bike = Bike()

# Calling methods
print(car.move())  # Output: "Vehicle moves"
print(car.drive()) # Output: "Car drives"

print(bike.move()) # Output: "Vehicle moves"
print(bike.ride()) # Output: "Bike rides"
