# a=[]
# n=int(input("enter a number"))
# r1=int(input("enter starting range"))
# r2=int(input("enter end range"))
# for i in range(n):
#     x=int(input())
#     if x>=r1 and x<=r2:
#         a.append(x)
#     else:
#         print("num not accepted")
# print(a)
# even=[x for x in a if x%2==0]
# print(even)
# po=[]
# for i in a:
#     for j in range(0,max(a)):
#         if 2**j==i:
#             po.append(i)
# print("powers of 2 are:",po)
# po1=[p for p in po if p in a]
# print(po1)
"""Create an array (1d), it should contain number b/w 10 to 30, in this array extract and print
I)	Even numbers
II)	power values"""
#using bitwise 
r=list(map(int,input("enter range:").split(" ")))
n=int(input("enter the number of elements:"))
li=[]
eli=[]
pli=[]
i=0
while(i<n):
    num=int(input())
    if num>=r[0] and num<=r[1]:
        li.append(num)
        i+=1
    else:
        print("invalid")
        continue 
for i in li:
    if i % 2==0:
        eli.append(i)
    if (i & (i-1))==0:
        pli.append(i)
print("even no's:",eli,"\n2 power values:",pli)

# using list comprehension method
"""
r=list(map(int,input("enter range:").split(" ")))
n=int(input("enter the number of elements:"))
li=[]
eli=[]
pli=[]
i=0
while(i<n):
    num=int(input())
    if num>=r[0] and num<=r[1]:
        li.append(num)
        i+=1
    else:
        print("invalid")
        continue 
tp=[(2**i) for i in range(r[1])]
for i in li:
    if i % 2==0:
        eli.append(i)
    if i in tp:
        pli.append(i)
print("even no's:",eli,"\n2 power values:",pli)
""" 
        
