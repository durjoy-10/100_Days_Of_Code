#dir() method
#-------------
x=[1,2,3] #Here x is a list
print(dir(x)) #By using dir() method I can know which methods I can apply in this list/tupple and so on


#__dict__ attribute
#-------------------
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
        
p=Person("Durjor",21)
print(p.__dict__) #The __dict__ attribute returns a dictionary representation of an object's attributes.


#help() method
#--------------
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
        
p=Person("Durjor",21)
print(help(Person))
#The help() method is used to get help documentation for
#an object,including a description of its attributes and methods.