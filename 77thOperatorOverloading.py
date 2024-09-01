# Operator overloading in Python refers to the ability to redefine the behavior of
# built-in operators for custom classes. This allows objects of a class to respond 
# to operators such as +, -, *, /, ==, <, >, etc., in a way that makes sense for that
# class. This feature provides flexibility and enhances the readability and expressiveness
# of code. Here's an example to illustrate operator overloading in Python:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator '+'
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overloading the subtraction operator '-'
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Overloading the equality operator '=='
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloading the string representation operator '__str__'
    def __str__(self):
        return f'({self.x}, {self.y})'

# Create two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Using overloaded addition operator '+'
p3 = p1 + p2
print("Addition of p1 and p2:", p3)  # Output: Addition of p1 and p2: (4, 6)

# Using overloaded subtraction operator '-'
p4 = p2 - p1
print("Subtraction of p2 and p1:", p4)  # Output: Subtraction of p2 and p1: (2, 2)

# Using overloaded equality operator '=='
print("Are p1 and p2 equal?", p1 == p2)  # Output: Are p1 and p2 equal? False
print("Are p1 and p1 equal?", p1 == p1)  # Output: Are p1 and p1 equal? True

#_______________________________________________________________________________________________


class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j +{self.k}k"
    
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
v1=Vector(3,5,6)
print(v1)

v2=Vector(1,2,9)
print(v2)

print(v1+v2)
print(type(v1+v2))
    