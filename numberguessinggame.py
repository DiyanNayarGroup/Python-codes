import random

target_number = random.randrange(0, 101, 1)
print("Enter a number between 1 - 100")


match = True

while match:

    guess = int(input("Guess the number:"))

    if guess < target_number:
        print("Your number is smalled than mine. Enter a bigger number:")
    elif guess > target_number:
        print("Your number is bigger than mine. Enter a smalled number:")
    else:
        print("Good Job! You won!")
        match = False