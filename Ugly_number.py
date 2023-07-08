a=int(input())
f=0
for i in range(a):
    for j in range(a):
        for k in range(a):
            if (a==(2**i)*(3**j)*(5**k)):
                f=1
if(f==1):
    print("Ugly Number")
else:
     print("Not Ugly Number")