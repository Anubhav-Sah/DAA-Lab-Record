def matrix_multiplication(matrix1, matrix2, row1, row2, col1, col2):
    if col1 != row2:
        return -1  
    
    multiplication_matrix = [[0 for _ in range(col2)] for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                multiplication_matrix[i][j] += matrix1[i][k] * matrix2[k][j] 
    return multiplication_matrix

matrix1 = [[1, 2],
           [3, 4]]

matrix2 = [[1, 2],
           [3, 4]]

result = matrix_multiplication(matrix1, matrix2, len(matrix1), len(matrix2), len(matrix1[0]), len(matrix2[0]))

print(result)
