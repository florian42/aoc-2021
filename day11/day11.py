from __future__ import annotations

import pathlib
import sys
from typing import List


def parse(puzzle_input):
    """Parse input"""
    pass


def part1(data):
    """Solve part 1"""
    pass


class DumboOctopus:
    def __init__(self, value, column, row, neighbours: List[DumboOctopus]):
        self.value = value
        self.column = column
        self.row = row
        self.neigbours = neighbours
        self.flashed = False

    def step(self):
        self.value += 1
        if self.value >= 9:
            self.flash()

    def flash(self):
        if not self.flashed:
            for neighbour in self.neigbours:
                neighbour.step()
            self.flashed = True


def part2(data):
    """Solve part 2"""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
