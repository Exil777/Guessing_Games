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

game_over = False
correct_letters = []
lives = 10

while not game_over:
# creating a while loop so that the user get ask to guess a letter over and over until correct letter is guess or game over
    print(f"You have {lives} lives left")

    guess_letter = input("Guess a letter, until you the guess all the correct letters in the word ").lower()
    # asking the user to guess a letter with the input function
    #print(guess_letter)

    if guess_letter in correct_letters:
        print(f"You've already guess: {guess_letter}")
    
    display = ""
    
    for letter in random_word:
        if letter == guess_letter:
            display += letter
            correct_letters.append(guess_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    # this for look is checking to see if letter the user pick is in the random word
    print(display)


    if "_" not in display:
        game_over = True
        print("Congradulation, You win the game")  
    # if the user guess all the correct letters and the "_" disappear, user win the game       

    if guess_letter not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("I'm sorry, You ran out of chances") 
    # each time the user guess the wrong letter the user lose a life until the user runs out of lives   



