#Python decorators are a powerful and versatile tool that
#allow you to modify the behaivour of function or methods.
#They are a way to extend the functionality of a function
# or method without modifying its source code

#A decorator is a function that takes another function as an aegument and returns a new function that
#modifies the behaivour of the orginal function.The new function is often reffered to as "decorated" 
#function.

def greet(fx):
    def mfx(*args, **kwargs): #If args have in the function then We have to add this (*args(args as tuple),**kwargs(as dict))
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World!!!")
    
   
def add(a,b):
    print(a+b)

#greet(hello)()    
hello()

greet(add)(10,110)
# add(1,2)