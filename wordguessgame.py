import random  # Uses the random module to choose a random word.

# Print statement to welcome the player to the game.
print("\nWelcome to the Word Guessing Game!")

# Asks the player's name and prompts the player to enter their name.
name = input("What is your name? ""My name is: ")

# Capitalizes the first character (of each word) of the player's name.
name = name.title()

# Message to wish the player good luck.
# The player's name is being mentioned to enhance the player's experience and make them more involved.
print("Good luck " + name + ".")

# List of words which is saved to the variable 'words'.
words = ['repository', 'commit', 'branch', 'pull request', 'merge', 'fork', 'issue', 'clone', 'gitignore', 'README', 'workflow', 'collaborator', 'version control',
         'GitHub Pages', 'repository owner', 'issue tracker', 'branch protection', 'code review', 'git push', 'git pull']

# Chooses a random word from the list which the player has to guess.
# Uses the .choice function of the random module to pick a random word from the provided list.
word = random.choice(words)

# Message to let the player know that the game will now really begin.
# Creates a sense of tension to ensure that the player will take the game serious.
print("\nTIME TO GUESS THE CHARACTERS.")

# Variable to store the player's guesses.
# Everytime the player takes a guess, the guessed character, is stored inside the variable 'guesses'.
guesses = ''

# Number of turns the player has to guess the correct word.
turns = 9  # Every character that is prompted costs one turn.

# While loop to allow the player to guess the word (from the list 'words') within the allowed attempts.
# Continues the loop until the player has exceeded the maximum number of allowed attempts.
while turns > 0:

    # Variable which determines when the player has failed to guess the word, within the allowed attempts.
    failed = 0

    # For loop which goes through every character of the (chosen) word the player has to guess.
    for char in word:

        # Shows the character of the word, if the player has entered the right character.
        if char in guesses:
            # Prints the character when it has been guessed.
            print(char, end=" ")

        # Shows space between two (or more) words.
        elif char == " ":
            # Prints a space instead of an underscore for spaces between (two) words.
            print(" ", end=" ")

        # No character will be shown when the entered character is not correct.
        else:
            # The place of the right character will stay empty (an underscore) when the guess is not correct.
            print("_", end=" ")
            # Inceases the 'failed'' count with 1, everytime the guess is not correct.
            failed += 1

    # If statement when the player has guessed the right word, within the allowed attempts.
    if failed == 0:
        # Prints "You've Won' when the correct word has been guessed.
        print("\n\tYou've Won!")
        # Prints the correct word after the player has guessed it.
        print("The correct word is indeed: " + "(" + word + ")")
        # Break to stop the loop since the player has guessed the right word.
        break

    print()  # Prints a newline for better readability.

    # Prompts the player to guess a character.
    guess = input("Guess a character: ")  # Input for the character.

    # While loop to ensure the player will only enter one character at a time.
    while len(guess) != 1:
        print("\nPlease enter only one character.")
        guess = input("\nGuess a character: ")

    # The correct (guessed) word is being added the the variable 'guesses'.
    guesses += guess

    # If statement when the prompted character is not correct.
    if guess not in word:
        # Decreases the number of attempts left with 1, everytime the guess is not correct.
        turns -= 1
        # Print statement to let the player know that their guess is not correct.
        print("\n\tNot correct.")

        # If statement when the player has more than 1 attempt left to guess the right character.
        if turns > 1:
            # Print statement to let the player know of the attempts that are left.
            print("\nYou have", turns, "more guesses.")
        # Elif statement when the player has 1 attempt left to guess the correct character.
        elif turns == 1:
            print("\nYou have only 1 guess left.")

# When the player has zero attempts left to guess the right word and thereby lost the game.
else:
    # Message to encourage the player to try again.
    print("You've lost, try again! You can do it!")
