n=int(input())
l=list(map(int,input().split()))
c=0
z=int(input())
for i in range(n):
    if (l[i]==z) :
        c+=1
print(c)