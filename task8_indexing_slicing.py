# 51	Access the first element of an array.
import numpy as np
arr51 = np.array([1, 2, 3, 4, 5])
first_element = arr51[0]
print("First element:", first_element)

# 52	Access the last element of an array.
last_element = arr51[-1]
print("Last element:", last_element)

# 53	Extract first 5 elements from an array.
first_five = arr51[:5]
print("First 5 elements:", first_five)

# 54	Extract last 5 elements from an array.
last_five = arr51[-5:]
print("Last 5 elements:", last_five)

# 55	Slice every alternate element.
alternate_elements = arr51[::2]
print("Alternate elements:", alternate_elements)

# 56	Reverse an array using slicing.
reversed_array = arr51[::-1]
print("Reversed array:", reversed_array)

# 57	Access a specific row in a matrix.
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_1 = matrix[1]
print("Second row:", row_1)

# 58	Access a specific column in a matrix.
column_1 = matrix[:, 1]
print("Second column:", column_1)

# 59	Extract a submatrix from a 5×5 matrix.
submatrix = matrix[1:3, 1:3]
print("Submatrix:", submatrix)

# 60	Replace the third element with value 100.
arr60 = np.array([1, 2, 3, 4, 5])
arr60[2] = 100
print("Array with third element replaced:", arr60)

# 61	Replace all even numbers with -1.
arr61 = np.array([1, 2, 3, 4, 5])
arr61[arr61 % 2 == 0] = -1
print("Array with even numbers replaced:", arr61)

# 62	Find all elements greater than 50.
arr62 = np.array([10, 60, 30, 80, 20])
greater_than_50 = arr62[arr62 > 50]
print("Elements greater than 50:", greater_than_50)

# 63	Find indices of elements greater than 50.
indices = np.where(arr62 > 50)
print("Indices of elements greater than 50:", indices)

# 64	Select elements divisible by 3.
arr64 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
divisible_by_3 = arr64[arr64 % 3 == 0]
print("Elements divisible by 3:", divisible_by_3)

# 65	Extract diagonal elements from a matrix.
diagonal_elements = np.diag(matrix)
print("Diagonal elements:", diagonal_elements)
