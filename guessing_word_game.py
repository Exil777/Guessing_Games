# Recreating the hangman game for the purpose of understand the logic of creating the game.

# In the guessing word game, a random word is generated and the user is ask to guess the letters that make up the word.

# The user will have a numbers of chances to guess the correct letters until the user have the correct word or runs out of chances.

# Whenever the user guess the wrong letter one life will be deducted to total of lives the user have until the user runs out of lives before the user guess the correct word
import random
# importing the random modules so i can use the random function

print("Welcome to the game where you guess a letter until you guess the correct word")
words_list = ["apple", "jameson", "orlando", "computers", "Headphone"]
# creating a list of words

random_word = random.choice(words_list)
# generating a random word
print(random_word)

word_placeholder = ""
# creating a empty string variable so i can add my underscore space as my random word placeholder
random_word_length = len(random_word)
# getting the length of my random word
for position in range(random_word_length):
    word_placeholder += "_"
print(word_placeholder)
# adding an underscore under each letter of the random word


guess_letter = input("Guess a letter, until you the guess all the correct letters in the word ")
# asking the user to guess a letter with the input function
print(guess_letter)


for letter in random_word:
    if guess_letter == letter:
        print("letter in word")
    else:
        print("letter not in word")
# this for look is checking to see if letter the user pick is in the random word


