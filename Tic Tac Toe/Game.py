""" This is a Game of Tic Tac Toe """
import os


def cls():
    """ Clears the Console """
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    """ creates a new Game of Tic tac Toe with an empty Field and default Values """

    def __init__(self):
        self.possible_wins = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 5, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [3, 5, 7]
        ]
        """ Contains all possible Win-Conditions """

        self.current_game = """
# ##### # ##### # ##### #
#       #       #       #
#   1   #   2   #   3   #
#       #       #       #
# ##### # ##### # ##### #
#       #       #       #
#   4   #   5   #   6   #
#       #       #       #
# ##### # ##### # ##### #
#       #       #       #
#   7   #   8   #   9   #
#       #       #       #
# ##### # ##### # ##### #
"""
        """ Visual representation of the current Game """

        self.not_used_fields = list(range(1, 10))
        """ stores all Fields that were not taken by a Player """

        self.win = False
        """ Flag that triggers the Win to end the Game """

    def draw_game(self):
        """ Clears the Console and displays the current Game """
        cls()
        print(self.current_game)

    def set_field(self, field, symbol, player):
        """ Assigns a specific Field to a User, returns False if Field was already taken

        field
            needs a Number of an available Field

        symbol
            is the Symbol that identifies the current Player
        """
        if field in self.current_game:
            self.current_game = self.current_game.replace(field, symbol)
            self.not_used_fields.remove(int(field))
            print(self.not_used_fields)
            player.fields.append(int(field))
            self.check_win(player)
            return True
        return False

    def check_win(self, player):
        """ checks the current Game, for a possible Winner """
        self.draw_game()
        for win in self.possible_wins:
            if set(win).issubset(set(player.fields)):
                player.won()
                self.win = True
                return
        if len(self.not_used_fields) == 0:
            print("That is a Draw, nobody has won.")
            self.win = True
