from random import *

class GuessingGame:

    def __init__(self, max):

        self.pc_number = randint(1, max)
        self.guesses = 0

        while True:
            try:
                self.max_guesses = int(input("How many Guesses do you want? "))
                break
            except ValueError:
                print("Please use only Numbers.")
                continue

    def guess(self):

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

while True:
    try:
        Game = GuessingGame(int(input("I want to play a Game from 1 to ")))
        break
    except ValueError:
        print("Please use only Numbers.")
        continue


while Game.guesses < Game.max_guesses:
    if not Game.guess():
        break
