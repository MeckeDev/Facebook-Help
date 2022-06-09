""" This is a Game of Tic Tac Toe """
import Game
import Player


GAME = Game.Game()  # Create a new Game
P1 = Player.Player(input("Please enter a Name for Player1: "))  # ask Player1 for a Name
P2 = Player.Player(input("Please enter a Name for Player2: "))  # ask Player2 for a Name
ROUND = 0  # just a Counter of Rounds to see who is the active Player

# here we start the Game-Loop
while not GAME.win:

    # if the Round-Number is even, Player1 can pick a Field
    # else it is Player2's turn
    if ROUND % 2 == 0:

        # we use an Infinite-Loop until the Player made a correct Input
        while True:

            # asking the Player for an Input
            picked_field = input(f"{P1.name}, please select a Field: ")

            # checking if the Input is valid
            # breaking the Infinite-Loop if Input is correct
            # else asking for new Input
            if GAME.set_field(picked_field, "X", P1):
                break

            # let the Player know his Input was not Valid, before asking for a new Input
            else:
                print(f"{picked_field} is not a Valid Input. Valid is {GAME.not_used_fields}")
    else:

        # same Process as for Player1 above
        while True:
            picked_field = input(f"{P2.name}, please select a Field: ")
            if GAME.set_field(picked_field, "*", P2):
                break
            else:
                print(f"{picked_field} is not a Valid Input. Valid is {GAME.not_used_fields}")

    # adding 1 to ROUND to switch to the other Player
    ROUND += 1
