a=[]
n=int(input("enter a number"))
r1=int(input("enter starting range"))
r2=int(input("enter end range"))
for i in range(n):
    x=int(input())
    if x>=r1 and x<=r2:
        a.append(x)
    else:
        print("num not accepted")
print(a)
even=[x for x in a if x%2==0]
print(even)
po=[]
for i in a:
    for j in range(0,max(a)):
        if 2**j==i:
            po.append(i)
print("powers of 2 are:",po)
po1=[p for p in po if p in a]
print(po1)
    
        
