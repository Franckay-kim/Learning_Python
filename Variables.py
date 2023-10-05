# Defining and Using variables
character_name = 'John'
character_age = '35'

print("My name is " + character_name + ". I am " + character_age + " years.")


# Working with strings in Python
print("Giraffe Academy")

# new line, quotation mark
print("Giraffe\nAcademy")
print("Giraffe\"Academy")

# string variable
phrase = "Giraffe"
print(phrase)

# string concatenation
print(phrase + " is cool.")

# using functions with strings
print(phrase.lower())
print(phrase.upper())  # prints the string in uppercase
print(phrase.isupper())  # check whether a string is uppercase. returns trues or false
print(phrase.upper().isupper())  # using the functions in combination
print(len(phrase))   # prints the length of a string
print(phrase[0])   # getting individual characters
print(phrase.index("G"))  # getting index of a character by passing it as a parameter in the index function
print((phrase.replace("Giraffe", "Elephant")))  # Replaces a value of a string with a new value


# Working with Numbers in Python
print(2.087)
print(3 + 2.1)   # using normal maths operations using numbers
print(3 * (4 + 5))   # using parenthesis to specify order of operation
print(10 % 3)   # Modulus operator. returns remainder. read as 10 mod 3.

# Store numbers inside variables
my_num = 5
print(my_num)

print(str(my_num))  # convert a number into a string

# using functions with numbers
my_num = -4
print(abs(my_num))   # prints absolute value

print(pow(2, 5))   # raising 2 to the power of 5

# Importing functions into my python code
from math import *   # imports math functions to my code and I can access a variety of functions

print(floor(3.8))   # Gives the whole no. without rounding up
print(ceil(3.9))  # rounds up the number upwards to the next whole number
print(sqrt(36))   # square root

