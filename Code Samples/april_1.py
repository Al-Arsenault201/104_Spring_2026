s = "UMBC"
print(id(s))
s = "UMB"
print(id(s))
l = [1,2,3,4,5]
print(id(l))
for i in range(0,len(l)):
    l[i] += 1
print(l)
print(id(l))

