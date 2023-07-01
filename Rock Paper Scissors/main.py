""" Game for Rock Paper Scissors """
# Importing random to let the PC pick a Random Choice
from random import choices

# Importing os to be able to clear the Console
import os


# Function to clear the Console
def cls():
    """ clear the Console """
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to specify the Winner
def generate_winner(u_pick, bot_pick):
    """ Checks if the Player lost or won, restarts game on Draw """

    # small Dictionary for the possible Win-Conditions
    # Remember first Position is called Key, second Position is called Value
    # "Key" : "Value"
    possible = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }

    # clearing the Console before posting the Result
    cls()

    # if the PC-pick matches the  "Value" of the User_Pick "Key"
    # the User wins, if User and PC picked the same it's a Draw
    # else the PC wins
    if possible[u_pick] == bot_pick:
        return "LOSE"
    if u_pick == bot_pick:
        return "DRAW"

    return "WIN"


# Choices for the User
possible_choices = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

# creating user_pick with no Value
USER_PICK = None

# This will loop the Game until the User use 0 as an Input
while True:

    # This Try and Except will catch every Error if a User use other Inputs than 0 - 3
    try:

        # Get the User-Input and writing some Instructions to the Console
        USER_PICK = int(input(("""
Welcome to my short Rock, Paper, Scissors Game

Please enter a Number between 1 or 3

0 = Quit Game

1 = Rock
2 = Paper
3 = Scissors

Your Pick: """)))

        # If the User picks 0, this will break the Loop and end the Game
        if USER_PICK == 0:
            break

        # if the User enters a Number above 3, we will also raise a ValueError
        if USER_PICK > 3 or USER_PICK < 0:
            raise ValueError

        # if the User picks something from 1 to 3 we will translate his Number into his Choice like
        # Rock, Paper or Scissors
        USER_PICK = possible_choices[USER_PICK - 1]

        # Here we get a Random Choice from the PC
        pc_pick = choices(possible_choices)[0]

        # printing the Results of the Match and starting a new Round
        print(f"""
{generate_winner(USER_PICK, pc_pick)} 
You picked:\t {USER_PICK}
PC picked: \t {pc_pick}
""")

        # This will force the Player to press Enter before starting the Loop from the Beginning
        input("Press Enter to start a new Game.")
        cls()

    # This will be printed if the User makes a wrong Input
    except ValueError:
        cls()
        print("You have to pick a Number between 0 and 3")
