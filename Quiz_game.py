# Print a welcoming message for the user
print("Welcome to my computer quiz!")

# Take user input to check if they want to play the quiz
playing = input("Do you want to play? ")

# Check if the user wants to play by comparing the input with "yes", if not, end the program
if playing.lower() != "yes":
    quit()

# If user wants to play, print a message and initialize the score variable
print("Okay! Let's play :)")
score = 0

# Ask the first question and get user input
answer = input("What does CPU stand for? ")
# Check if the user's answer is correct, if yes, add to the score and print a message
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
# If the answer is incorrect, print a message
else:
    print("Incorrect!")

# Ask the second question and get user input
answer = input("What does GPU stand for? ")
# Check if the user's answer is correct, if yes, add to the score and print a message
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
# If the answer is incorrect, print a message
else:
    print("Incorrect!")

# Ask the third question and get user input
answer = input("What does RAM stand for? ")
# Check if the user's answer is correct, if yes, add to the score and print a message
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
# If the answer is incorrect, print a message
else:
    print("Incorrect!")

# Ask the fourth question and get user input
answer = input("What does PSU stand for? ")
# Check if the user's answer is correct, if yes, add to the score and print a message
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
# If the answer is incorrect, print a message
else:
    print("Incorrect!")

# Print the total score and the percentage of correct answers
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
