# 81	Generate a random array and normalize it between 0 and 1.
import numpy as np
random_array = np.random.rand(5)
#formualae for normalization: (x - min) / (max - min)
normalized_array = (random_array - np.min(random_array)) / (np.max(random_array) - np.min(random_array))
print("Normalized array:", normalized_array)


# 82	Create a checkerboard pattern matrix (8×8).
checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print("Checkerboard pattern:")
print(checkerboard)


# 83	Find unique elements in an array.
unique_elements = np.unique(random_array)
print("Unique elements:", unique_elements)



# 84	Count frequency of each unique value.
frequency = np.bincount(unique_elements.astype(int))
print("Frequency of unique values:", frequency)



# 85	Shuffle elements of an array randomly.
np.random.shuffle(random_array)
print("Shuffled array:", random_array)


# 86	Find common elements between two arrays.
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])
common_elements = np.intersect1d(array1, array2)
print("Common elements:", common_elements)


# 87	Remove duplicate values from an array.
unique_array = np.unique(random_array)
print("Array with duplicates removed:", unique_array)


# 88	Find missing numbers in an array from 1-100.
full_array = np.arange(1, 101)
missing_numbers = np.setdiff1d(full_array, random_array)
print("Missing numbers:", missing_numbers)


# 89	Convert a 1D array into a 3D array.
three_d_array = random_array.reshape(5, 1, 1)
print("3D array:", three_d_array)



# 90	Create a border matrix where borders are 1 and inner values are 0.
border_matrix = np.zeros((8, 8), dtype=int)
border_matrix[0, :] = 1
border_matrix[-1, :] = 1
border_matrix[:, 0] = 1
border_matrix[:, -1] = 1
print("Border matrix:")
print(border_matrix)
