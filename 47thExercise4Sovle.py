# Write a python program to translate a massage into secret code language. Use  the rules below to translate normal
# English into secret code language

# coding:
# if the word atleast 3 characters, remove the first and append it at the end 
# else:# now append three random characters at the starting at the end

#     simply reverse the String 
    
# Decoding:
# if the word contains less than 3 characters,reverse it
# else:
#     remove 3 characters from start and end. Now remove the last letter and append it to the beginning
    
# your program shoould ask whether you want to code or decode
import string
import random
st=input("Give a message:")
words=st.split(" ")
coding =input("Enter 1 for Coding or 0 for Decoding: ")
coding=True if (coding=="1") else False
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            # r1="xyz"
            # r2="abc"
            stnew=''.join(random.choices(string.ascii_lowercase, k=3))+word[1:]+word[0]+''.join(random.choices(string.ascii_lowercase, k=3))
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
    
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
