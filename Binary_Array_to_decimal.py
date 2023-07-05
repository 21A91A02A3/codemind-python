n=int(input())
l=list(map(int,input().split()))
a=0
for i in range(n-1,-1,-1):
    a+=l[i]*pow(2,n-i-1)
print(a)