"""
Hangman Game

This program will simulate the game of hangman.  It will generate a random word from
the wonderwords python generator.  It will take input from the user,
tell the user if the input was correct or incorrect, and keep track of the number
of guesses remaining. It will also display a hangman picture based on the number
of incorrect guesses. The program will end when the user has guessed all the
letters in the word or when they run out of guesses.

Word generation functionality powered by wonderwords
Library: wonderwords
URL: https://pypi.org/project/wonderwords/
Documentation: https://wonderwords.readthedocs.io/

Author: Nathan Muldowney
Date: March 7th, 2026
"""

import random
from wonderwords import RandomWord

#WonderWords generator for the whole program
word_generator = RandomWord()

# Representations for the game state
hangman_pics = [
    """
     +---+
     |   |
     |    
     |    
     |    
     |    
    =========
    """,
    """
     +---+
     |   |
     |   O
     |    
     |    
     |    
    =========
    """,
    """
     +---+
     |   |
     |   O
     |   |
     |    
     |    
    =========
    """,
    """
     +---+
     |   |
     |   O
     |  /|
     |    
     |    
    =========
    """,
    """
     +---+
     |   |
     |   O
     |  /|\\
     |    
     |    
    =========
    """,
    """
     +---+
     |   |
     |   O
     |  /|\\
     |  / 
     |    
    =========
    """,
    """
     +---+
     |   |
     |   O
     |  /|\\
     |  / \\
     |    
    =========
    """,
    """
     +---+
     |   |
     |   X
     |  /|\\
     |  / \\
     |    
    =========
    """
]


def get_random_word():
    """
    Generates and returns one random word from WonderWords
    between 5 and 9 letters long.

    Returns:
    Random word
    """
    valid_word = False
    chosen_word = ""

    while not valid_word:
        target_length = random.randint(5, 9)
        chosen_word = word_generator.word(word_min_length=target_length,word_max_length=target_length).lower()

        if chosen_word.isalpha():
            valid_word = True

    return chosen_word


def create_hidden_word(word):
    """
    Creates a list of underscores to represent the letters
    in the secret word that have not been guessed yet.

    Parameter:
    word: The secret word the player is trying to guess.

    Returns:
    An amount of underscores with the same length as the word.
    """
    hidden = []
    for letter in word:
        hidden.append("_")
    return hidden


def display_game_state(hidden_word, guessed_letters, wrong_guesses):
    """
    Displays the current state of the game, including the hangman picture,
    the hidden word with guessed letters filled in, the letters already guessed,
    and the number of guesses remaining.

    Parameters:
    hidden_word: The current visible version of the word.
    guessed_letters: The letters the player has already guessed.
    wrong_guesses: The number of incorrect guesses so far.
    """
    print(hangman_pics[wrong_guesses])
    print("Your fate is sealed within the word: " + " ".join(hidden_word))
    print("Letters you have previously wagered: " + ", ".join(guessed_letters))
    print("Chances left before your demise:", 7 - wrong_guesses)
    print()


def get_guess(guessed_letters):
    """
    Asks the player to enter one letter. Keeps asking until the player enters
    a valid single letter that has not already been guessed.

    Parameter:
    guessed_letters: The letters the player has already guessed.

    Returns:
    A valid guessed letter.
    """
    guess = input("What letter will you wager against death? ").lower()

    while len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
        if guess in guessed_letters:
            print("Try again, you have already wagered that letter.")
        else:
            print("In order to tempt your fate, please enter a new letter.")
        guess = input("Spin the wheel of fate, enter a letter: ").lower()

    return guess


def update_hidden_word(word, hidden_word, guess):
    """
    Checks to see if the guessed letter is in the secret word.
    Then replaces the matching underscores
    in the hidden word with the guessed letter if correct.

    Parameters:
    word: The secret word
    hidden_word: The current visible version of the word
    guess: The player's guessed letter

    Returns:
    True if the guessed letter is in the word, False if guess is wrong
    """
    found_letter = False

    for index in range(len(word)):
        if word[index] == guess:
            hidden_word[index] = guess
            found_letter = True

    return found_letter


def is_word_guessed(hidden_word):
    """
    Checks whether the entire word has been guessed. If there are no underscores
    left, the word is complete.

    Parameter:
    hidden_word: The current visible version of the word

    Returns:
    True if the word has been fully solved, False if puzzle is not solved
    """
    return "_" not in hidden_word


def play_round(player_name):
    """
    Plays one full round of Hangman using a randomly generated word.
    The round continues until the player either guesses the word
    or reaches 7 incorrect guesses.

    Parameters:
    player_name: The name entered by the player

    Returns:
    True if the player wins the round, False if the player loses
    """
    word = get_random_word()
    hidden_word = create_hidden_word(word)
    guessed_letters = []
    wrong_guesses = 0

    while wrong_guesses < 7 and not is_word_guessed(hidden_word):
        display_game_state(hidden_word, guessed_letters, wrong_guesses)
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        correct_guess = update_hidden_word(word, hidden_word, guess)

        if not correct_guess:
            wrong_guesses += 1

    display_game_state(hidden_word, guessed_letters, wrong_guesses)

    if is_word_guessed(hidden_word):
        print("For this round, the gallows stand empty.")
        print(player_name + ", you have outsmarted death, and for now, your fate remains your own.")
        print("The hidden word you uncovered was:", word)
        print("On this occasion, death leaves empty-handed.")
        return True
    else:
        print(player_name + ", even your superior wit couldn't outsmart death. Your fate is sealed.")
        print("The hidden word that led you to ruin was:", word)
        print("Thus, you meet your end beneath the gallows.")
        return False


def play_game():
    """
    Starts the Hangman game, greets the player,
    and allows the player to keep playing new rounds
    until they choose to stop.
    """
    print()
    print()
    print("                   Welcome to Hangman!")
    print()
    print("Enter at your own peril, for this is a game of Life and Death")
    print()
    print()
    player_name = input("Who now stands before the gallows? ")
    print()
    print("A word of great mystery lies hidden before you!")
    print("Its secret must be revealed one letter at a time.")
    print("Every error will draw you closer to your demise!")
    print("Your reckoning begins now,", player_name + "!")
    print()

    play_again = "y"

    while play_again == "y":
        play_round(player_name)
        print()
        play_again = input("Do you wish to tempt your fate once again? (y/n): ").lower()

        while play_again != "y" and play_again != "n":
            play_again = input("Please enter y or n: ").lower()

    print("Thanks for playing!")


play_game()