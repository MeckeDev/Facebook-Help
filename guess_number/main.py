""" Guess a Number Game // not the best to solve this with a Class """
# importing random to generate the Random Number
import sys
from random import randint


# defining a Class for the Game
class GuessingGame:
    """ Class for the Game, containing the Random Number and the Guesses """

    # initialize the Game with the Max-Number defined by the User
    # Max-Number means the Game picks a random Number between 1 and Max-Number
    # Example: Max-Number is 50 the Game generates a random Number from 1 to 50
    def __init__(self, max_number):

        # here we generate the random Number
        self.pc_number = randint(1, max_number)

        # initialize the Amount of possible Guesses with 0
        self.guesses = 0

        # asking the User how many Guesses he wants and saving it
        # this Type of While Loop helps me to be 100% sure the User enters a Number
        while True:
            try:
                self.max_guesses = int(input("How many Guesses do you want? "))
                break
            except ValueError:
                print("Please use only Numbers.")
                continue

    # in this Function the User can Guess a Number,
    # and it will get checked if the User guessed correctly
    def guess(self):
        """ Check if the guessed Number was correct, smaller or bigger """

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
                    print(f"Congrats, you have found the Number after "
                          f"{self.guesses}/{self.max_guesses} Guesses.")
                    return False

                if my_guess > self.pc_number:
                    print(f"Your Number was too high. You have used "
                          f"{self.guesses}/{self.max_guesses} Guesses.")
                    return True

                if my_guess < self.pc_number:
                    print(f"Your Number was too small. You have used "
                          f"{self.guesses}/{self.max_guesses} Guesses.")
                    return True

            except ValueError:
                print("Please use only Numbers.")
                continue


# initialize a Default Number
GAME = 0

# First we ask the User for the Max-Number
# we create the Game-Class with that given Max-Number
# this Loop also ensures that the User enters a real Number
while True:
    try:
        GAME = GuessingGame(int(input("I want to play a Game from 1 to ")))
        break
    except ValueError:
        print("Please use only Numbers greater than 0.")
        continue

if not GAME:
    sys.exit(1)
# This is the Main-Loop of the Game
# This Loop runs as long as the User has Guesses left, or he guessed the correct Number
while GAME.guesses < GAME.max_guesses:
    if not GAME.guess():
        break

# if the User did not Guess the Number we will let him know what the Number was
if GAME.guesses == GAME.max_guesses:
    print(f"The Number was {GAME.pc_number}")
