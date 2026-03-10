"""
This program will simulate the game of hangman.  It will take input from the user, tell the user if the input was
correct or incorrect, and keep track of the number of guesses remaining.  It will also display a hangman picture
based on the number of incorrect guesses.  The program will end when the user has guessed all the letters in the word
or when they run out of guesses.

Author: Nathan Muldowney
Date: March 7th, 2026
"""

import random


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


word_list = [
    "apple",
    "tiger",
    "planet",
    "bridge",
    "monster",
    "computer",
    "elephant",
    "notebook",
    "dinosaur",
    "football"
]


def get_random_word(words):
    """
    Chooses and returns one random word from the list of possible words.

    Parameter:
    words (list): A list of words the game can choose from.

    Returns:
    A randomly selected word.
    """
    return random.choice(words)


def create_hidden_word(word):
    """
    Creates a list of underscores to represent the letters
    in the secret word that have not been guessed yet.

    Parameter:
        word: The secret word the player is trying to guess.

    Returns:
        list: A list of underscores with the same length as the word.
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
    hidden_word (list): The current visible version of the word.
    guessed_letters (list): The letters the player has already guessed.
    wrong_guesses (int): The number of incorrect guesses made so far.

    Returns:
        None
    """
    print(hangman_pics[wrong_guesses])
    print("Word: " + " ".join(hidden_word))
    print("Guessed letters: " + ", ".join(guessed_letters))
    print("Guesses left:", 7 - wrong_guesses)
    print()


