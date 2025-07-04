import random

# List of words to choose from
word_list = ["rain", "sunny", "cloudy", "storm", "wind"]

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a list to show guessed letters (initially all underscores)
display = ['_'] * word_length

# Number of incorrect attempts allowed
lives = 6

# To store guessed letters
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Game loop
while lives > 0 and '_' in display:
    print("\n" + " ".join(display))
    guess = input("Guess a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        # Correct guess: update display
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print(f"Good job! '{guess}' is in the word.")
    else:
        # Wrong guess
        lives -= 1
        print(f"Sorry, '{guess}' is not in the word. Lives left: {lives}")

# Game outcome
if '_' not in display:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame Over! The word was:", chosen_word)
