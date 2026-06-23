# Python Data Structures Assignment 
# Section 1: Lists
# 1.	Create a List:
# Create a list containing the numbers 1 through 15. Print the list.

numbers = list(range(1, 16))
print(numbers)

# 2.	List of Strings:
# Create a list of your five favorite fruits. Print the list.

fruits = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
print(fruits)

# 3.	Accessing Elements:
# Given the list [10, 20, 30, 40, 50], print the first and last element using positive and negative indexing.

numbers_list = [10, 20, 30, 40, 50]
print(numbers_list[0])
print(numbers_list[-1])

# 4.	List Length:
# Create a list of any 5 items and print its length using the len() function.

items = ['Pen', 'Notebook', 'Eraser', 'Ruler', 'Pencil']
print(len(items))

# 5.	Appending Elements:
# Start with an empty list and append the numbers 1, 2, and 3. Print the list.

empty_list = []
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
print(empty_list)

# 6.	Inserting an Element:
# Given a list [1, 3, 4], insert the number 2 at the correct position so that the list becomes [1, 2, 3, 4].

numbers = [1, 3, 4]
numbers.insert(1, 2)
print(numbers)

# 7.	Removing an Element:
# Remove the number 3 from the list [1, 2, 3, 4, 5] using a list method and print the new list.

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)   
print(numbers)

# 8.	Popping an Element:
# Given the list [10, 20, 30, 40], pop the last element and print the element and the updated list.

numbers = [10, 20, 30, 40]
popped_element = numbers.pop()
print('Popped element:', popped_element)
print(numbers)

# 9.	Slicing a List:
# Given the list [0, 1, 2, 3, 4, 5], print a slice that contains the elements from index 2 to 4.

numbers = [0, 1, 2, 3, 4, 5]
sliced_list = numbers[2:5]  
print(sliced_list)

# 10.	List Concatenation:
# Concatenate two lists, e.g., [1, 2, 3] and [4, 5, 6], and print the resulting list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]   
combined = list1 + list2
print(combined)

# 11.	Repeating a List:
# Create a list [1, 2] and print the list repeated three times.

list = [1, 2]
repeated_list = list * 3
print(repeated_list)

# 12.	Copying a List:
# Create a copy of a given list and print both the original and the copy.

original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print("Original List:", original_list)
print("Copied List:", copied_list)

# 13.	Clearing a List:
# Given any list, use a method to clear all its elements and then print the empty list.

my_list = [1, 2, 3, 4, 5]
my_list.clear()
print("Cleared List:", my_list)






# Section 2: Tuples
# 1.	Create a Tuple:
# Create a tuple containing the numbers 1, 2, and 3. Print the tuple.

numbers_tuple = (1, 2, 3)
print(numbers_tuple)

# 2.	Tuple of Strings:
# Create a tuple of three different color names and print it.

colors = ('Red', 'Green', 'Blue')
print(colors)

# 3.	Accessing Tuple Elements:
# Given the tuple (10, 20, 30, 40), print the second element.

numbers_tuple = (10, 20, 30, 40)
print(numbers_tuple[1])

# 4.	Tuple Slicing:
# Using the tuple (0, 1, 2, 3, 4), print a slice that contains elements from index 1 to 3.

numbers_tuple = (0, 1, 2, 3, 4)
sliced_tuple = numbers_tuple[1:4]
print(sliced_tuple)

# 5.	Concatenating Tuples:
# Concatenate two tuples, e.g., (1, 2) and (3, 4), and print the result.

tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# 6.	Tuple Unpacking:
# Store the tuple ("Alice", 25, "New York") into three variables and print them.

person_info = ("Alice", 25, "New York")
name, age, city = person_info
print("Name:", name)
print("Age:", age)
print("City:", city)

# 7.	Convert List to Tuple:
# Convert the list [1, 2, 3, 4] into a tuple and print the tuple.

list_to_tuple = [1, 2, 3, 4]
tuple_from_list = tuple(list_to_tuple)
print(tuple_from_list)

# 8.	Counting Occurrences:
# Given the tuple (1, 2, 2, 3, 2), count how many times the number 2 appears.

numbers_tuple = (1, 2, 2, 3, 2)
count = numbers_tuple.count(2)
print("Number of occurrences of 2:", count)

# 9.	Finding an Index:
# In the tuple (10, 20, 30, 40), find the index of the element 30 and print it.

numbers_tuple = (10, 20, 30, 40)
index_of_30 = numbers_tuple.index(30)   
print("Index of 30:", index_of_30)
