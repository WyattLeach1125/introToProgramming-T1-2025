import random

randint = random.randint(1, 100)
Trueguess = False

while Trueguess == False:
    guessint = int(input("Guess a number\n>"))
    if guessint < randint:
        print("too low, try again!")
    elif guessint > randint:
        print("too high, try again!")
    else:
        print("Correct!")
        Trueguess = True
