# This is a simple number guessing game where the user has to guess a number between 1 and 10.
# The program generates a random number and checks if the user's guess is correct.

# Importing the random module to generate a random number
# The random module provides functions to generate random numbers.
# It is a built-in module in Python, so no installation is required.
# The `randint` function generates a random integer between the specified range (inclusive).

import random

number_to_guess = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number_to_guess:
    print("Correct! You guessed it!")
else:
    print(f"Wrong! The number was {number_to_guess}")
