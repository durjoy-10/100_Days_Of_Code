def fun():
    try:
        l=[1,5,6,7]
        i=int(input("Enter The index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed.")
    print("It is not executed.")
        
x=fun()
print(x)

#Generally we use finally inside the function.If we use try ,except block inside the loop and
#return any value at the end then the code after the block is not executed as execute if it is not a function.
#Thats why we use finally block.It always executed .