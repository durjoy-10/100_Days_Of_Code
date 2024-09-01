#Dictionary is ordered.But set is not ordered.
ep1={122:45,123:89,568:69,670:69}
ep2={222:67,566:90}
ep1.update(ep2) #ep1 updated with the value of ep2
print(ep1)

ep1={122:45,123:89,568:69,670:69}
ep1.pop(122) #it remove key 122 and its corresponding value.
print(ep1)

ep1={122:45,123:89,568:69,670:69}
ep1.popitem() #it remove last key and its corresponding value.
print(ep1)


del ep1 #it delete the dictonary
# print(ep1) 


ep1={122:45,123:89,568:69,670:69}
del ep1[122] #it deletes the key 122 and its corresponding value.
print(ep1)


ep1.clear() #empty dictionary.It clear all the element form the dictonary.
print(ep1)

