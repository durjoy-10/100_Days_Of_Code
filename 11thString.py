name="Durjoy"
friend='Abir'

print("hey",friend,"\n")

#print("He said ,"i want to eat an apple") # it shows an error
 
#because we can't use double quatation if a use double quatation for string..
#for that we can use single quatation.

print('He said ,"i want to eat an apple"\n') # now there is no error

#if we want to use many lines as string we can use '''....''' or """....""" for multiple line string
MuLine='''He said,
hi Durjoy
hey I am good
"I want to eat an apple"
'''
print(MuLine,"\n")

print(name[0]) #D
print(name[1]) #u
print(name[2]) #r
print(name[3]) #j
print(name[4]) #o
print(name[5]) #y
# print(name[6]) it shows a error

print("\nLets try a for loop\n")
for character in name:
    print(character)
