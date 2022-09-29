x,y=map(int,input().split())
res=0
res=(x-2*y)
if x==0 and y%2==0:
    print('YES')
elif x==0 and y%2!=0:
    print('NO')
elif res%2==0:
    print('YES')
else:
    print('NO')