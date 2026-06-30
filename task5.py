# Iterate Through a Tuple and Print Types
# •	Task: Create a tuple with at least 5 different types of elements (int, float, string, bool, and complex).
# •	Use a for loop to iterate over the tuple and print each element along with its data type.

tuple_element = (8, 2.33, 'saroj', True, 2+3j)
for element in tuple_element:
    print(f"Element : {element}  |  Datatype : {type(element)}")


# Print All Items from a List with a Custom Message
# •	Task: Create a list of 4 different city names.
# •	Use a for loop to print each city name followed by the phrase "is a great place".

city_names = ['kathmandu', 'chitwan', 'pokhara', 'jhapa']
for city in city_names:
    print(f"{city} is a great place.")



# Print Each Character of a String with Its Index
# •	Task: Ask the user to enter a word.
# •	Use a for loop and enumerate() to print each character of the string along with its index.

word = input('Enter a word.')
for index,char in enumerate(word):
    print(f'index : {index}  |  char : {char}')



# Sum of Elements in a List
# •	Task: Create a list of integers.
# •	Use a for loop to calculate the sum of all the elements and print the total.

list_of_integers = int[2, 5 , 67, 8, 23, 32, 12, 43, 45, 32, 22]

total = 0
for i in list_of_integers:
    total += i
    print('total')

    
# Count Booleans in a Tuple
# •	Task: Create a tuple containing different data types, including multiple True and False values.
# •	Use a for loop to count how many True values are present and print the count.

tuple_list = (True, 'saroj', 63, False, True, True, False, True, False, True)
true_count = 0
for element in tuple_list:
    if element is True:
        true_count += 1
print(f'The amount of true values present in this is {true_count}')



# Check and Print Data Types from a List
# •	Task: Create a list with at least 6 elements of different types (int, float, str, bool, etc.).
# •	Use a for loop to iterate through the list and print the data type of each element.

list_elements = [23, 3.22, 'saroj', True, False, [1,2,3], 2+3j, 56, 'python']
for elements in list_elements:
    print(f'Data : {elements}  | Datatype : type{elements}')



# Check for Vowels in a String
# •	Task: Ask the user for a word.
# •	Use a for loop to check each character and print a message if it’s a vowel (a, e, i, o, u).


user_word = input("Please enter a word: ")

for char in user_word:
    if char in "aeiou":
        print(f"Found a vowel: '{char}'")


# Print Square of Numbers from a Tuple
# •	Task: Create a tuple of numbers from 1 to 5.
# •	Use a for loop to iterate through the tuple and print the square of each number.


numbers = (1, 2, 3, 4, 5)
for num in numbers:
    square = num ** 2  
    print(f"The square of {num} is {square}")



# Print Elements of a List in Uppercase
# •	Task: Create a list of 5 small letter containing words.
# •	Use a for loop to iterate over the list and print each word in lowercase.


words_list = ["apple", "banana", "orange", "dragonfruit", "strawberry"]

for word in words_list:
    
    print(word.lower())



# Count Numbers Greater Than 10 in a List
# •	Task: Create a list of integers.
# •	Use a for loop to count how many numbers in the list are greater than 10.
# •	Print the final count.

numbers = [4, 15, 8, 23, 42, 10, 3, 8, 12, 5, 4, 25]
count_greater_than_10 = 0

for num in numbers:
    if num > 10:
        count_greater_than_10 += 1  


print(f"Number of values greater than 10:{count_greater_than_10}")
