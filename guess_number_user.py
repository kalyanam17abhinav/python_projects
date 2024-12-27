import random

def computer_guess(x):
    low, high = 1, x
    feedback=''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} is too low(L), too high(H), or correct(C) ').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f'computer guessed {guess} correctly')

limit = int(input("enter the range of the numbers: "))
computer_guess(limit)