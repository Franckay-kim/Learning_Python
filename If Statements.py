
is_male = True
is_tall = False
# executes print when the condition is m et
if is_male:
    print("You are a male")
else:
    print("you are not a male")
# checks for more than one condition using keywords
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

# and keyword
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are tall but not a male")
else:
    print("You are not male and not tall")