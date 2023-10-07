# function to give exponent of a number - using for loop
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

# call the function
print(raise_to_power(2, 3))
