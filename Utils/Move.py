from Players.Player import Player


class Move:
    def __init__(self, row: int, column: int, player: Player):
        """

        """
        self. row = row
        self. column = column
        self.player = player

    def _get_cords(self):
        return self.row, self.column

    def __eq__(self, other: any) -> bool:
        if isinstance(other, Move):
            return (self.row, self.column) == (other.row, other.column)

    def __hash__(self):
        return hash((self.row, self.column))

    def __repr__(self) -> str:
        return "Move({}, {}, {})".format(self.row, self.column, self.player)

