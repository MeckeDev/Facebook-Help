# Importing random to let the PC pick a Random Choice
import random

# Importing os to be able to clear the Console
import os

# Function to clear the Console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Function to specify the Winner
def generate_winner(user_pick, pc_pick):

    # small Dictionary for the possible Win-Conditions
    # Rembember first Position is called Key, second Position is called Value
    # "Key" : "Value"
    possible = {
        "Rock" : "Paper",
        "Paper" : "Scissors",
        "Scissors" : "Rock"
    }

    # clearing the Console before posting the Result
    cls()

    # if the PC-pick matches the  "Value" of the User_Pick "Key"
    # the User wins, if User and PC picked the same it's a Draw
    # else the PC wins
    if possible[user_pick] == pc_pick:
        return "LOSE"
    elif user_pick == pc_pick:
        return "DRAW"
    else:
        return "WIN"

# Choices for the User
choices = {
    0 : "Rock",
    1 : "Paper",
    2 : "Scissors"
}

# creating user_pick with no Value
user_pick = None

# This will loop the Game unti the User use 0 as an Input
while True:

    # This Try and Except will catch every Error if a User use other Inputs than 0 - 3
    try:

        # Get the User-Input and writing some Instructions to the Console
        user_pick = int(input(("""
Welcome to my short Rock, Paper, Scissors Game

Please enter a Number between 1 or 3

0 = Quit Game

1 = Rock
2 = Paper
3 = Scissors

Your Pick: """)))

        # If the User picks 0, this will break the Loop and end the Game
        if user_pick == 0:
            break

        # if the User picks something from 1 - 3 we will translate his Number into his Choice like
        # Rock, Paper or Scissors
        else:
            user_pick = choices[user_pick-1]            

        # Here we get a Random Choice from the PC
        pc_pick = random.choices(choices)[0]
        
        # printing the Results of the Match and starting a new Round
        print(
f"""
{generate_winner(user_pick, pc_pick)} 
You picked:\t {user_pick}
PC picked: \t {pc_pick}
"""
        )

        # This will force the Player to press Enter before starting the Loop from the Beginning
        input("Press Enter to start a new Game.")
        cls()

    # This will be printed if the User makes a wrong Input
    except:
        print("You have to pick a Number between 0 and 3")