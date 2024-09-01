l=[1,2,3,4,5,6,1,3,4,1,4,5,1,3,4,5,1]
print(l,"\n")

l.append(7)
print(l,"\n")

l.sort()
print(l,"\n")

l.sort(reverse=True)
print(l,"\n")

l.reverse()
print(l,"\n")

print(l.index(5),"\n")

print(l.count(1),"\n")

m=l.copy()
m[0]=0
print(m)


