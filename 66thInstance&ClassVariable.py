 
# In Python, class variables and instance variables are both types of variables but have different scopes and purposes within a class.

# Instance Variables:

# Instance variables are variables that are unique to each instance of a class.
# They are defined within methods of a class and are prefixed with self within those methods to reference the instance they belong to.
# Instance variables hold data that is specific to each instance of the class.
# They are typically initialized within the __init__ method.
# Example:
 
class MyClass:
    def __init__(self, x):
        self.x = x  # 'x' is an instance variable

# Class Variables:

# Class variables are variables that are shared among all instances of a class.
# They are defined outside of any method in the class and are typically placed directly below the class definition.
# Class variables are accessed using the class name rather than an instance of the class.
# They are used to store data that is shared among all instances of the class.
# Example: 

class MyClass:
    class_variable = 10  # 'class_variable' is a class variable

#  instance variables are specific to each instance of a class,
#  while class variables are shared among all instances of a class. 
#  Understanding the distinction between the two is crucial for effective object-oriented programming in Python.


# Here's a simple example to illustrate the use of both class variables and instance variables:

class Circle:
    pi = 3.14  # Class variable

    def __init__(self, radius):
        self.radius = radius  # Instance variable

    def calculate_area(self):
        return self.pi * (self.radius ** 2)

# Using class variable
print("The value of pi is:", Circle.pi)

# Creating instances with different radii
circle1 = Circle(5)
circle2 = Circle(7)

# Accessing instance variables and calculating area
print("Area of circle1:", circle1.calculate_area())
print("Area of circle2:", circle2.calculate_area())


# In this example, pi is a class variable that is shared among all instances of the Circle class,
# while radius is an instance variable that varies for each circle object.