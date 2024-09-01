#A constructor is a unique function that gets called automatically
#when an object is created of a class.The main purpose of a  constructor is to initialize or assign value of the data members of that class
#It can't return any value other than none
#SYNTAX
#-------
#Parameterize Constructor Example

class Details:
    def __init__(self,animal,group): #creating cons..
        self.animal=animal
        self.group=group

obj=Details("Crab","Crustaceans")
print(obj.animal," belongs to the",obj.group,"group")

#Default Constructor Example

class Detail:
    def __init__(self): #creating cons..
        print("animal crab belongs to Crustaceans group")
obj1=Detail()

#Another Example

class person:
    def __init__(self,n,o): #It automatically called when obj reated.
        print("Hey I am a person")
        self.name=n #Here self.name=n="Durjoy" updated when created obj a of this class
        self.occ=o 
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=person("Durjoy","Developer")
b=person("Abir","Manager")
a.info()
b.info()