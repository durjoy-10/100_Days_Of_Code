tup=(1,5,6,234,"Green",True) 
print(type(tup),tup)        
print(len(tup))  #determine the length of tuple

print(tup[0])
print(tup[1])
print(tup[2])

# tup=(1,) #if you have one value of tuple then we have to give a comme after value. 
# print(type(tup),tup)

if 234 in tup: #condition is true
    print("Yes 234 is present in this tuple") 
    
if 34 in tup:  #condition is false
    print("Yes 234 is present in this tuple")
    
tup2=tup[1:4] #create a new tupple with 1 index to before 4 index(3)
print(tup2) #print>>>(5,6,234)
    
#syntex of tuple>>> tup=(any data and seperated by comma)
#syntex of tuple>>> List=[any data and seperated by comma]
#value of index can be changed in List. But value of index can't be changed in Tuple. 
