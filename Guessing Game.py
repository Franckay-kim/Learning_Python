# Variables
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# While Loop - lopps only if the conditions are met
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

# If statements - when you break out of the loops a message is printed
if out_of_guesses:
    print("Out of Guesses, YOU LOOSE")
else:
    print("You win!")
