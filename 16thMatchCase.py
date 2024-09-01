x=int(input("Enter a number:"))

match x: #match is use as swith
    case 0:
        print("x is zero") #There is not use any break statement.if a case block matched then another block can't work.
    case 4:
        print("X is four")
    # case _ if x!=90:
    #     print("x is not 90")
    # case _ if x!=80:
    #     print("X is not 80")
    case _: # case _ use as default.
        print(x)
    