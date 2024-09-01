# __init__(self, ...): Constructor method
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(3, 4)
print(point.x, point.y)  # Output: 3 4


# __len__(self): Length method.
class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

my_list = MyList([1, 2, 3, 4, 5])
my_list2="Durjoy"
print(len(my_list))  # Output: 5
print(len(my_list2))  # Output: 6


# __str__(self): String representation method.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}+{self.y})"

point = Point(3, 4)
print(str(point))  # Output: (3+4) 

# __repr__(self): Object representation method.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

point = Point(3, 4)
print(repr(point))  # Output: Point(3, 4)

# __call__(self, ...): Call method.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return self.factor * x

multiply_by_2 = Multiplier(2)
print(multiply_by_2(5))  # Output: 10


# __getitem__(self, key): Indexing method.
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])  # Output: 3

# __eq__(self, other): Equality method.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point1 = Point(3, 4)
point2 = Point(3, 4)
print(point1 == point2)  # Output: True

