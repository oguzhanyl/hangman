import random
from hangman_art import stages,logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

# Testing code
# print(f"boi, the solution is {chosen_word}")

print(logo)

# Create blanks
display = []
for blank in range(word_lenght):
    display += "_"

lives = 6

end_of_the_game = False
while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    check = True

    # When the guessed letter is re-entered
    if guess in display:
        print("You already guessed this letter.")

    # Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    
    # Wrong letter takes a life and check if user is wrong
    if guess not in chosen_word:
        print("This letter guess not have in chosen word.")
        lives -= 1

        # Game over condition when lives runs out
        if lives == 0:
            end_of_the_game = True
            print(f"You died. The word was: {chosen_word}")

    # Concatenate all items in list and convert to string
    print(f"{' '.join(display)}")
    
    # Check if user has got all letters
    if "_" not in display:
        end_of_the_game = True
        print("You win!")

    # ASCII art corresponding to current lives
    print(stages[lives])