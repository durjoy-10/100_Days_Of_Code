s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))  #union methods determine the union between two sets
print(s1,s2) #{1,2,5,6} {3,6,7}
s1.update(s2) #>>>{1,2,3,5,6,7}
print(s1,s2) #{1,2,3,5,6,7} {3,6,7}


cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.intersection(cities2)  ##intersection means common value between two sets.
print(cities3) #>>>>{'Tokyo','Madrid'}
print(cities1)#>>>>>{'Tokyo','Madrid','Berlin','Delhi'} ...Cities1 value is not changed
cities1.intersection_update(cities2) #>>Now cities1 value update as intersection between cities1 and cities2.
print(cities2) #>>>>{'Tokyo','Madrid'}


cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.symmetric_difference(cities2)  ##Symmetric difference removes the common value between two sets.
print(cities3) #>>>>{'Berlin','Delhi','Seoul','Kabul'}

cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.difference(cities2)  ##difference means (cities1-cities2)
print(cities3) #>>>>{'Delhi','Berlin'}


cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities1.isdisjoint(cities2)) #>>>If cities1 disjoint cities2 then it print true otherwise false.
#Disjoint set means there are no common element between two sets.


cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid"}
print(cities1.issuperset(cities2)) #If cities1 superset of cities2 then it print true otherwise false.

cities1={"Tokyo","Madrid"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities1.issubset(cities2)) #If cities1 subset of cities2 then it print true otherwise false.

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.add("Helsinki") ##add methods add element in set.
print(cities)

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Madrid") ##remove methods remove element from the set.
print(cities)

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.discard("Berlin") ##discard methods also remove element from the set.
print(cities)
##Difference between remove and discard method is:
#if There is no item which i want do delete by remove item then it shows an error.But discard methods don't show any error.

cities={"Tokyo","Madrid","Berlin","Delhi"}
item=cities.pop() #There any value from set is poped.There is no fixed item to poped
print(cities)
print(item)

cities={"Tokyo","Madrid","Berlin","Delhi"}
del cities #If we want to delete the whole set then we use del keyword.
# print(cities)


cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.clear() #If we want to clear all the items from the set then we use clear() method.
print(cities)

info={"Durjoy",17,False,5.9}
if "Durjoy" in info:
    print("Durjoy is present.")
else:
    print("Durjoy is absent.")

