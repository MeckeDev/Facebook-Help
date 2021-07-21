# we have to import math in order to use floor()
from math import *

# a while True loop runs forever except it you use break to end the Loop
while True:

    # try helps us to catch any Errors if for Example the user did not enter a Number
    try:

        # Get User Input, throws Error if User don't input a Number
        total_minutes = int(input("""
How many Minutes do you want to convert?
Enter 0 to exit the Program

>>> """))

        # Quits the Program if the User enters a 0
        if total_minutes == 0:
            break

        # Checking how many times the 60 fits into the given Number
        hours = floor(total_minutes/60)

        # calculates the Modulo of the Hours to get the Minutes
        minutes = total_minutes % 60

        # prints the Results to the Console
        print(f"{hours} Hours and {minutes} Minutes")
    
    # this gets called if the User did not enter a Number
    except:

        # lets the User know what he did wrong and starts the Program from the beginning
        print("Please only enter Numbers.")
