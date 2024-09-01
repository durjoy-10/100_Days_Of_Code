#tuple vaule can be change inderectly in this way

countries=("Spain","Italy","India","England","Germany")
temp = list(countries) #converting tuple to list
temp.append("Russia") #add "Russia" at the end of the creating list.
temp.pop(3)  #remove Index 3
countries=tuple(temp) #converting List to tuple and changed the tuple item.
print("\n",countries,"\n")

#We can concatinate two tuple.
countries1=("Pakistan","Afganistan","Bangladesh")
countries2=("Vietnam","India","China")
southEastAsia=countries1+countries2 #concatinate countries1 and countries2 and make a new tuple.
print(southEastAsia,"\n")

#some methods in tuple
tuple1=(0,1,2,3,32,12,12,1,3,4,5,3,2,4,2,3)
res=tuple1.count(3)  #count of 3 in tuple is
print("count of 3 in tuple is:",res)

res1=tuple1.index(3) 
print(res1) # print index 3

res2=tuple1.index(3,4,10) 
print(res2) #print the index number where the 3 is in index 4 to index 9
