""" This is a Player of the Tic Tac Toe Game """


class Player:
    """ A Player that can interact with the Tic Tac Toe Game """

    def __init__(self, name):
        self.name = name
        """ Name of the Player """

        self.points = 0
        """ Points of the Player, that can be acquired by winning a Game """

        self.fields = []
        """ stores all Fields the Player has picked """

    def add_point(self):
        """ gives the Player a Point """
        self.points += 1

    def pick_field(self, field):
        """ adds a specific Field to the Player """
        self.fields.append(field)

    def won(self):
        print(self.name, "has won the Game.")
