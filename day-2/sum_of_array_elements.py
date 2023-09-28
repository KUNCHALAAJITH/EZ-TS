'''def s_a(x):
    sum=0
    for i in X:
        sum=sum+i
    print(sum)

X=list(map(int,input().split(" ")))
y=s_a(X)'''
def l_s(x):
    c=0
    n=int(input("enter the search element"))
    for i in range(len(X)):
        if i==n:
            return True
    return c
    

X=list(map(int,input().split(" ")))
print(l_s(X))

