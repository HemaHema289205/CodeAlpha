# HUNGAM GAME

import nltk
nltk.download('words')
from nltk.corpus import words

import random

# Predefined list of words
word_list = words.words()
chosen_word = random.choice(word_list)

# Game setup
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display word with underscores
def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in chosen_word])

# Game loop
print("Welcome to Hangman!")
while wrong_guesses < max_wrong_guesses and "_" in display_word():
    print("\nWord:", display_word())
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue


    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print("Incorrect!")

# Game over
if "_" not in display_word():
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame Over! The word was:", chosen_word)



