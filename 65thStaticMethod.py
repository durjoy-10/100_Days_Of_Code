class Math:
    def __init__(self,num): #Constructor
        self.num=num
        
    def addtonum(self,n):
        self.num=self.num+n
        
    @staticmethod
    def add(a,b): #Here add( ) is a static method.In add method,There is no need to give self argument.
        return a+b
    
a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
result = Math.add(1,2)
print(result)
res=a.add(2,5)
print(res)