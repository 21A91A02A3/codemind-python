t=int(input())
for i in range(1,t+1):
    n=int(input())
    p=1
    for i in range(n,1,-1):
        p=p*i
    i=i-1
    print(p)