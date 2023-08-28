n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
for i in a:
    while i!=0:
        r=i%10
        c+=1
        i//=10
    l.append(c)
    c=0
print(l.count(min(l)))