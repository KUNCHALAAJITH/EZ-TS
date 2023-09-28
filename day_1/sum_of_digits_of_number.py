'''n=input()
z=0
for i in n:
    z=z+int(i)
print(z)'''
n=int(input())
c=0
r=0
while(n>0):
    r=n%10
    c=c+r
    n=n//10
    
print(c)
    
   
