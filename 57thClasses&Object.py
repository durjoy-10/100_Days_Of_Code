class person:
    name="Durjoy"
    occupation="Software Developer"
    def info(self): #self>>which object jar jonno method call hoy
        print(f"{self.name} is a {self.occupation}")
        

a=person() #Creating obj of person class as a
b=person() #Creating obj of person class as b
c=person() #Creating obj of person class as c
a.name="Abir" #Name change in person class by using obj of person class
a.occupation="Manager"
b.name="Shubham"
b.occupation="Teacher"
a.info() #call info() function(which is in person class) by obj a of person class
b.info()
c.info()