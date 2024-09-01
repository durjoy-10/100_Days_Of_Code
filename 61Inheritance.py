class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")
        
        
class Programmer(Employee): #Here Programmer class inherits Employee class
    def showlanguage(self):
        print("The default language is Python")
        
e1=Employee("Durjoy",2102017)
e1.showDetails()
# e1.showlanguage It shows an error
e2=Programmer("Mim",2102018)
e2.showDetails() #Here Programmer class inherits Employee class so that I can use Employee class by creating a obj of programmer class.
e2.showlanguage()