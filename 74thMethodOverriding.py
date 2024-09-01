# Suppose we have a base class Employee with a method calculate_salary() to calculate the salary of an employee.
# We'll create two subclasses FullTimeEmployee and PartTimeEmployee which override the calculate_salary() method 
# to calculate the salary specific to each type of employee.

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, 40, salary / 40)  # Assuming full-time employees work 40 hours per week

    def calculate_salary(self):
        return super().calculate_salary() * 4  # Assuming monthly salary for full-time employees

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return super().calculate_salary() * 4  # Assuming monthly salary for part-time employees

# Creating instances of subclasses
full_time_emp = FullTimeEmployee("John", 4000)  # Monthly salary of $4000
part_time_emp = PartTimeEmployee("Alice", 20, 25)  # 20 hours per week, hourly rate of $25

# Calling the overridden method
print("Full-Time Employee Salary:", full_time_emp.calculate_salary())  # Output: Full-Time Employee Salary: 16000
print("Part-Time Employee Salary:", part_time_emp.calculate_salary(),"\n\n\n\n")  # Output: Part-Time Employee Salary: 2000

#________________________________________________________________________________________________________________________________


# Let's consider a more complex example involving a base class Shape with a method area() to calculate the area
# of various shapes, and subclasses Rectangle and Circle that override the area() method to calculate the area
# specific to each shape:

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

# Creating instances of subclasses
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Calling the overridden method
print("Area of Rectangle:", rectangle.area())   # Output: Area of Rectangle: 20
print("Area of Circle:", circle.area())         # Output: Area of Circle: 28.274333882308138
