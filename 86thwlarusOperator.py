a= True
print(a:=False)  #prints false


numbers=[1,2,3,4,5]
while (n:=len(numbers))>0:
    print(numbers.pop()) #pop() prints & removes the last item from the list.
    
    
#walrus operator :=

# new to python 3.8
#assignment expression aka walrus operator
#assign values to variables as part of a larger expression

happy = True   #without walrus
print(happy)

print(happy :=True)

foods=list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food) 
#____________________________________

foods = list()  #with walrus
while(food:=input("what food do you like?: ") != "quit"):
    foods.append(food)