dic={
    17:"Durjoy",
    18:"Mim",
    19:"Hridoy",
    20:"Sadman"    
}
print(dic[17])


info={'name':'Durjoy','age':21,'Eligible':True}
print(info) #for print all dictionary
print(info['name']) #for print particular element.If there is no element which I want to access by this way then it shows an error. 
print(info.get('name')) #for print particular element.If there is no element which I want to access by this way then it shows no error.It prints None.
print(info.keys()) #accessing multiple keys
print(info.values()) #accessing multiple values



for key in info.keys():
    # print(info[key]) #We get corresponding value of name,age,Eligible by this way.
    print(f"The value corresponding to the key {key} is {info[key]}") #by use f-string


print(info.items())##It show key and it's corresponding item in pair
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

