# Import the playsound function from the playsound module
from playsound import playsound

# Import the time module
import time

# Define two string constants to clear the terminal window and move cursor
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Define a function called alarm that takes one argument: seconds
def alarm(seconds):
    # Initialize a variable to keep track of elapsed time
    time_elapsed = 0
    
    # Clear the terminal window
    print(CLEAR)
    
    # Keep looping until the elapsed time is less than the input seconds
    while time_elapsed < seconds:
        # Pause the program for 1 second
        time.sleep(1)
        
        # Increase the time_elapsed by 1 second
        time_elapsed += 1
        
        # Calculate the remaining time
        time_left = seconds - time_elapsed
        
        # Convert the remaining time to minutes and seconds
        minutes_left = time_left // 60 
        seconds_left = time_left % 60
        
        # Display the countdown in the terminal in the format "mm:ss"
        print(f"{CLEAR_AND_RETURN}Countdown to alarm in: {minutes_left:02d}:{seconds_left:02d}")
        
    # Play the alarm sound file
    playsound("alarm.mp3")


# Ask the user to input the number of minutes to wait
minutes = int(input("How many minutes to wait: "))

# Ask the user to input the number of seconds to wait
seconds = int(input("How many seconds to wait: "))

# Calculate the total seconds to wait
total_seconds = minutes * 60 + seconds

# Call the alarm function with the total_seconds as the argument
alarm(total_seconds)
