class Employee:
    def __init__(self,name):
        self.name=name
        
    def show(self):
        print(f"The name is {self.name}")
        
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"The Dance is {self.dance}")
        
class DancerEmployee(Employee,Dancer): #Multiple inheritance
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
        
o=DancerEmployee("Kartik","Shivani")
print(o.name)
print(o.dance)
o.show() #Here print show method >>The name is Shivani<< in Employee class because DanceEmployee class first inherit Employee class.
