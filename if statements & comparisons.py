# function to check conditions and return a suitable value
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
# call the function, pass the parameters
print(max_num(380, 640, 52))