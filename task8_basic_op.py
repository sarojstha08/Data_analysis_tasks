# 31	Add two arrays element-wise.
import numpy as np
arr31a = np.array([1, 2, 3])
arr31b = np.array([4, 5, 6])
sum_arr = arr31a + arr31b
print("Sum of arrays:", sum_arr)

# 32	Subtract two arrays element-wise.
sub_arr = arr31a - arr31b
print("Difference of arrays:", sub_arr)

# 33	Multiply two arrays element-wise.
mul_arr = arr31a * arr31b
print("Product of arrays:", mul_arr)

# 34	Divide two arrays element-wise.
div_arr = arr31a / arr31b
print("Division of arrays:", div_arr)

# 35	Find square of every element in an array.
arr35 = np.array([1, 2, 3, 4, 5])
square_arr = np.square(arr35)
print("Square of array elements:", square_arr)

# 36	Find cube of every element.
cube_arr = np.power(arr35, 3)
print("Cube of array elements:", cube_arr)

# 37	Calculate square root of array values.
sqrt_arr = np.sqrt(arr35)
print("Square root of array elements:", sqrt_arr)

# 38	Find exponential values of array elements.
exp_arr = np.exp(arr35)
print("Exponential values of array elements:", exp_arr)

# 39	Find logarithm of array elements.
log_arr = np.log(arr35)
print("Logarithm of array elements:", log_arr)

# 40	Compute sum of all elements in an array.
sum_arr = np.sum(arr35)
print("Sum of array elements:", sum_arr)

# 41	Compute mean of array values.
mean_arr = np.mean(arr35)
print("Mean of array values:", mean_arr)

# 42	Compute median of array values.
median_arr = np.median(arr35)
print("Median of array values:", median_arr)

# 43	Compute standard deviation.
std_arr = np.std(arr35)
print("Standard deviation of array values:", std_arr)

# 44	Compute variance.
var_arr = np.var(arr35)
print("Variance of array values:", var_arr)

# 45	Find cumulative sum of elements.
cumsum_arr = np.cumsum(arr35)
print("Cumulative sum of array elements:", cumsum_arr)

# 46	Find cumulative product of elements.
cumprod_arr = np.cumprod(arr35)
print("Cumulative product of array elements:", cumprod_arr)

# 47	Find product of all elements in array.
product_arr = np.prod(arr35)
print("Product of array elements:", product_arr)

# 48	Round decimal values to 2 decimal places.
rounded_arr = np.round(arr35, decimals=2)
print("Rounded array elements:", rounded_arr)

# 49	Find absolute values of negative numbers.
arr49 = np.array([-1, -2, -3, 4, 5])
abs_arr = np.abs(arr49)
print("Absolute values:", abs_arr)

# 50	Replace all negative values with zero.
arr50 = np.array([-1, -2, -3, 4, 5])
zero_arr = np.where(arr50 < 0, 0, arr50)
print("Array with negative values replaced by zero:", zero_arr)
