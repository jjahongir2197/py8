import random

number = random.randint(1, 100)

tries = 0

while True:
    guess = int(input("Guess number: "))
    tries += 1

    if guess > number:
        print("Too big")

    elif guess < number:
        print("Too small")

    else:
        print("Correct!")
        print("Tries:", tries)
        break
