# catching errors when one inputs a non-integer
try:
    number = int(input("Enter a number: "))
    print(number)
# specifies the error to except
except ValueError:
    print("Invalid Input")