#super keyword
#--------------
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        #by using super keyword I can call constructor of parent class
        self.lang=lang
        
abir=Employee("Abir",233)
durjoy=Programmer("Durjoy",243,"Python")
print(durjoy.name)
print(durjoy.id)
print(durjoy.lang,"\n\n\n\n\n")
#------------------

class ParentClass:
    def parent_method(self):
        print("This is the parent method")
    
    def parent_method2(self):
        print("This is the parent method2")
class ChildClass(ParentClass):
    def parent_method(self):
        print("Durjoy")
        super().parent_method() #calling parent clsss method by super keyword
    def child_method(self):
        print("This is the child method")
        super().parent_method2() #calling parent clsss method by super keyword
        
child_obj=ChildClass()
child_obj.child_method()
child_obj.parent_method()