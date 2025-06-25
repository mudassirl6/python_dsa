def matrix_multi(a,b):
    
    if len(a[0]) != len(b):
        raise ValueError("Number of columns in A must match number of rows in B")
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

# Example usage:
if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    print(matrix_multi(A, B))  # Output: [[58, 64], [139, 154]]
    # Output: [[58, 64], [139, 154]]
    C = [[1, 2], [3, 4], [5, 6]]
    print(matrix_multi(A, C))  # Output: [[22, 28], [67, 82]]
      