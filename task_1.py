# Basic Arithmetic and Type Identification
#Create three variables: one integer, one float, and one complex number.
#Print each variable and use the type() function to confirm their data types. 

a =10
b = 3.14
c = 2+3j
print(a,b,c)
print (type(a), type(b), type(c))


#Arithmetic with Mixed Types
#•	Create one int variable (a) and one float variable (b).
#•	Print the sum, difference, product, and quotient of a and b.
#•	Print the type() of each result (notice how types may change).

a = 10
b = 4.33
print('Sum:', a + b)
print('Difference:', a - b)
print('Product:', a * b)
print('Quotient:', a / b)
print('Type of sum:', type(a + b))
print('Type of difference:', type(a - b))
print('Type of product:', type(a * b))
print('Type of quotient:', type(a / b))


#Comparison Operators
#•	Let x = 10 and y = 7.
#•	Print the results of x > y, x < y, x == y, and x != y.
#•	After observing the output, explain why each result is True or False in comments.

x = 10
y = 7
print('x > y:', x > y)  # True, because 10 is greater than 7
print('x < y:', x < y)  # False, because 10 is not less than 7
print('x == y:', x == y)  # False, because 10 is not equal to 7
print('x != y:', x != y)  # True, because 10 is not equal to 7


#Boolean Variables
#•	Define a variable status = True.
#•	Print the value of status and confirm it is a boolean using type(status).
#•	Reassign status to False and confirm its type again.

status = True
print('Status:', status)
print('Type of status:', type(status))

status = False
print('Status:', status)
print('Type of status:', type(status))


#String Creation and Length
#•	Create a string variable, for example text = "Hello World".
#•	Use len(text) to print its length.
#•	Use type(text) to verify it is a string.

text = 'Hello world'
print('Length of text:', len(text))
print('Type of text:', type(text))


#String Indexing
#•	With the string s = "Python", print each character. Then print just the first and last characters using negative indexing.


s = 'Python'
print('Each character:')
for char in s:
    print(char)
print('First character:', s[0]) #first character
print('Last character:', s[-1]) #last character


#String Slicing
#•	Let lang = "Programming".
#•	Print the substring from index 0 to index 4.
#•	Print the substring from index 3 to the end.
#•	Print the substring that omits the first 2 and last 2 characters.


lang = 'Programming'
print('Substring from index 0 to 4:', lang[0:4]) #substring from index 0 to 4
print('Substring from index 3 to the end:', lang[3:11]) #substring from index 3 to the end
print('Substring that omits the first 2 and last 2 characters:', lang[2:9]) #substring that omits the first 2 and last 2 characters


#Exploring len() on Slices
#•	Continue using lang = "Programming".
#•	Slice lang to get "Program" and store it in a variable part1.
#•	Print len(part1) and comment how it differs from len(lang).

lang = 'Programming'
part1 = lang[0:7] #slice lang to get "Program"
print('Length of part1:', len(part1)) #length of part1
print('Length of lang:', len(lang)) #length of lang	
#The length of part1 is 7, while the length of lang is 11. This shows that part1 is a substring of lang and has fewer characters.


#String Methods – Case Conversion
#•	Let phrase = "Hello, Python!".
#•	Print phrase.upper() and phrase.lower().
#•	Print the original phrase to show it remains unchanged (strings are immutable).

phrase = 'Hello, Python!'
print('Uppercase:', phrase.upper()) #uppercase
print('Lowercase:', phrase.lower()) #lowercase
print('Original phrase:', phrase) #original phrase


#Combining Strings
#•	Create two strings, str1 = "Data" and str2 = "Science".
#•	Combine them into a single string with a space in between and print it.
#•	Print the length of the combined string

str1 = 'Data'
str2= 'Science'
combined = str1 + ' ' + str2
print('Combined string:', combined) 
print('Length of combined string:', len(combined))


#In-Place vs. Reassignment with String Methods
#•	Let word = "example".
#•	Call word.upper() but do not store it, then print word.
#•	Now set word = word.upper(), then print word.
#•	Comment on why the second print is different from the first.

word = 'example'
word.upper()
print(word)
word = word.upper()
print(word)
#The first print shows the original word "example" because strings are immutable and the upper() method does not change the original string. The second print shows "EXAMPLE" because we reassigned word to the result of word.upper(), which is a new string in uppercase.



#Arithmetic Operator Precedence
#•	Define a = 5, b = 3, c = 2.
#•	Print the result of the expression a + b * c.
#•	Print the result of (a + b) * c.
#•	In comments, explain how operator precedence affects the outcome.


a = 5
b = 3
c = 2
print('Result of a + b * c:', a + b * c) #result of a + b * c
print('Result of (a + b) * c:', (a + b) * c) #result of (a + b) * c
#In the first expression, multiplication has higher precedence than addition, so b * c is calculated first, resulting in 5 + 6 = 11. In the second expression, parentheses - () changes the order of operations, so a + b is calculated first, resulting in 8 * 2 = 16.



#String Index Out of Range
#•	Let text = "Hello".
#•	Attempt to access an index that doesn’t exist, like text[10].
#•	Observe the error message (IndexError) and explain why it happens in comments.

text = 'Hello'
print(text[10]) #attempt to access an index that doesn’t exist
#This will raise an IndexError because the index 10 is out of range for the string "Hello", which has indices from 0 to 4.



#Equality vs. Identity Check (Conceptual Explanation)
#•	Create two variables with the same string value, s1 = "test" and s2 = "test".
#•	Use the == operator to compare them, then use the is operator.
#•	Explain in comments what each comparison checks.

s1 = 'test'
s2 = 'test'
print('s1 == s2:', s1 == s2) #True, because the values are equal
print('s1 is s2:', s1 is s2) #True, because both variables point to the same object in memory (string interning in Python).



#Creating and Checking a Complex Number
#•	Define z = 3 + 4j.
#•	Print the real part (z.real) and the imaginary part (z.imag).
#•	Confirm that its type is complex using type(z).


z = 3 + 4j
print('Real part:', z.real) #real part
print('Imaginary part:', z.imag) #imaginary part
print('Type of z:', type(z)) #type of z


#Comparisons with Floats
#•	Let f1 = 0.1 + 0.2 and f2 = 0.3.
#•	Print f1 == f2.
#•	Print the actual values of f1 and f2 to explain any difference in the comparison outcome (floating-point precision).


f1 = 0.1 + 0.2
f2 = 0.3
print('f1 == f2:', f1 == f2) #False, because of floating-point precision issues
print('f1:', f1) #actual value of f1
print('f2:', f2) #actual value of f2	


