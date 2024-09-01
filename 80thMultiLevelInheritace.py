
# Multi-level inheritance in Python refers to a situation where a subclass inherits
# from another subclass, creating a hierarchical chain of inheritance. Here's an
# example to illustrate multi-level inheritance:
# Grandparent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Parent class inheriting from Person
class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def work(self):
        return f"{self.name} is working."

# Child class inheriting from Employee
class Manager(Employee):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age, emp_id)
        self.department = department

    def supervise(self):
        return f"{self.name} is supervising the {self.department} department."

# Creating an instance of the grandchild class
manager = Manager("Alice", 35, "M123", "Sales")

# Accessing methods and attributes
print(manager.greet())        # Output: "Hello, my name is Alice and I am 35 years old."
print(manager.work())         # Output: "Alice is working."
print(manager.supervise())    # Output: "Alice is supervising the Sales department."
