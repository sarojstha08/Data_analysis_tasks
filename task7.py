# Function with Default Argument
# Question:
# Create a function greet(name, message="Welcome!") that prints:
# "Hello, <name>! <message>"
# •	Call the function with and without the message argument.

def greet(name, message="Welcome!"):
    print(f"Hello, {name}! {message}")

greet("Saroj")
greet("Saroj", "Good morning!")


# Function with args (Variable Number of Arguments)
# Question:
# Create a function total(*numbers) that takes any number of numeric arguments and returns their sum.
# •	Example call: total(5, 10, 15) should return 30.

def total(*numbers):
    return sum(numbers)

result_1 = total(5, 10, 15)
print(f"total(5, 10, 15) = {result_1}")

result_2 = total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"total(1, 2, ..., 10) = {result_2}")

result_3 = total()
print(f"total() = {result_3}")


# Function with kwargs (Keyword Arguments)
# Question:
# Create a function display_info(**details) that prints key-value pairs like:
# name: Rajesh 
# age: 25  
# city: Kathmandu  

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Rajesh", age=25, city="Kathmandu")



# Function Using Both args and a Default Argument
# Question:
# Create a function repeat_words(*words, times=2) that repeats each word the given number of times.
# •	Example: repeat_words("Hi", "Bye", times=3)
# Output:

def repeat_words(*words, times=2):
    for word in words:
        print(word * times)

repeat_words("Hi", "Bye", times=3)
repeat_words("Apple", "Banana")


# Function Using All Types of Parameters Together
# Question:
# Create a function user_profile(name, age=18, *hobbies, **extra_info) that:
# •	Prints the name and age.
# •	Prints all hobbies (if any).
# •	Prints any additional info passed via **kwargs.

def user_profile(name, age=18, *hobbies, **extra_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"{hobby}")
    else:
         print("Hobbies: None specified")
            
    if extra_info:
        print("Additional Info:")
        for key, value in extra_info.items():
            print(f"  {key}: {value}")
    else:
        print("Additional Info: None specified")

user_profile("Rajesh", 25, "Reading", "Hiking", "Coding", city="Kathmandu", job="Developer")
user_profile("Sachin")