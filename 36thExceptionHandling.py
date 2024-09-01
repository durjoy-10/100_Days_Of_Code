a=int(input("Enter the Number:")) 
#Here if I enter anything except number then it shows an error.That's why I should use try except to handle this error.
print(f"Multipplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")

except:
    print("Invalid input!")
#If i don't use try except block then if it shows an error then the code after it is not executed.
print("Some imp lines of code")
print("End of program.")