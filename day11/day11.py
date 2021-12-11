from __future__ import annotations

import pathlib
import sys
from copy import deepcopy
from typing import List, Dict, Tuple, Optional


def parse(puzzle_input) -> Dict[Tuple[int, int], DumboOctopus]:
    # sourcery skip: simplify-numeric-comparison
    """Parse input"""
    lines = puzzle_input.splitlines()
    row_count = len(lines)
    column_count = len(lines[0])
    dumb_octopuses: Dict[Tuple[int, int], DumboOctopus] = {}
    for row, line in enumerate(lines):
        for column, num in enumerate(line):
            dumb_octopuses[(row, column)] = DumboOctopus(int(num))
    for row_index in range(row_count):
        for column in range(column_count):
            neighbours = []
            if row_index > 0:  # top
                neighbours.append(dumb_octopuses[(row_index - 1, column)])
            if row_index + 1 < row_count:  # down
                neighbours.append(dumb_octopuses[(row_index + 1, column)])
            if column - 1 >= 0:  # left
                neighbours.append(dumb_octopuses[(row_index, column - 1)])
            if column + 1 < column_count:  # right
                neighbours.append(dumb_octopuses[(row_index, column + 1)])
            if row_index - 1 >= 0 and column - 1 >= 0:  # diagonal top left
                neighbours.append(dumb_octopuses[(row_index - 1, column - 1)])
            if row_index - 1 >= 0 and column + 1 < column_count:  # diagonal top right
                neighbours.append(dumb_octopuses[(row_index - 1, column + 1)])
            if row_index + 1 < row_count and column - 1 >= 0:  # diagonal bottom left
                neighbours.append(dumb_octopuses[(row_index + 1, column - 1)])
            if (
                row_index + 1 < row_count and column + 1 < column_count
            ):  # diagonal bottom right
                neighbours.append(dumb_octopuses[(row_index + 1, column + 1)])

            current_octopus = dumb_octopuses[(row_index, column)]
            current_octopus.neigbours = neighbours

    return dumb_octopuses


class DumboOctopus:
    def __init__(
        self,
        value: int,
        neighbours: Optional[List[DumboOctopus]] = None,
    ):
        self.value = value
        self.neigbours = neighbours or []
        self.flashed = False

    def step(self):
        self.value += 1

    def flash(self):
        if self.flashed:
            raise Exception("Trying to flash twice in the same step?")
        self.flashed = True
        for nbr in self.neigbours:
            nbr.step()

    def __repr__(self):
        return f"{self.value}"


def get_next_flashing_octo(dumbos: Dict[Tuple[int, int], DumboOctopus]):
    for _, dumbo in dumbos.items():
        if dumbo.value > 9 and not dumbo.flashed:
            yield dumbo


def part1(dumbos: Dict[Tuple[int, int], DumboOctopus], steps=100):
    """Solve part 1"""
    total_flash = 0
    sync_flashing = -1
    for step in range(steps):
        step_flashes = 0
        for _, current in dumbos.items():
            current.step()
        next_flash = next(get_next_flashing_octo(dumbos), None)
        while next_flash:
            next_flash.flash()
            total_flash += 1
            step_flashes += 1
            next_flash = next(get_next_flashing_octo(dumbos), None)
        if step_flashes == len(dumbos.items()):
            sync_flashing = step
        for _, current in dumbos.items():
            if current.flashed:
                current.flashed = False
                current.value = 0

    return total_flash, dumbos, sync_flashing


def part2(dumbos: Dict[Tuple[int, int], DumboOctopus]):
    step = 1
    sync_flashing = part1(dumbos, 1)
    while sync_flashing[2] < 0:
        sync_flashing = part1(dumbos, 1)
        step += 1
    return step


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1, _, _ = part1(deepcopy(data))
    solution2 = part2(deepcopy(data))

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
