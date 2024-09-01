# PROTECTED
class Student:
    def __init__(self):
        self._name="Durjoy"
        
    def _funName(self): #protected method
        return "CodeWithHarry"
    
class Subject(Student):
    pass

obj=Student()
obj1=Subject()

#calling by object of Student class
print(obj._name)
print(obj._funName())
#calling by object of Subject class
print(obj1._name)
print(obj1._funName())


#PRIVATE
class Employee:
    def __init__(self):
        self.__name="Durjoy" #private atribute>>Name mangling
        self._id=2102017
        
a=Employee()
# print(a.__name)  Can't be accessed directly
print(a._Employee__name)  #Can be accessed indirectly
print(a._id)
