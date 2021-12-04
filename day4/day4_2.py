from __future__ import annotations

from typing import List


class BingoBoard:
    def __init__(self, rows: List[List[int]]):
        self.rows = [[Number(number) for number in rows] for rows in rows]
        self.rows = [row for row in self.rows if len(row) > 1]

    def has_won(self) -> bool:
        for row in self.rows:
            if all(num.isMarked is True for num in row):
                return True
        transposed_rows: List[List[Number]] = list(map(list, zip(*self.rows)))
        for row in transposed_rows:
            if all(num.isMarked is True for num in row):
                return True

    def mark(self, num_to_mark: int):
        for row in self.rows:
            for num in row:
                if num.number == num_to_mark:
                    num.isMarked = True

    def __eq__(self, other: object):
        return str(self) == str(other)

    def __repr__(self):
        return "".join("".join([str(x) for x in row]) for row in self.rows)

    def __str__(self):
        return "\n".join(", ".join([str(x) for x in row]) for row in self.rows)

    def __hash__(self):
        return hash(repr(self))


class Number:
    def __init__(self, num: int):
        self.number = num
        self.isMarked = False

    def __repr__(self):
        return f"[{self.number} {self.isMarked}], "

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.number + other.number)
        return self.number + other

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.number - other.number)
        return self.number - other

    def __hash__(self):
        return hash(repr(self))


def calc_score(board, number):
    total = 0
    for row in board.rows:
        for num in row:
            if num.isMarked is False:
                total += num.number
    return total * number


def play(all_marked_numbers: List[int], boards: List[BingoBoard]):
    number_of_boards = len(boards)
    winner = None
    looser = None
    for number in all_marked_numbers:
        for board in boards:
            board.mark(number)
            if board.has_won() and number_of_boards == len(boards):
                winner = board, number
            if board.has_won() and len(boards) == 1:
                looser = board, number
            if board.has_won():
                boards.remove(board)

    return winner, looser


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
