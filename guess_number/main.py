# importing random to generate the Random Number
from random import *

# defining a Class for the Game
class GuessingGame:

    # initialize the Game with the Max-Number defined by the User
    # Max-Number means the Game picks a random Number between 1 and Max-Number
    # Example: Max-Number is 50 the Game generates a random Number from 1 to 50
    def __init__(self, max):

        # here we generate the random Number
        self.pc_number = randint(1, max)
        
        # initialize the Amount of possible Guesses with 0
        self.guesses = 0

        # aking the User how many Guesses he want and saving it
        # this Type of While Loop helps me to be 100% sure the User enters a Number
        while True:
            try:
                self.max_guesses = int(input("How many Guesses do you want? "))
                break
            except ValueError:
                print("Please use only Numbers.")
                continue

    # in this Function the User can Guess a Number and it will get checked if the User guessed correctly or not
    def guess(self):

        # this Part of the Program should be obvious
        # we get the Guess from the User-Input
        # checking it if it is a Number
        # then we respond depending on the result
        # if it is not a Number, we ask again for an Input
        # we only increase the Number of Guesses if it really was a Number
        while True:

            try:
                my_guess = int(input("Please enter your Guess: "))

                self.guesses += 1

                if my_guess == self.pc_number:
                    print(f"Congats, you have found the Number after {self.guesses}/{self.max_guesses} Guesses.")
                    return False

                elif my_guess > self.pc_number:
                    print(f"Your Number was too high. You have used {self.guesses}/{self.max_guesses} Guesses.")
                    return True

                elif my_guess < self.pc_number:
                    print(f"Your Number was too small. You have used {self.guesses}/{self.max_guesses} Guesses.")
                    return True

            except:
                print("Please use only Numbers.")
                continue

# First we ask the User for the Max-Number
# we create the Game-Class with that given Max-Number
# this Loop also ensures that the User enters a real Number
while True:
    try:
        Game = GuessingGame(int(input("I want to play a Game from 1 to ")))
        break
    except ValueError:
        print("Please use only Numbers.")
        continue

# This is the Main-Loop of the Game
# This Loop runs as long as the User has Guesses left or he guessed the correct Number
while Game.guesses < Game.max_guesses:
    if not Game.guess():
        break

# if the User did not Guess the Number we will let him know what the Number was
if Game.guesses == Game.max_guesses:
    print(f"The Number was {Game.pc_number}")