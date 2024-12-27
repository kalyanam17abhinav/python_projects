import random

def play():
    user = input("what's your choice:\n'r' for rock\n'p' for paper\n's' for scissors\n").lower()
    computer = random.choice(['r','p','s'])

    if user==computer:
        return "IT IS A TIE"

    if is_win(user, computer):
        return "USER WINS"

    return "USER LOST"

def is_win(user, computer):
    if((user=='r' and computer=='s') or (user=='p' and computer=='r') or (user=='s' and computer=='p')):
        return True

do_play='y'
while do_play=='y':
    print(play())
    do_play = input('play agian? (y/n)').lower()