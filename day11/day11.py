from __future__ import annotations

import pathlib
import sys
from typing import List, Dict, Tuple


def parse(puzzle_input) -> Dict[Tuple[int, int], DumboOctopus]:
    # sourcery skip: simplify-numeric-comparison
    """Parse input"""
    lines = puzzle_input.splitlines()
    row_count = len(lines)
    column_count = len(lines[0])
    dumb_octopuses: Dict[Tuple[int, int], DumboOctopus] = {}
    for row, line in enumerate(lines):
        for column, num in enumerate(line):
            dumb_octopuses[(row, column)] = DumboOctopus(num, column, row)
    for row_index in range(row_count):
        for column in range(column_count):
            neighbours = []
            if row_index > 0:  # top
                neighbours.append(dumb_octopuses[(row_index - 1, column)])
            if row_index + 1 < row_count - 1:  # down
                neighbours.append(dumb_octopuses[(row_index + 1, column)])
            if column - 1 > 0:  # left
                neighbours.append(dumb_octopuses[(row_index, column - 1)])
            if column + 1 < column_count - 1:  # right
                neighbours.append(dumb_octopuses[(row_index, column + 1)])
            if row_index - 1 > 0 and column - 1 > 0:  # diagonal top left
                neighbours.append(dumb_octopuses[(row_index - 1, column - 1)])
            if (
                row_index - 1 > 0 and column + 1 < column_count - 1
            ):  # diagonal top right
                neighbours.append(dumb_octopuses[(row_index - 1, column + 1)])
            if row_index + 1 < row_count - 1 and column - 1 > 0:  # diagonal bottom left
                neighbours.append(dumb_octopuses[(row_index + 1, column - 1)])
            if (
                row_index + 1 < row_count - 1 and column + 1 < column_count - 1
            ):  # diagonal bottom right
                neighbours.append(dumb_octopuses[(row_index + 1, column + 1)])

            current_octopus = dumb_octopuses[(row_index, column)]
            current_octopus.neigbours = neighbours

    return dumb_octopuses


class DumboOctopus:
    def __init__(self, value, column, row, neighbours=None):
        self.value = value
        self.column = column
        self.row = row
        self.neigbours = neighbours or []
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

    def __repr__(self):
        return f"({self.row}, {self.column}): {self.value}"


def part1(data: List[List[int]]):
    """Solve part 1"""
    pass


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
