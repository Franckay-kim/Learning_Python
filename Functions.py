# Function with two parameters
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

# call the function and pass required parameters
say_hi("Frank", "35")

# Return keyword from a function - using it to get a return value from a function
def cube(num):
    return num*num*num
# create a variable to call the function and pass the required parameters
result = cube(4)
print(result)

