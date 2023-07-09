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

word_list = ["hello", "world", "python"]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

# Testing code
print(f"boi, the solution is {chosen_word}")

# Create blanks
display = []
for blank in range(word_lenght):
    display += "_"

lives = 6

end_of_the_game = False
while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    check = True
    # Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        
        if letter == guess:
            check = False
            display[position] = letter
    # Wrong letter takes a life
    if check == True:
        lives -= 1
    # Game over condition when lives runs out
    if lives == 0:
        end_of_the_game = True
        print("You died.")
    # Concatenate all items in list and convert to string
    print(f"{' '.join(display)}")
    
    # Check if user has got all letters
    if "_" not in display:
        end_of_the_game = True
        print("You win!")

    # ASCII art corresponding to current lives
    print(stages[lives])