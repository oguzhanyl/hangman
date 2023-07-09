import random
word_list = ["hello", "world", "python"]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

# Testing code
print(f"boi, the solution is {chosen_word}")

# Create blanks
display = []
for blank in range(word_lenght):
    display += "_"

end_of_the_game = False
while not end_of_the_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    
    print(display)
    if "_" not in display:
        end_of_the_game = True
        print("You win!")