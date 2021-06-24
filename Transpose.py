# 39. Program to transpose a matrix.
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
B=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        B[j][i]=A[i][j]
for i in B:
    print(i)