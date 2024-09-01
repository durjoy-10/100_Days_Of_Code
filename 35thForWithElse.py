for i in range(6):
    print(i)
    # if i==4:
    #     break
    
else: #If the loop is properly runs,then else blocked execute.But if the loop is breaked then the else block is not executed.
    print("Sorry no i") 
    
j=1
while j<7:
    print(j)
    if j==4:
        break
    j=j+1
else: #The else block is not execute.Because I use break statement in the loop and the loop is broken while j==4. 
    print("Sorry no j")