Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Get user input and store it in first_name
firstname = input("Please enter your firstname:")
Please enter your firstname:Keerthi
print(f"Your firstname is: {firstname}")
Your firstname is: Keerthi
# Print the user's first name ,  # Print the data type of first_name
print(f"The data type of your firstname is: {type(firstname)}")
The data type of your firstname is: <class 'str'>



 # Get user input and store it in last_name
 
lastname = input("Please enter your lastname:")
Please enter your lastname:Gurram
# Print the user's full name
print(f"Your name is {firstname} {lastname}!")
Your name is Keerthi Gurram!



# Get user input and store it in age
age = int(input("Please enter your age:"))
Please enter your age:26
 # Print the user's age
 
print(f"You are {age} years old...")
You are 26 years old...



# Convert the age from a string to an integer
age_in_years = int(age)
# Calculate the number of seconds in a year
seconds_in_a_year = 365 * 24 * 60 * 60
# Calculate age in seconds
age_in_seconds = age_in_years * seconds_in_a_year
# Print the age in seconds
print("Which means you're at least", age_in_seconds, "seconds old...")
Which means you're at least 819936000 seconds old...
# Print the data type of age_in_seconds
print("The data type of this number is:", type(age_in_seconds))
The data type of this number is: <class 'int'>



print("Please enter the value of pi: ")
pi = float(input())  # Get user input and convert it to a float
print("Please enter the radius of the circle: ")
radius = float(input())  # Get user input and convert it to a float
area_of_circle = pi * (radius ** 2)  # Calculate the area of the circle
print("Given that a circle has a radius =", radius, "and pi =", pi, "then the circle's area =", area_of_circle)
print("The data type of this area is:", type(area_of_circle))  # Print the data type of area_of_circle
SyntaxError: multiple statements found while compiling a single statement



print("Please enter the value of pi:")
Please enter the value of pi:
Please enter the value of pi:34
SyntaxError: invalid syntax

print("Please enter the value of pi: ")
Please enter the value of pi: 

pi = float(input())  # Get user input and convert it to a float

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    pi = float(input())  # Get user input and convert it to a float
ValueError: could not convert string to float: ''
print("Please enter the value of pi:")
Please enter the value of pi:

print("Please enter the value of pi: ")
Please enter the value of pi: 
3.14
3.14
pi = float(input()) # Get user input and convert it to a float
print("Please enter the radius of the circle: ")

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    pi = float(input()) # Get user input and convert it to a float
ValueError: could not convert string to float: 'print("Please enter the radius of the circle: ")'
print("Please enter the radius of the circle: ")
radius = float(input())
SyntaxError: multiple statements found while compiling a single statement
print("Please enter the radius of the circle: ")

Please enter the radius of the circle: 
3.14
3.14
radius = float(input())

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    radius = float(input())
ValueError: could not convert string to float: ''
print("Please enter the radius of the circle: ")
Please enter the radius of the circle: 
>>> 2
2
>>> radius = float(input())

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    radius = float(input())
ValueError: could not convert string to float: ''
>>> pi = float(input("Please enter the value of pi: "))
Please enter the value of pi: 3.14
>>> radius = float(input("Please enter the radius of the circle: "))
... 
Please enter the radius of the circle: 2
>>> area = pi * (radius ** 2)
... 
>>> print(f"Given that a circle has radius = {radius} and pi = {pi}, then the circle's area = {area}.")
... 
Given that a circle has radius = 2.0 and pi = 3.14, then the circle's area = 12.56.
>>> print(f"The data type of area is: {type(area)}")
... 
The data type of area is: <class 'float'>
>>> story = input("Please tell me a one sentence story: ")
... 
Please tell me a one sentence story: "Cool story bro! It's got length characters, the first one is a first, the second one is a second and the last one is a last."
>>> length = len(story)
... 
>>> first = story[0]
... 
>>> second = story[1]
... 
>>> last = story[-1]
... 
>>> print(f"Cool story bro! It's got {length} characters, the first one is a '{first}', the second one is a '{second}' and the last one is a '{last}'.")
... 
Cool story bro! It's got 126 characters, the first one is a '"', the second one is a 'C' and the last one is a '"'.
>>> print(f"The data type of length is: {type(length)}")
... 
The data type of length is: <class 'int'>
>>> print(f"The data type of second character is: {type(second)}")
... 
The data type of second character is: <class 'str'>
