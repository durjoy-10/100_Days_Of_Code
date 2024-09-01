marks=[12,56,32,98,12,45,1,4]
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("Harry,awesome!")
    index+=1
    
#We can write the same code using enumerate function like this.


marks=[12,56,32,98,12,45,1,4]

for index, mark in enumerate(marks,start=1): #Here index start with 1
    print(mark)
    if(index==3):
        print("Harry,awesome!")
