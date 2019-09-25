"""
Python representation of a tic-tac-toe board
"""
from Utils.Move import Move
from typing import List


class InvalidMoveException(Exception):
    """
    Exception is raised if the player makes
    an invalid move
    """


class Board:
    def __init__(self, setup: bool = False, board_state: List[List[int]] = None):
        """
        :param setup: if setup is False then the board wont
        be initialized to a default state
        :param board_state: previous board state
        """
        # either setup board or use previous state
        if setup is True and board_state is None:
            # initialize a fixed 3x3 array
            self.board_state = [[None, None, None] for x in range(0, 3)]
        else:
            self.board_state = board_state

        # board state being won
        self.won = False
        # number of moves recorded
        self.num_moves = 0

    def __str__(self):
        """
        :return: a string representation of the board state
        """
        row = 0
        board = ""
        for count in range(0, 6):
            # draw row ex: x | x | x
            if count % 2 == 0:
                values = []
                for move in self.board_state[row]:
                    if move is None:
                        values.append(" ")
                    else:
                        values.append(move.player.mark)
                board += "{} | {} | {}\n".format(values[0], values[1], values[2])
                row += 1
            else:
                if count is not 5:
                    board += "__|___|__\n"
        board += "  |   |  \n"
        return board

    def get_valid_moves(self):
        """
        Finds every possible move that can be made as a list of tuples of row, column
        :return: a List of every possible move that can be made
        """
        valid_moves = []
        for row in range(0, len(self.board_state)):
            for column in range(0, len(self.board_state[row])):
                if not self.board_state[row][column]:
                    valid_moves.append((row, column))
        return valid_moves

    def get_player_moves(self, player):
        previous_moves = []
        for row in range(0, len(self.board_state)):
            for column in range(0, len(self.board_state[row])):
                if self.board_state[row][column] and self.board_state[row][column].player == player:
                    previous_moves.append((row, column))
        return previous_moves

    def is_valid_move(self, move: Move) -> bool:
        """
        Checks if the move is valid. A  move is not
        valid if a player has already made it or if the
        move is out of board boundary
        :param move: a move the player wishes to make
        :return: true if the move is valid otherwise false
        """
        if not self.board_state[move.row][move.column]:
            return True
        return False

    def move(self, move):
        """
        Applies the players move to the board
        :param move: a move the player wishes to make
        :return: The new board state after applying the move
        """
        if self.is_valid_move(move):
            new_board = self.copy()
            new_board.board_state[move.row][move.column] = move
            return new_board
        else:
            raise InvalidMoveException()

    def is_winning_row(self, move: Move) -> bool:
        """
        Checks if a row contains a winning move after
        the player applies their move
        :param move: a move a player is making
        :return: True if after the move the row is a winning row
        """
        winning_row = True

        # check only for the row
        for previous_move in self.board_state[move.row]:
            # if the move in that spot is not from the player it cannot be a winning row
            # if there has been no move made it cannot be a winning row
            if (previous_move and previous_move.player is not move.player) or not previous_move:
                return False
        return True

    def is_winning_column(self, move: Move) -> bool:
        """
        Checks if a column contains a winning move after
        the player applies their move
        :param move: a move a player is making
        :return: True if after the move the columnis a winning row
        """
        for row in self.board_state:
            if (row[move.column] and row[move.column].player is not move.player) or not row[move.column]:
                return False
        return True

    def is_winning_diagonal(self, move: Move) -> bool:
        top_left = True
        top_right = True
        column = 0
        for row in self.board_state:
            if row[column] and row[column].player == move.player:
                pass
            else:
                top_left = False
            column += 1

        column = 2
        for row in self.board_state:
            if row[column] and row[column].player == move.player:
                pass
            else:
                top_right = False
            column -= 1
        if top_left or top_right:
            return True
        return False

    def check_winning_move(self, move: Move) -> bool:
        """
        """
        if self.is_winning_row(move):
            return True
        elif self.is_winning_column(move):
            return True
        elif self.is_winning_diagonal(move):
            return True
        return False

    def set_won(self) -> bool:
        self.won = True

    def get_won(self) -> bool:
        return self.won

    def copy(self):
        return Board(setup=False, board_state=self.board_state)


