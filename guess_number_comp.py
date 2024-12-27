import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f"guess a no. between 1 and {x} "))
        if guess<random_number:
            print("too low")
        elif guess>random_number:
            print("too high")

    print("congrats, you guessed it correct")

limit = int(input("enter the range of the numbers: "))
guess(limit)