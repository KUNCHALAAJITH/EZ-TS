
n=int(input("Enter row Size of the matrix:"))
m=int(input("Enter col size of the matrix:"))
matrix=[]
print("Enter the Martix below:")
for i in range(n):
    matrix.append(list(map(int,input().split())))
print(matrix)
temp=0
for i in range(0,n):
    for j in range(i,m):
        temp=matrix[i][j]
        matrix[i][j]=matrix[j][i]
        matrix[j][i]=temp
print(matrix)
for i in matrix:
    i.reverse()
print(matrix)
