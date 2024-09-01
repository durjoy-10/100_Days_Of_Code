import math  #importing math class thats why i can use all things anoung math class
result = math.sqrt(9)*math.pi #Using sqrt and pi function by importing math class
print(result)

from math import sqrt,pi #from math importing particular function(sqrt,pi) by using from keyword
result = sqrt(9)*pi #Here we don't need to write math.sqrt
print(result)

from math import * #By this way we can import all things from a built in class(math)
result = sqrt(9)*pi
print(result)

import math as m #Here importing math class as m.Now we can use math class write m.function()
result = m.sqrt(9)*m.pi
print(result)

from math import sqrt as s,pi #Here importing particular function(sqrt as s) and pi form math class.Now we can use s for sqrt function
result = s(9)*pi
print(result)

import math
print(dir(math)) #By using dir() function we can see what is in the math class

# def welcome():
#     print("Hey you are welcome my friend")

# Durjoy="A good boy"

from durjoy import welcome,Durjoy #Where durjoy is another python program.We can use its function and other things by this way
welcome()
print(Durjoy)

from durjoy import * #Here importing all things from durjoy
welcome()
print(Durjoy)

import durjoy as ds #Here importing all things from durjoy as ds
ds.welcome()
print(ds.Durjoy)