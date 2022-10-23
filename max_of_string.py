n=input()
l=[]
for i in range(0,len(n)):
    l.append(ord(n[i]))
print(chr(max(l)))