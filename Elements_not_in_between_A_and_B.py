n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
r=[]
for i in l:
    if i<a or i>b:
        r.append(i)
if len(r):
        print(*r)
else:
    print(-1)