x=10 # global variable

def my_function():
    y=6 #local variable
    print(y)
my_function()
print(x)
#print(y) #his will cause an error because y is a locl variable and is not accessible outside of the function



x=10 # global variable

def my_fun():
    global x
    x=5 #This will change the value of the global variable x
    y=6 #local variable
    print(y)
my_fun()
print(x) #prints 5
#print(y) #his will cause an error because y is a locl variable and is not accessible outside of the function

