# 66	Add two matrices.
import numpy as np
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
sum_matrix = matrix1 + matrix2
print("Sum of matrices:", sum_matrix)

# 67	Subtract two matrices.
diff_matrix = matrix1 - matrix2
print("Difference of matrices:", diff_matrix)

# 68	Multiply two matrices element-wise.
prod_matrix = matrix1 * matrix2
print("Element-wise product of matrices:", prod_matrix)

# 69	Perform matrix multiplication using dot().
dot_matrix = np.dot(matrix1, matrix2)
print("Matrix multiplication result:", dot_matrix)

# 70	Calculate transpose of a matrix.
transpose_matrix = matrix1.T
print("Transpose of matrix1:", transpose_matrix)

# 71	Find determinant of a matrix.
det_matrix = np.linalg.det(matrix1)
print("Determinant of matrix1:", det_matrix)

# 72	Find inverse of a matrix.
inv_matrix = np.linalg.inv(matrix1)
print("Inverse of matrix1:", inv_matrix)

# 73	Find eigenvalues of a matrix.
eigenvalues = np.linalg.eigvals(matrix1)
print("Eigenvalues of matrix1:", eigenvalues)

# 74	Find eigenvectors of a matrix.
eigenvectors = np.linalg.eig(matrix1)[1]
print("Eigenvectors of matrix1:", eigenvectors)

# 75	Compute matrix rank.
rank_matrix = np.linalg.matrix_rank(matrix1)
print("Rank of matrix1:", rank_matrix)

# 76	Create a random 4×4 matrix and find row sums.
matrix4x4 = np.random.rand(4, 4)
row_sums = np.sum(matrix4x4, axis=1)
print("Row sums:", row_sums)

# 77	Find column sums of a matrix.
column_sums = np.sum(matrix4x4, axis=0)
print("Column sums:", column_sums)

# 78	Find row-wise maximum values.
row_max = np.max(matrix4x4, axis=1)
print("Row-wise maximum values:", row_max)

# 79	Find column-wise minimum values.
column_min = np.min(matrix4x4, axis=0)
print("Column-wise minimum values:", column_min)

# 80	Create a 5×5 multiplication table matrix.
multiplication_table = np.outer(np.arange(1, 6), np.arange(1, 6))
print("Multiplication table:")
print(multiplication_table)
