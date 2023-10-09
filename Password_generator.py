import random  # Import the random module to enable random selection of characters.
import string  # Import the string module to gain access to ASCII characters.

# Define a function named generate_password with parameters for minimum length, numbers, and special characters.
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters  # Create a variable holding all ASCII letters (both lowercase and uppercase). 
    #! ^these hold alphabet letter in lower and upper cases
    digits = string.digits  # Create a variable holding all digits (0 through 9).
    special = string.punctuation  # Create a variable holding all special characters.

    # Start with a character set that includes only ASCII letters. 
    # This is just our letters for now as an initial container
    
    characters = letters  
    
    # If numbers should be included, add digits to the character container.
    if numbers:
        characters += digits  
    
    # If special characters should be included, add them to the character container.
    if special_characters:
        characters += special  

    # Initialize variables: pwd to store the password, and flag variables to check if the password meets criteria.
    pwd = ""  # Initialize a variable to store the generated password.
    meets_criteria = False  # Flag to check if the generated password meets the criteria.
    has_number = False  # Flag to check if the password contains a number.
    has_special = False  # Flag to check if the password contains a special character.

    # Loop until the password meets the criteria and is at least min_length characters long.
    while not meets_criteria or len(pwd) < min_length:  
        new_char = random.choice(characters)  # Select a random character from the characters set.
        pwd += new_char  # Add the new character to the password string.
        
        # If the new character is a digit, set has_number to True.
        if new_char in digits:  
            has_number = True  
        # If the new character is a special character, set has_special to True.
        elif new_char in special:  
            has_special = True  
        
        # Assume that the password now meets the criteria.
        meets_criteria = True  
        # If numbers are required but none have been added to pwd yet, 
        # set meets_criteria back to False.
        if numbers:  
            meets_criteria = has_number 
        # If special characters are required but none added to pwd yet, 
        # adjust meets_criteria to False.
        if special_characters:  
            meets_criteria = meets_criteria and has_special  

    # Return the generated password.
    return pwd  
    

# Collect user inputs for minimum length, numbers, and special characters.
min_length = int(input("Enter the minimum length: "))  
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"  #sets to true if y or Y is pressed
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"  #sets to true if y or Y is pressed
# Generate the password and print it.
pwd = generate_password(min_length, has_number, has_special)          
print("The generated password is:", pwd)  
