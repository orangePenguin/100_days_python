# Hangman Game.
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

fruits = ['apple', 'pear', 'orange', 'banana', 'strawberry', 'watermelon', 'lime', 'mango']
chosen_word = random.choice(fruits)
word_length = len(chosen_word)
lives = 6

print(f"The solution is {chosen_word}")

display = []
for blank in range(word_length):
    display += '_'
print(f"The word is {display}")

end = False
while not end:
    guess = input("Guess a Letter!").lower()
    if guess in chosen_word:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"The word is {display}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} guesses left.")
        if lives == 0:
            end = True
            print(f"You LOST! The word was \'{chosen_word}\'.")

    if '_' not in display:
        end = True
        print("You WIN!.")

    print(stages[lives])
