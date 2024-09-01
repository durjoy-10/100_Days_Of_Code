#Factorical by recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
    
print("Enter The value of n:")
num=int(input())

print("Value of factorial",num,"is:",factorial(num))
