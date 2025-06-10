
# Guessing Game - Shannon Murdock, IT112


"""
Create an object for the computer to generate a random number.  
The randint subclass will generate a number from 1 through 100 (inclusive).
"""

import random

def validate_input(user_input):
    try:
        num = int(user_input)
        if 1 <= num <= 100:
            return True, num
        else:
            print("Please enter a number between 1 and 100.")
            return False, None
    except ValueError:
        print("Please enter a valid number.")
        return False, None

# Generate random number
secret_number = random.randint(1, 100)
guess = None

# Main game loop
while guess != secret_number:
    # Get user input
    user_input = input("Guess a number between 1 and 100: ")
    
    # Validate input
    valid, guess = validate_input(user_input)
    if not valid:
        continue
    
    # Compare guess with secret number
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Winner! Winner! Chicken Dinner! You guessed the right number!")
