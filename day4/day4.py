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
        return any(all(num.isMarked is True for num in row) for row in transposed_rows)

    def mark(self, num_to_mark: int):
        for row in self.rows:
            for number in row:
                if number.number == num_to_mark:
                    number.isMarked = True

    def __eq__(self, other: object):
        return str(self) == str(other)

    def __repr__(self):
        return "".join("".join([str(x) for x in row]) for row in self.rows)

    def __str__(self):
        return "\n".join(", ".join([str(x) for x in row]) for row in self.rows)


class Number:
    def __init__(self, num: int):
        self.number = num
        self.isMarked = False

    def __repr__(self):
        return f"{self.number}, {self.isMarked}"

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.number + other.number)
        return self.number + other

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.number - other.number)
        return self.number - other


if __name__ == "__main__":
    content = open("input.txt").read().split("\n\n")

    all_marked_numbers = list(map(int, content[0].split(",")))
    boards = [
        BingoBoard([list(map(int, line.split())) for line in board.split("\n")])
        for board in content[1:]
    ]
    is_won = False
    for number in all_marked_numbers:
        if not is_won:
            for board in boards:
                board.mark(number)
                has_won = board.has_won()
                if has_won:
                    is_won = True
                    total = 0
                    for row in board.rows:
                        for num in row:
                            if num.isMarked is False:
                                total += num.number
                    print(total * number)
