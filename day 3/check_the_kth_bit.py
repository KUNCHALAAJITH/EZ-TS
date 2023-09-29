n=int(input())
'''k=int(input("enter kth bit"))
if(n&(1<<k-1))==0:
    print("it is not set bit")
else:
    print("it is set bit")'''

xor=0
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)
