# translate a phrase to add g where there is a vowel
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


# call the function and print the result
print(translate(input("Enter a phrase: ")))
