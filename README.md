# Hangman Game in Python

This is a simple implementation of the classic Hangman game using Python. The game can be played in the terminal/command prompt and is suitable for beginners who wish to understand basic Python programming concepts such as loops, conditionals, strings, and user input.

## Features

- Randomly selects a word from a predefined list.
- Allows the player to guess one letter at a time.
- Tracks the number of incorrect guesses.
- Displays the current state of the word and hangman after each guess.
- Ends the game when the word is guessed or when the maximum number of incorrect guesses is reached.

## Prerequisites

- Python 3.x installed on your machine.

## How to Run

1. **Clone this repository or download the script:**
    ```bash
    git clone https://github.com/that-guy18/CodeAlpha_HangmanGame.git
    cd game
    ```

2. **Run the game:**
    ```bash
    game.py
    ```

## Gameplay Instructions

1. The game will display the number of letters in the secret word.
2. Enter one letter per turn to guess the word.
3. If your guess is correct, the letter will be revealed.
4. If your guess is wrong, you lose one life and a part of the hangman is drawn.
5. The game ends when you either guess the word or run out of lives.

## Sample Output

```
Welcome to Hangman!
_ _ _ _ _

Guess a letter: a
Good guess!

a _ _ _ _

Guess a letter: e
Wrong guess. You have 5 lives left.

a _ _ _ _

...
```

## Customization

- Modify the list of words by editing the `word_list` variable in `game.py`.
- Adjust the number of allowed incorrect guesses by changing the `lives` variable.


## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Author

- that-guy18(https://github.com/that-guy18)
