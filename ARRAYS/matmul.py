A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2],[4,5],[7,8]]

c = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]


for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(A[0])):
            c[i][j] += A[i][k]*B[k][j] 
            
print(c)

