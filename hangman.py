

# import the arts and words
import random
from hangman_arts import stages
from hangman_arts import logo
from hangman_wordList import word_list

print(logo)
# Player's life variable
lives = 10

# placeholder variable
placeholder = ""
# Choose a random word form the list of words
chosen_word = random.choice(word_list)
# Create a placeholder with the length of the word chosen using "_"s.
for letter in chosen_word:
    placeholder = placeholder + "_"
print(placeholder)
# Game state
game_over = False
# List of correct letters chosen so far
corrected_letters = []


# Run the game till Player wins the game of loses all lives and game over.
while not game_over:
    # get player chosen letter and store it in a variable
    guessed_letter = input("Guess a letter: ").lower()
    print(guessed_letter)
    print(lives)
    display = ""
    for letter in chosen_word:
        if letter == guessed_letter:
            display = display + letter
            corrected_letters.append(letter)
        elif letter in corrected_letters:
            display = display + letter
        else:
            display = display + "_"


    if guessed_letter not in corrected_letters:
        lives = lives - 1
        if lives == 0:
            game_over = True
            print("You lose!")


    print(display)

    if "_" not in display:
        print("You win!")
        game_over = True

    print(stages[lives])
