a=int(input())
b=int(input())
s=0
s1=0
for i in range(1,a):
    if a%i==0:
        s=s+i
for i in range(1,b):
    if b%i==0:
        s1=s1+i
if s1==a and s==b:
    print("Amicable")
else:
    print("Not Amicable")