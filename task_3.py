# Integer & Float Mix
# •	Create an integer a and a float b.
# •	Perform addition, subtraction, multiplication, and division on them.
# •	Print the results and observe the type of each result with type().

a = 10
b = 5.55
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Type of addition:", type(a + b))
print("Type of subtraction:", type(a - b))
print("Type of multiplication:", type(a * b))
print("Type of division:", type(a / b))

# Large Integers & Type
# •	Assign a very large integer to a variable (e.g., in the billions).
# •	Print it and confirm its type is still int in Python or not.

large_int = 12345678901234567890
print("Large Integer:", large_int)
print("Type of large integer:", type(large_int))

# Complex Number Basics
# •	Create a complex number z = 3 + 4j.
# •	Print its real part, imaginary part, and confirm its type is complex.
# •	Perform a basic arithmetic operation with another complex number (e.g., (3 + 4j) + (1 + 2j)).

z = 3 + 4j
print("Real part:", z.real)
print("Imaginary part:", z.imag)
print("Type of complex number:", type(z))

complex_sum = z + (1 + 2j)
print("Sum of complex numbers:", complex_sum)

# Boolean from Comparisons
# •	Create two variables, m = 10 and n = 15.
# •	Define status = (m > n) and print status.
# •	Confirm type(status) is bool.
# •	Assign status = (m != n) and print again.

m = 10
n = 15
status = (m > n)
print("Status (m > n):", status)
print("Type of status:", type(status))
status = (m != n)
print("Status (m != n):", status)
print("Type of status:", type(status))

# String Creation & Indexing
# •	Create a string text = "HelloWorld".
# •	Print the first and last characters using positive and negative indexing.
# •	Comment on the total length of the string.

text = "HelloWorld"
print("First character (positive index):", text[0])
print("Last character (positive index):", text[len(text) - 1])
print("First character (negative index):", text[-1])
print("Last character (negative index):", text[-len(text)])


# String Slicing
# •	With lang = "PythonProgramming", print the substring from index 2 to 8.
# •	Print the substring from the start up to index 5.
# •	Print the entire string in reverse using slicing.

lang = "PythonProgramming"
print("Substring from index 2 to 8:", lang[2:9])
print("Substring from start to index 5:", lang[:5])
print("Entire string in reverse:", lang[::-1])


# String Methods
# •	Let phrase = " Hello, Python World! ".
# •	Demonstrate strip(), upper(), and replace() on this string.
# •	Print the results and comment on immutability of strings in Python.

phrase = " Hello, Python World! "
stripped_phrase = phrase.strip()
upper_phrase = phrase.upper()
replaced_phrase = phrase.replace("Python", "Java")

print("Stripped phrase:", stripped_phrase)
print("Upper phrase:", upper_phrase)
print("Replaced phrase:", replaced_phrase)
# Comment: Strings are immutable in Python, meaning that methods like strip(), upper(), and replace() return new strings rather than modifying the original string in place.


# String Formatting
# •	Create two variables: name = "Rajesh" and score = 95.
# •	Print: "Alice scored 95 points." using two methods (concatenation and an f-string or str.format()).

name = "Rajesh"
score = 95

# Using concatenation
print("Alice scored " + str(score) + " points.")

# Using an f-string
print(f"{name} scored {score} points.")

# Boolean Operations in Expressions
# •	Write a small expression using and, or, and not with boolean values.
# •	Example: result = not(True and False) or (5 > 3).
# •	Print result and explain how Python evaluated the expression.

result = not(True and False) or (5 > 3)
print("Result of the boolean expression:", result)
# Comment: The expression evaluates as follows: True and False is False, not(False) is True, and (5 > 3) is True. Therefore, the final result is True or True, which evaluates to True.


# List Creation & Access
# •	Create a list of 5 different integers.
# •	Print the first item, middle item, and last item using indexing.

