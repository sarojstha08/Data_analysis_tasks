# Even or Odd Checker
# •	Task: Write a program that prompts the user for an integer.
# o	Use if/else to check whether the number is even or odd.
# o	Print "Even" or "Odd" accordingly.

number = int(input('Enter an integer: '))
if number %2 == 0:
    print('Even')
else:
    print('Odd')


# Positive, Negative, or Zero
# •	Task: Write a program that prompts the user for a number.
# o	Use if/elif/else to determine if the number is positive, negative, or zero.
# o	Print a message such as "The number is positive.".

number = int(input('Enter a numnber:'))
if number > 0:
    print('The number is positive.')
elif number < 0:
    print('The number is negative.')
else:
    print('The number is zero.')


# Grade Categorizer
# •	Task: Prompt the user for a number between 0 and 100 (the score).
# o	Use if/elif/else to categorize the score:
# 	90–100: "Grade A"
# 	80–89: "Grade B"
# 	70–79: "Grade C"
# 	< 70: "Fail"

score = int(input('Enter a score between 0 and 100: '))
if score >= 90 and score <= 100:
    print('Grade A')
elif score >= 80 and score <= 89:
    print('Grade B')
elif score >= 70 and score <= 79:
    print('Grade C')
else:
    print('Fail')


# Multiples of 3 and 5
# •	Task: Prompt the user for a single integer n.
# o	Use a for loop to iterate from 1 up to n (inclusive).
# o	For each value i, print:
# 	"Multiple of both" if i is divisible by 3 and 5.
# 	"Multiple of 3" if i is divisible by 3 but not 5.
# 	"Multiple of 5" if i is divisible by 5 but not 3.
# 	The number i itself otherwise.

n = int(input('Enter a single integer n: '))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('Multiple of both')
    elif i % 3 == 0:
        print('Multiple of 3 only but not 5')
    elif i % 5 == 0:
        print('Multiple of 5')
    else:
        print(i)



# Simple Password Check
# •	Task: Prompt the user for a password (e.g., "secret").
# o	Use if to check if the user’s input matches the correct password.
# o	If correct, print "Access granted", otherwise print "Access denied".

password = input('Enter the password: ')
if password == 'secret':
    print('Access granted')
else:
    print('Access denied')



# Count Vowels in a String
# •	Task: Ask the user for a string.
# o	Use a for loop to iterate over each character.
# o	Use if conditions to check if it’s a vowel ("a", "e", "i", "o", "u").
# o	Count the total number of vowels and print the result.

vowel = 'aeiouAEIOU'
user_string = input('Enter a string: ')
vowel_count = 0

for char in user_string:
    if char in vowel:
        vowel_count += 1

print(f'The number of vowels in the string is: {vowel_count}')



# Smallest of Three Numbers
# •	Task: Prompt the user for three different numbers.
# o	Use if/elif/else to find and print which one is smallest.

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
number3 = int(input('Enter the third number: '))

if number1 <= number2 and number1 <= number3:
    print(f'The smallest number is: {number1}')
elif number2 <= number1 and number2 <= number3:
    print(f'The smallest number is: {number2}')
else:
    print(f'The smallest number is: {number3}')



# Simple Menu Selection
# •	Task: Prompt the user to choose an option (e.g., 1 for "Start", 2 for "Settings", 3 for "Exit").
# o	Use if/elif/else to print a response based on which option is chosen.
# o	Example:
# 	If user enters 1: print "Game starting..."
# 	If user enters 2: print "Opening settings..."
# 	If user enters 3 or any other: print "Exiting..."



option = int(input('Choose an option (1-3): '))
if option == 1:
    print('Game starting...')
elif option == 2:
    print('Opening settings...')
else:
    print('Exiting...')
