class MyClass:
    def __init__(self, value):
        self._value=value
        
    def show(self):
        print(f"Value is {self._value}")
        
    @property #getted method
    def ten_value(self):
        return 10* self._value
    @ten_value.setter #setter method
    def ten_value(self, new_value):
        self._value=new_value/10
        
obj = MyClass(10)
obj.ten_value = 67 #set ten_value as 67 to change self._value
print(obj.ten_value) #get value to getter
obj.show() #By the operation the value changes 10 to 6.7 