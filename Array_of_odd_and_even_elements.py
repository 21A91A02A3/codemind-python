n=int(input())
l=list(map(int,input().split()))
k=[]
r=[]
for i in l:
    if i%2==0:
        k.append(i)
    else:
        r.append(i)
print(*r,*k)