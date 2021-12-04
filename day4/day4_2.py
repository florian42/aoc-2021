from __future__ import annotations

from copy import deepcopy
from typing import List, Tuple


class BingoBoard:
    def __init__(self, rows: List[List[int]]):
        self.rows = [[Number(number) for number in rows] for rows in rows]

    def has_won(self) -> bool:
        for row in self.rows:
            if all(num.isMarked is True for num in row):
                return True
        transposed_rows: List[List[Number]] = list(map(list, zip(*self.rows)))
        return any(all(num.isMarked is True for num in row) for row in transposed_rows)

    def mark(self, num_to_mark: int):
        for row in self.rows:
            for num in row:
                if num.number == num_to_mark:
                    num.isMarked = True

    def __eq__(self, other: object):
        if isinstance(other, BingoBoard):
            for row_index, row in enumerate(self.rows):
                for column_index, num in enumerate(row):
                    other_number = other.rows[row_index][column_index]
                    if num.number != other_number.number:
                        return False
            return True
        return False

    def __repr__(self):
        return "".join("".join([str(x) for x in row]) for row in self.rows)

    def __str__(self):
        return "\n".join(", ".join([str(x) for x in row]) for row in self.rows)


class Number:
    def __init__(self, num: int):
        self.number = num
        self.isMarked = False

    def __repr__(self):
        return f"[{self.number} {self.isMarked}], "


def calc_score(board, number):
    total = 0
    for row in board.rows:
        for num in row:
            if num.isMarked is False:
                total += num.number
    return total * number


def is_in_winning_list(winners: List[Tuple[BingoBoard, int]], other: BingoBoard):
    if not winners:
        return False
    return any(board == other for board, _ in winners)


def play(
    all_marked_numbers: List[int], boards: List[BingoBoard]
) -> tuple[tuple[BingoBoard, int], tuple[BingoBoard, int]]:
    winners: List[Tuple[BingoBoard, int]] = []
    for number in all_marked_numbers:
        for board in boards:
            board.mark(number)
            if board.has_won():
                in_list = is_in_winning_list(winners, board)
                if not in_list:
                    winners.append((deepcopy(board), number))

    return winners[0], winners[-1]


if __name__ == "__main__":
    content = open("input.txt").read().split("\n\n")

    all_marked_numbers = list(map(int, content[0].split(",")))
    boards = [
        BingoBoard([list(map(int, line.split())) for line in board.split("\n")])
        for board in content[1:]
    ]

    winner, looser = play(all_marked_numbers, boards)

    print(calc_score(winner[0], winner[1]))
    print(calc_score(looser[0], looser[1]))
