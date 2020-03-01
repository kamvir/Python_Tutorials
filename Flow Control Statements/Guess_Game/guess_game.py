# import random

secret_number = 9

# secret_number = round(random.random() * 100)

guess_count = 0

guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("Sorry, you failed! Correct number is :: " + str(secret_number))
