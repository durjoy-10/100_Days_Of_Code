a=[1,2,34]
b=[1,2,34]

print(a is b) #False>>exact location of object in memory
print(a==b) #true>>comparision value


a=2
b=2
print(a is b) #True>>exact location of object in memory
print(a==b) #true>>comparision value

a=(1,2,3) #Tuple immutable
b=(1,2,3)
print(a is b) #True>>exact location of object in memory
print(a==b) #true>>comparision value

a="Durjoy" #String immutable
b="Durjoy" 
print(a is b) #True>>exact location of object in memory
print(a==b) #true>>comparision value

a=None
b=None
print(a is b) #True>>exact location of object in memory
print(a is None) #True
print(a==b) #true>>comparision value