numbers = [10, 20, 30, 40, 50]
print("First item:", numbers[0])
print("Middle item:", numbers[len(numbers) // 2])
print("Last item:", numbers[-1])


# List Insertion & Deletion
# •	Start with a list nums = [10, 20, 30, 40].
# •	Insert 25 at index 2.
# •	Remove the last element.
# •	Print the updated list.

nums = [10, 20, 30, 40]
nums.insert(2, 25)
nums.pop()
print("Updated list:", nums)


# List Slicing
# •	Given letters = ["a", "b", "c", "d", "e"], print the slice that contains only ["b", "c", "d"].
# •	Print the slice that omits the first and the last element.

letters = ["a", "b", "c", "d", "e"]
slice_bcd = letters[1:4]
print("Slice containing ['b', 'c', 'd']:", slice_bcd)

slice_omit_first_last = letters[1:4]
print("Slice omitting first and last element:", slice_omit_first_last)


# Sorting & Reversing
# •	Create a list of random integers.
# •	Sort the list in ascending order and print it.
# •	Reverse the sorted list and print again.

random_numbers = [42, 15, 8, 23, 4, 8, 1, 23, 62, 18]
random_numbers.sort()
print("Sorted list:", random_numbers)
random_numbers.reverse()
print("Reversed sorted list:", random_numbers)



# Combining Lists
# •	Let list1 = [1, 2, 3] and list2 = [4, 5, 6].
# •	Combine them into a single list and print.
# •	Demonstrate two ways: using + and using .extend().

list1 = [1, 2, 3]
list2 = [4, 5, 6]   
# Combining using +
combined_list_plus = list1 + list2
print("Combined list using +:", combined_list_plus)

# Combining using .extend()
list1.extend(list2)
print("Combined list using .extend():", list1)


# Aggregating List Values
# •	Create a list of floats, e.g., [2.5, 3.6, 1.2, 5.0].
# •	Print the sum, minimum, and maximum of that list using built-in functions.

float_list = [2.5, 3.6, 1.2, 5.0]
print("Sum of float list:", sum(float_list))
print("Minimum of float list:", min(float_list))
print("Maximum of float list:", max(float_list))


# Tuple Creation
# •	Create a tuple t = (10, 20, "Hello", True).
# •	Print the tuple and confirm its type with type(t).

t = (10, 20, "Hello", True)
print("Tuple:", t)
print("Type of tuple:", type(t))


# Tuple Indexing & Slicing
# •	Print the first two elements of t using slicing.
# •	Print the last element of t using negative indexing.

print("First two elements of tuple:", t[0:2])
print("Last element of tuple using negative indexing:", t[-1])


# Tuple Unpacking
# •	Suppose t2 = ("Tom", 25, "Engineer").
# •	Unpack it into three separate variables: name, age, profession.
# •	Print these variables individually.

t2 = ("Tom", 25, "Engineer")
name, age, profession = t2
print("Name:", name)
print("Age:", age)
print("Profession:", profession)


# Attempt Tuple Mutation
# •	Try to change an element of t (t[0] = 999) and observe the error.
# •	In comments, explain why the error occurs.

# t[0] = 999  # This will raise a TypeError because tuples are immutable in Python, meaning their elements cannot be changed after creation.


# Set Creation & Membership
# •	Create a set my_set = {1, 3, 5, 7}.
# •	Check if 5 is in my_set.
# •	Check if 2 is not in my_set.

my_set = {1, 3, 5, 7}
print("Is 5 in my_set?", 5 in my_set) 
print("Is 2 not in my_set?", 2 not in my_set)


# Add & Remove Elements
# •	Add 9 to my_set.
# •	Remove 3 from my_set.
# •	Print the updated set.

my_set.add(9)
my_set.remove(3)
print("Updated set:", my_set)


# Set Operations
# •	Create two sets: setA = {1, 2, 3} and setB = {3, 4, 5}.
# •	Print the union, intersection, and difference (setA - setB).

setA = {1, 2, 3}
setB = {3, 4, 5}
print("Union:", setA | setB)
print("Intersection:", setA & setB)
print("Difference (setA - setB):", setA - setB)


# Check Unique Values
# •	Define a list vals = [1, 2, 2, 3, 3, 3, 4].
# •	Convert it to a set.
# •	Print both the list and the set to show how duplicates are removed.

vals = [1, 2, 2, 3, 3, 3, 4]
unique_vals = set(vals)
print("Original list:", vals)
print("Set with unique values:", unique_vals)

# Frozenset Creation
# •	Create a frozenset from a list [2, 4, 4, 6].
# •	Print it and observe whether duplicates are preserved.

frozen_set = frozenset([2, 4, 4, 6])
print("Frozenset:", frozen_set)


# Operator Precedence
# •	Define a = 4, b = 2, c = 5.
# •	Print the result of a + b * c vs. (a + b) * c.
# •	Explain in comments how the result differs.

a = 4
b = 2
c = 5
print("Result of a + b * c:", a + b * c)
print("Result of (a + b) * c:", (a + b) * c)
# Comment: In the first expression, multiplication has higher precedence than addition, so b * c is calculated first, resulting in 4 + 10 = 14. In the second expression, parentheses change the order of operations, so a + b is calculated first (4 + 2 = 6), and then multiplied by c (6 * 5 = 30).


# Modulo & Floor Division
# •	Let x = 17 and y = 4.
# •	Print x % y and x // y.
# •	Explain the difference between these two operators in comments.

x = 17
y = 4
print("x % y:", x % y)
print("x // y:", x // y)
# Comment: The modulo operator (%) returns the remainder of the division, while the floor division operator (//) returns the quotient of the division, rounded down to the nearest integer.



# Power Operator
# •	Print the result of 2 ** 3.
# •	Write a line to calculate 3 ** 4.
# •	Print the addition of both.

n1 = 2 ** 3
n2 = 3 ** 4
print("Result of 2 ** 3:", n1)
print("Result of 3 ** 4:", n2)
print("Addition of both:", n1 + n2)

# String Comparison
# •	Compare "apple" and "banana" with <, >, and ==.
# •	Print the results.

c1 = "apple"
c2 = "banana"
print("c1 < c2:", c1 < c2)
print("c1 > c2:", c1 > c2)
print("c1 == c2:", c1 == c2)


# Mixed Type Comparison
# •	Compare 5 and 5.0 with ==.
# •	Compare 5 and 5.0 with is.
# •	Discuss the results in comment.

a = 5
b = 5.0
print("a == b:", a == b)
print("a is b:", a is b)
# Comment: 5 == 5.0 returns True because they have the same value, but 5 is 5.0 returns False because they are different objects in memory.


# Chain Comparisons
# •	Evaluate the expression 2 < 3 < 5.
# •	Print the result and explain how Python handles chained comparisons.

result = 2 < 3 < 5
print("Result of 2 < 3 < 5:", result)

# Comment: Python evaluates chained comparisons by checking each comparison in sequence. In this case, it checks if 2 < 3 (True) and then if 3 < 5 (True). Since both comparisons are True, the overall result is True.


# Logical and
# •	Define p = True and q = False.
# •	Print p and q.
# •	Demonstrate a real-world example: (age > 18) and (has_ID == True).

p = True
q = False
print("p:", p)
print("q:", q)
age = 26
has_ID = True
print((age > 18) and (has_ID))



# Logical or
# •	Using the same p and q, print p or q.

print("p or q:", p or q)


# Logical not
# •	Let r = (10 > 5).
# •	Print r, then print not r.

r = (10 > 5)
print("r:", r)
print("not r:", not r)


# Using len()
# •	Create a list with 7 elements.
# •	Use len() to get the total count.
# •	Print the result.

my_list = [1, 2, 3, 4, 5, 6, 7]
print("Length of my_list:", len(my_list))


# Using type()
# •	For each of the following: 10, 10.5, "ten", True, 3+2j, print type(...).
# •	Summarize in comments the data types you observed.

print("Type of 10:", type(10))
print("Type of 10.5:", type(10.5))  
print("Type of 'ten':", type("ten"))
print("Type of True:", type(True))
print("Type of 3+2j:", type(3+2j))
# Comment: The data types observed are int for 10, float for 10.5, str for "ten", bool for True, and complex for 3+2j.


# Using abs()
# •	Print abs(10), abs(-10), and abs(-3.5).
# •	Explain what abs() does in comments.

print("abs(10):", abs(10))
print("abs(-10):", abs(-10))
print("abs(-3.5):", abs(-3.5))
# Comment: The abs() function returns the absolute value of a number, effectively removing its sign.


# Using round()
# •	Demonstrate round(3.14159, 2).
# •	Show how round(2.5) behaves in Python.

print("round(3.14159, 2):", round(3.14159, 2))
print("round(2.5):", round(2.5))
# Comment: The round() function rounds a floating-point number to a specified number of decimal places. When the fractional part of the number is exactly 0.5, Python rounds to the nearest even number (this is known as "round half to even" or "bankers' rounding").

# Using sum(), max(), min()
# •	Create a list of numeric values.
# •	Print sum(), max(), and min() of that list.

numbers = [10, 20, 30, 40, 50]
print("Sum of numbers:", sum(numbers))
print("Max of numbers:", max(numbers))
print("Min of numbers:", min(numbers))


# Using sorted()
# •	Create a list or tuple vals = (3, 1, 4, 2).
# •	Use sorted(vals) and print the result.
# •	Show that vals itself is unchanged.

vals = (3, 1, 4, 2)
sorted_vals = sorted(vals)
print("Original vals:", vals)
print("Sorted vals:", sorted_vals)


# Using any() / all()
# •	Create a list of booleans, for example [True, False, True].
# •	Print any() on the list, then all() on the list.
# •	Show the difference in how they evaluate.

bool_list = [True, False, True]
print("any(bool_list):", any(bool_list))
print("all(bool_list):", all(bool_list))    


# Storing Booleans from Comparisons
# •	Compare two values in separate expressions, e.g., a = (10 > 3), b = (5 == 5).
# •	Combine these booleans with and or or.
# •	Print the final result.

a = (10 > 3)
b = (5 == 5)
c = a and b
d = a or b
print("Result of a and b:", c)
print("Result of a or b:", d)


# Multiline String & Counting
# •	Create a multiline string describing your favorite hobby.
# •	Use the string method .count(substring) to count how many times the letter "a" appears (case-insensitive).
# •	Print the count and explain any steps taken to handle case sensitivity.

hobby_description = '''I enjoy hiking in the mountains. It allows me to connect with nature and stay fit.
I also like to read books about adventure and exploration.'''
print("Count of 'a' in hobby_description:", hobby_description.lower().count('a'))
# Comment: To handle case sensitivity, I converted the entire string to lowercase using .lower() before counting the occurrences of 'a'.


# Advanced String Slicing
# •	Take the string "ABCDEFGHIJ" and slice every second character, resulting in "ACEGI".
# •	Print the sliced string.
# •	Also slice in reverse step.

letters = "ABCDEFGHIJ"
sliced_letters = letters[::2]
print("Sliced letters:", sliced_letters)

# Slice in reverse step
reversed_sliced_letters = letters[::-2]
print("Reversed sliced letters:", reversed_sliced_letters)


# Casefold vs. Lower
# •	Create two strings, "Case" and "case".
# •	Compare them with the regular == operator directly.
# •	Compare them again after applying .casefold().
# •	Print results and comment on how .casefold() differs from .lower() in edge cases.

str1 = "Case"
str2 = "case"
print("Direct comparison (==):", str1 == str2)
print("Comparison with .casefold():", str1.casefold() == str2.casefold())
# Comment: The .casefold() method is more aggressive than .lower() and is designed for caseless matching, especially for certain Unicode characters. While .lower() simply converts uppercase letters to lowercase, .casefold() can handle more complex cases, making it suitable for case-insensitive comparisons across different languages and scripts.


# Formatted Printing
# •	Define name = "Ramesh", product = "Notebook", quantity = 2, and price = 12.50.
# •	Use an f-string (or str.format()) to print:
# "Ramesh purchased 2 Notebook for a total of $25.0."

name = "Ramesh"
product = "Notebook"
quantity = 2
price = 12.50

# Formatted Printing
print(f"{name} purchased {quantity} {product} for a total of ${quantity * price:.1f}")



# Type Conversion Chain
# •	Ask a user for a string that represents a number, e.g., "0".
# •	Convert it to a float, then to a bool, and print the intermediate and final results.

user_input = input("Enter a number as a string (e.g., '0'): ")
float_value = float(user_input)
bool_value = bool(float_value)
print("Float value:", float_value)
print("Bool value:", bool_value)


# String List Sorting
# •	Given fruits = ["apple", "banana", "cherry"], sort them in descending alphabetical order.
# •	Print the sorted list, then use the .reverse() method to flip it. Compare the two results.

fruits = ["apple", "banana", "cherry"]
fruits.sort(reverse=True)
print("Sorted in descending order:", fruits)
fruits.reverse()
print("After reversing:", fruits)


# Insert Using Slicing
# •	Start with a list [2, 5, 7, 1, 9].
# •	Insert the value 4 right after the 2 using slicing (not insert() or append()).
# •	Print the modified list.

numbers = [2, 5, 7, 1, 9]
# Find the index of 2
index_of_2 = numbers.index(2)
# Insert 4 after the index of 2
numbers[index_of_2 + 1:index_of_2 + 1] = [4]
print("Modified list:", numbers)


# Indexing Within a Mixed List
# •	Create a list info = ["John", 28, True, 4500.75].
# •	Print only "John" and 4500.75 using their indices.

info = ["John", 28, True, 4500.75]
print("Name:", info[0])
print("Salary:", info[3])


# Tuple Concatenation & Replication
# •	Create two tuples (1, 2) and (3, 4).
# •	Concatenate them into (1, 2, 3, 4).
# •	Replicate (1, 2) 3 times to get (1, 2, 1, 2, 1, 2).

tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
replicated_tuple = tuple1 * 3
print("Concatenated tuple:", concatenated_tuple)
print("Replicated tuple:", replicated_tuple)


# Single-Element Tuple
# •	Demonstrate that (42,) is a tuple whereas (42) is just an integer.

single_element_tuple = (42,)
not_a_tuple = (42)
print("Single-element tuple:", single_element_tuple)
print("Not a tuple:", not_a_tuple)
# Comment: The comma in (42,) indicates that it is a tuple, while (42) without the comma is just an integer.


# Intersection & Union
# •	Let setA = {1, 2, 3, 4} and setB = {1,2,3}.
# •	Print their intersection using setA & setB.
# •	Print their union using setA | setB.

setA = {1, 2, 3, 4}
setB = {1, 2, 3}   
print("Intersection of setA and setB:", setA & setB)
print("Union of setA and setB:", setA | setB)


# Subset and Superset
# •	Check if setB is a subset of setA using setB.issubset(setA).
# •	Check if setA is a superset of setB using setA.issuperset(setB).
# •	Print the results.

setB_is_subset = setB.issubset(setA)
setA_is_superset = setA.issuperset(setB)
print("Is setB a subset of setA?", setB_is_subset)
print("Is setA a superset of setB?", setA_is_superset)







