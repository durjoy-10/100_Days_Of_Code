# def double(x):
#     return x*2  #we can use lambda function to simplyfy the function like this
double =lambda x: x*2

# def cube(x):
#     return x*x*x
cube = lambda x: x*x*x

# def average(x,y,z):
#     return((x+y+z)/3)
average=lambda x,y,z:(x+y+z)/3


def apply(fx,value):
    return 6+fx(value)

print(double(5))
print(cube(5))
print(average(3,5,7))
print(apply(lambda x: x*x,2))