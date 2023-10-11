# Import the random module to generate random numbers
import random

# Request the user to input a number and store it in the variable top_of_range
top_of_range = input("Type a number: ")

# Check if the input is a digit (i.e., a positive integer)
if top_of_range.isdigit():
    # Convert the string input to an integer
    top_of_range = int(top_of_range)

    # Check if the number is less than or equal to 0
    if top_of_range <= 0:
        # Print an error message and exit the program if the number is not greater than 0
        print('Please type a number larger than 0 next time.')
        quit()
# If the input is not a digit, print an error message and exit the program
else:
    print('Please type a number next time.')
    quit()

# Generate a random number between 0 and top_of_range and store it in the variable random_number
random_number = random.randint(0, top_of_range)
# Initialize a variable to keep track of the number of guesses the user makes
guesses = 0

# Start an infinite loop
while True:
    # Increment the guess count by 1 each time the loop runs
    guesses += 1
    # Request the user to make a guess and store it in the variable user_guess
    user_guess = input("Make a guess: ")
    
    # Check if the user's guess is a digit
    if user_guess.isdigit():
        # Convert the user's guess to an integer if it is a digit
        user_guess = int(user_guess)
    # If the user's guess is not a digit, print an error message and restart the loop
    else:
        print('Please type a number next time.')
        continue  # continue with the next iteration of the loop

    # Check if the user's guess is equal to the random number
    if user_guess == random_number:
        # If the guess is correct, print a success message and exit the loop
        print("You got it!")
        break
    # If the guess is too high, inform the user
    elif user_guess > random_number:
        print("You were above the number!")
    # If the guess is too low, inform the user
    else:
        print("You were below the number!")

# Print the number of guesses it took the user to get the correct number
print("You got it in", guesses, "guesses")
