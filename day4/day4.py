from __future__ import annotations
from typing import List


class BingoBoard:
    def __init__(self, rows: List[List[int]]):
        grid = {}
        for row_index, row in enumerate(rows):
            for column, number in enumerate(row):
                grid[(row_index, column)] = number
        self.grid = grid
        self.grid_as_list = rows

    def __eq__(self, other: BingoBoard):
        return str(self) == str(other)

    def __repr__(self):
        return "".join("".join([str(x) for x in row]) for row in self.grid_as_list)

    def __str__(self):
        return "\n".join("".join([str(x) for x in row]) for row in self.grid_as_list)

    @classmethod
    def from_string(cls, board: str) -> BingoBoard:
        rows = [
            [int(number) for number in row if number != " "]
            for row in board.splitlines()
        ]
        return BingoBoard(rows)
