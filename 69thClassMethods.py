class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company name is {self.company}")
        
    def changeOneTimeCompany(cls,newCompany):
        cls.company=newCompany
        
    @classmethod  
    def changeCompany(cls,newCompany):
        cls.company=newCompany
        
e1=Employee()
e1.name="Harry"
e1.show()
e1.changeOneTimeCompany("Tesla") #Here class variable in not changed
e1.show()
print(Employee.company) #Apple
e1.changeCompany("Durjoy LTD") #Here class variable in changed by using classmethod decorator in changeCompany method
e1.show()
print(Employee.company) #Durjoy LTD