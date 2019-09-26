from Players.Player import Player
from Utils.Move import Move
import neat
from random import randint
def convert_to_input(number: int) -> int:
    """
    Since there are 3 rows and 3 columns
    an input can be converted by multiplying the result by 3 and rounding
    :param number:
    :return:
    """
    if number < 0:
        return 0
    return int(round(number * 3, 1)) - 1


class AI(Player):
    def __init__(self, mark: str, net, config, board=None):
        self.net = net
        self.config = config
        self.board = board

        Player.__init__(self, mark)

    def make_move(self):
        # output gives a number between 0 and 0.5
        # Takes a list of floats
        # Can loop through each move and add them together
        # I can represent this board as a list of 1's and 2's
        # 1s for ai and 2s for opponents
        # There needs to be 9 inputs

        output = self.net.activate(self.board.encode_board_state())
        row = convert_to_input(output[0])
        column = convert_to_input(output[1])
        print(row, column)
        print(output)
        return Move(row, column, self)

    def randomize(self):
        valid_moves = self.board.get_valid_moves()
        move_set = valid_moves[randint(0, len(valid_moves))]
        return Move(move_set[0], move_set[1], self)




    def __repr__(self):
        return "Human({})".format(self.mark)
