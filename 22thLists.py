marks=[3,5,6,"Durjoy",True,4,33,32,54,65,123,12,34,15,24,100] #Syntex of list
#Index:0,1,2,3,      ,4   ,5,6 ,7 ,8.........................
print(marks) #Here prints all the list
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #print index no=(length of list-3)

if 6 in marks:
    print("Yes")
else:
    print("NO")
    
#Same thing applies for strings as well!
    
if "Du" in "Durjoy":
    print("Yes.")
    
print(marks[:])  #Default marks[0:len(marks)]
print(marks[1:9]) #prints index 1 to before 9(index 8)
print(marks[1:9:3]) #prints index 1 to before 9(index 8)..here increment is 3.

list=[i*i for i in range(10)]
print(list)
list=[i*i for i in range(10) if i%2==0]
print(list)