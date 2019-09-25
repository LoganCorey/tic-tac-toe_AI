from Players.Player import Player
from Utils.Move import Move


class Human(Player):
    def __init__(self, mark: str):
        Player.__init__(self, mark)

    def make_move(self):
        row = int(input("Which row? ")) - 1
        column = int(input("Which column? ")) - 1
        return Move(row, column, self)

    def __repr__(self):
        return "Human({})".format(self.mark)
