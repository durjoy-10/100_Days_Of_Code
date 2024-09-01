#SEEK,TELL AND TRUNCATE FUNCTION
#---------------

with open('myfile6.txt','r') as f:
    
    f.seek(10) #move to the 10th byte in the file
    
    data=f.read(6)#read the next 6 bytes
    
    print(f.tell())#tell() function returns the current positon within the file,in bytes 
    
    print(data)
    
    
with open('myfile7.txt','w') as f:
    f.write('Hello World')
    f.truncate(5) #Here truncate function add first 5 character
with open('myfile7.txt','r') as f:
    print(f.read()) #prints >> Hello

    
