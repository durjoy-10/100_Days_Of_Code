# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says something"

# Child class inheriting from Animal without overriding
class DogWithoutOverride(Animal):
    def bark(self):
        return f"{self.name} barks: Woof! Woof!"

# Child class inheriting from Animal with overriding
class DogWithOverride(Animal):
    def speak(self):
        return f"{self.name} says Woof! Woof!"

# Creating instances of both child classes
dog_no_override = DogWithoutOverride("Buddy")
dog_with_override = DogWithOverride("Max")

# Calling methods on instances
print("Without overriding:")
print(dog_no_override.speak())  # Output: "Buddy says something"
print(dog_no_override.bark())   # Output: "Buddy barks: Woof! Woof!"

print("\nWith overriding:")
print(dog_with_override.speak())  # Output: "Max says Woof! Woof!"
