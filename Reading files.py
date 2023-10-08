# Accessing an employee file from my main folder - reading

# open the file and store it in a variable
employee_file = open("Employee.txt", "r")
# using for loops to read the lines in the file
for employee in employee_file.readlines():
    print(employee)

# print(employee_file.readlines()[3])
# print(employee_file.readline())
# print(employee_file.read())


# Writing to a file - appending
employee_file = open("Employee.txt", "a")
employee_file.write("\nJoy - Human resources")

# write a file - overwrite a file/create a new file
employee_file = open("Employee.txt", "w")
employee_file.write("\nKevin - Driver")

employee_file = open("Employee1.txt", "w")
employee_file.write("Franklin - dev")





# close the file
employee_file.close()
