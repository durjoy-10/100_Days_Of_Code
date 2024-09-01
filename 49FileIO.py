# WRITING A FILE
f=open('myfile.txt','w') #To open file use open() file.Here 'w' is modes>>write.
#         If we write 'w' then I can olny write the text not read or append
f.write("Hey Durjoy.") #This mode used in the file for writtings olny and creats a new file if the file does not exist.
f.close() #It must be added

f=open('myfile2.txt','w') #To open file use open() file.Here 'w' is modes>>write.
#         If we write 'w' then I can olny write the text not read or append
f.write("How are you?") #This mode used in the file for writtings olny and creats a new file if the file does not exist.
f.close() #It must be added

# # AEADING A FILE
f=open('myfile.txt','r') #To open file use open() file.Here 'r' is modes>>read.It also set as default.
#         If we write 'r' then I can olny read the text not write or append
text=f.read() #to read the file 
print(text)
f.close()

f=open('myfile2.txt','rb') #To open file use open() txt file as binary form.('rb),>>jpg,image,pdfexe
#        If we write 'r' then I can olny read the text not write or append
text=f.read() #to read the file 
print(text)
f.close()

#APPENDING A FILE
f=open('myfile.txt','a') #To open file use open() file.Here 'a' is modes>>append.
#           If we write 'a' then I can olny append the text not read or write
f.write(" Heyyyyyyy!!!! ") #This mode used in the file for appends olny.It added in the txt file in the last what i write in this f.write() function
f.close()#It must be added

#ALSO APPENDING WITHOUT USING f.close AT LAST IN THE CODE
with open('myfile2.txt','a') as f:
    f.write("Hey i'm inside with")
