# 1	Import the NumPy library and print its version.
import numpy as np
print("NumPy version:", np.__version__)

# 2	Create a NumPy array containing numbers from 1 to 10.
arr1 = np.arange(1, 11)
print("Array from 1 to 10:", arr1)

# 3	Create an array of all zeros with size 10.
arr2 = np.zeros(10)
print("Array of zeros:", arr2)

# 4	Create an array of all ones with shape (3,3).
arr3 = np.ones((3, 3))
print("Array of ones:", arr3)

# 5	Create an identity matrix of size 5×5.
arr4 = np.identity(5)
print("Identity matrix:", arr4)

# 6	Create an array of even numbers from 2 to 50.
arr6 = np.arange(2, 51, 2)
print("Array of even numbers:", arr6)

# 7	Create an array of odd numbers from 1 to 99.
arr7 = np.arange(1, 100, 2)
print("Array of odd numbers:", arr7)

# 8	Generate numbers from 10 to 100 with step size 5.
arr8 = np.arange(10, 101, 5)
print("Array with step size 5:", arr8)

# 9	Create a NumPy array from a Python list.
list1 = [1, 2, 3, 4, 5]
arr9 = np.array(list1)
print("Array from list:", arr9)

# 10	Create a NumPy array from a tuple.
tuple1 = (6, 7, 8, 9, 10)
arr10 = np.array(tuple1)
print("Array from tuple:", arr10)

# 11	Find the shape of an array.
print("Shape of arr1:", arr1.shape)

# 12	Find the dimensions of an array.
print("Dimensions of arr1:", arr1.ndim)

# 13	Find the datatype of array elements.
print("Datatype of arr1:", arr1.dtype)

# 14	Create a random array of size 10.
arr14 = np.random.random(10)
print("Random array:", arr14)

# 15	Generate 10 random integers between 1 and 100.
arr15 = np.random.randint(1, 101, size=10)
print("Random integers between 1 and 100:", arr15)

# 16	Reshape an array of size 12 into (3,4).
arr16 = np.arange(12).reshape(3, 4)
print("Reshaped array (3,4):", arr16)

# 17	Flatten a 3×3 matrix into a 1D array.
arr17 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flattened_arr = arr17.flatten()
print("Flattened array:", flattened_arr)

# 18	Create a 4×4 matrix filled with value 7.
arr18 = np.full((4, 4), 7)
print("4×4 matrix filled with 7:", arr18)

# 19	Find the size (number of elements) of an array.
print("Size of arr1:", arr1.size)

# 20	Create a diagonal matrix with diagonal values [1,2,3,4].
arr20 = np.diag([1, 2, 3, 4])
print("Diagonal matrix:", arr20)

# 21	Convert a float array into an integer array.
arr21 = np.array([1.5, 2.7, 3.9])
int_arr = arr21.astype(int)
print("Integer array:", int_arr)

# 22	Create an array with values between 0 and 1 using linspace().
arr22 = np.linspace(0, 1, num=10)
print("Array with values between 0 and 1:", arr22)

# 23	Reverse an array.
arr23 = np.array([1, 2, 3, 4, 5])
reversed_arr = arr23[::-1]
print("Reversed array:", reversed_arr)

# 24	Sort an array in ascending order.
arr24 = np.array([5, 2, 9, 1, 5, 6])
sorted_arr = np.sort(arr24)
print("Sorted array:", sorted_arr)

# 25	Find the maximum and minimum values in an array.
print("Maximum value in arr24:", np.max(arr24))
print("Minimum value in arr24:", np.min(arr24))

# 26	Find the index of maximum value.
print("Index of maximum value:", np.argmax(arr24))

# 27	Find the index of minimum value.
print("Index of minimum value:", np.argmin(arr24))

# 28	Create a 2×3 matrix and print its transpose.
arr28 = np.array([[1, 2, 3], [4, 5, 6]])
print("Original matrix:")
print(arr28)
print("Transposed matrix:")
print(arr28.T)

# 29	Concatenate two arrays.
arr29a = np.array([1, 2, 3])
arr29b = np.array([4, 5, 6])
concatenated_arr = np.concatenate([arr29a, arr29b])
print("Concatenated array:", concatenated_arr)

# 30	Split an array into 3 equal parts.
arr30 = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr30, 3)
print("Split array:", split_arr)