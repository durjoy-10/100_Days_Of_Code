#MAP
def cube(x):
    return x*x*x

# print(cube(2))

l=[1,2,3,4,5,6,7]
# newl=[]
# for item in l:
#     newl.append(cube(item))
newl=map(cube,l) # Here we use map to execute a particular function to a list for all element.
#newl=map(particular function,list)
print(newl) #Here it prints map object 
newl2=list(newl)
#Here then map convert to the list again using list().
print(newl2) 

newl=list(map(lambda x:x*x*x,l))
print(newl)



#Filter
def filter_function(a):
    return a>2
newnewl = list(filter(filter_function,l)) #Here filter function(particular function,list) check 
#Here filter function converted into list.
print(newnewl)           #which value from list the particular value is true and this values add in the newnewl

# Here we can also use lambda function to simplify the code
newnewl=list(filter(lambda x: x>2,l))
print(newnewl)


#Reduce
from functools import reduce #Here if a want to use reduce function we have to import this.
numbers=[1,2,3,4,5,6,7,8,9]
#Here calculating the sum of the numbers using the reduce function
sum=reduce(lambda x,y: x+y,numbers)
print(sum)