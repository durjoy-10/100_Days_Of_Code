name = "Durjoy"
for i in name:
    print(i)
    if(i=="y"):
        print("End.")
        
colors = ["Red","Green","Blue","Yellow"]
for color in colors:
    print(color) #it prints Red,Blue...colors seperately
    for i in color:
        print(i) # it prints all char of the colors name seperately
        
        
for k in range(5): #it prints 0 to 4
    print(k)
    
for k in range(1,100): # it prints 1 to 99
    print(k)
    
for k in range(1,10,2): 
    print(k) # 1 3 5 7 9
    
# here range(start,stop,step/incrementation) 
#here start arguments means where the loop started,
#here stop arguments means where the loop stopped,
#here step arguments means the incrementation or decrementation of start agruments.
