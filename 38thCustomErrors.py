a=int(input("Enter any value between 5 and 9:"))

if(a<5 or a>9): # If what i need that is not get then sometimes i need an error to stop the program.
    raise ValueError("Value should be between 5 and 9") #Thats why we can use raise keyword to create an error.

print(f"You enter the value between 5 and 9.The value is {a}")

x=input("Enter quit to Show the program:")

if(x!="quit"):
    raise NameError("You have to enter {{quit}}")

print(f"Great!You enter {x}")