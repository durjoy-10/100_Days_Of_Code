def AreaOfTriangle(a,b):  # making a function by def keyword which parameter's are a and b....
 area=0.5*a*b;
 print("Length: ",a," Width: ",b," Area of Triangle: ",area)
 
def AreaOfRectangle(a,b): # making a function by def keyword which parameter's are a and b....
 area=a*b;
 print("Length: ",a," Width: ",b," Area of Rectangle: ",area)
 
def AreaOfSquare():
    pass # if we create a function and if we use pass in it's body then the code is execute and the function is passed 
         #Otherwise it shows a error..We should have a body of a function if we don't use pass keyword. 
 
x=int(input("Value of Length:")) #Enter the value of length by keyboard
y=int(input("Value of width:"))  #Enter the value of width by keyboard
AreaOfRectangle(x,y) #calling AreaOfRectangle function which parameter x=a,y=b
AreaOfTriangle(x,y)  #calling AreaOfTriangle function which parameter x=a,y=b