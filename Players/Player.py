"""
Abstract class representing a basic player
"""
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, mark: str):
        self.mark = mark
        super().__init__()

    @abstractmethod
    def make_move(self, row: int, column: int):
        """
        :param row:
        :param column:
        :return:
        """
        pass

    def __repr__(self) -> str:
        return "Player({})".format(self.mark)

    def __eq__(self, other: any):
        if isinstance(other, Player):
            return self.mark == other.mark
