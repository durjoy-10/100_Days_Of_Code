#ReadLine Methods

f=open('myfile3.txt','r')
i=0
while True:
    i=i+1
    line =f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in English is: {m2}")
    print(f"Marks of student {i} in CIT is: {m3}")
    print(line)
    
    
#WriteLine Methods

f=open('myfile4.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()

#or I can use it for multiple lines

f=open('myfile5.txt','w')
lines=['line 1','line 2','line 3']
for line in lines:
    f.write(line+'\n')
f.close() #For good practice we should close the file