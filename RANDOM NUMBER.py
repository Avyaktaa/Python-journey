import random
while True:
    Choice = int(input("Guess a number between 1 and 10: "))
    number = random.randint(1,10)
    if Choice == number:
        print("You guessed it right")
        break
    else:
        print("You guessed it wrong")