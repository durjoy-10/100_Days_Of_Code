class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    @classmethod  
    def fromStr(cls,string): #Here fromStr method use as constructor.It return name and salary from string=(John-50000)
                             #separated by splict("-") function
        return cls(string.split("-")[0],int(string.split("-")[1]))
                  #name=john            ,salary=50000
e1=Employee("Harry",12000)
print(e1.name)
print(e1.salary)

string = "john-50000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)