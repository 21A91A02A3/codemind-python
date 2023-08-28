n,k=map(int,input().split())
l=list(map(str,input().split()))
a=[]
for i in l:
    le=0
    for c in i:
        if c!='-':
            le+=1
    a.append(le)
print(a.count(k))