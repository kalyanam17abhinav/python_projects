import random
from words import words
import string

# print(random.choice(words))

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word

# print(get_valid_word(words))

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters)>0 and lives>0:
        print("you have ",lives, "lives left and you have used these letters", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives-1
                print("letter is not in word")

        elif user_letter in used_letters:
            print(f"you have already guessed {user_letter}")

        else:
            print("invalid character")
    if lives==0:
        print("your lives are completed, the word was ", word)
    else:
        print("you guessed correctly ", word)

hangman()