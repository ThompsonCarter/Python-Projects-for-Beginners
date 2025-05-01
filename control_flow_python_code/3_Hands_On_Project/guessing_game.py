import random

# Step 1: Generate a random number
number_to_guess = random.randint(1, 100)

# Step 2: Initialize the user's guess
guess = None

# Step 3: Give the user instructions
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100. Try to guess it!")

# Step 4: Start the loop
while guess != number_to_guess:
    # Step 4.1: Get the user's guess
    guess = int(input("Enter your guess: "))
    
    # Step 4.2: Provide feedback based on the guess
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
