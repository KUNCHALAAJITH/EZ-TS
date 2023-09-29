l=list(map(int,input().split(" ")))
l.sort()
p=[k for k in l if k>=0]
#print(p)
s=[]
for i in range(len(p)):
    if p[i]+1 and p[i]-1 not in p:
        s.append(p[i]+1)
        if p[i]-1 >=0:
            s.append(p[i]-1)
print(min(s))
        
    
    
