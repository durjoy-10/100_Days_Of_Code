def welcome():
    print("Hey you are welcome my friend")
    
print(__name__) #__name__ it means where it printed
if(__name__=="__main__"): #if I run harry.py then __name__=__main__ because it runs from harry.py.Then the if block executed
    welcome()             #If I import harry to another file then __name__==__harry.Then this block is not executed