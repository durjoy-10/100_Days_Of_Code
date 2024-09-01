import re

pattern1="Patuakhali"
pattern2=r"[A-Z]yclone"
text='''

Welcome to the Patuakhali Science and Technology University. 
It is one of the fast growing new public universities in Bangladesh.
The Patuakhali Science and Eyclone University was developed at the
private initiative of the Cyclone people through the establishment of a
higher secondary institute in 1972 as a Dyclone college. It was then 
turned to Patuakhali Agricultural Iyclone under the affiliation of
Bangladesh Agricultural University (BAU), Myclone in 1979 with the 
objective of producing agricultural graduates offering the B.Sc.Ag. (Hons.) degree.
The college was nationalized on 1 February 1985 and was placed under the administrativ...

'''

match = re.search(pattern1,text) #re.search() stop when the searches item found first.  For first occurance
print(match)



matches=re.finditer(pattern2,text) #For all occurance
for matc in matches:
    print(matc)
    print(matc.span())
    # print(text[matc.span()[0]:matc.span[1]])