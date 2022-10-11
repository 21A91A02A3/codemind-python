m,n=map(int,input().split())
k=""
l=""
m=str(m)
for i in range(0,n):
    k+=m[i]
i=0
n=len(m)-n
for i in range(len(m)-1,n-1,-1):
    l+=m[i]
    ##print(i)
l=l[::-1]
##print(k,l)
o=abs(int(k)-int(l))
print(o)