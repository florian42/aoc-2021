import pathlib
import sys
from functools import reduce
from typing import List


def parse(puzzle_input):
    """Parse input"""
    return [[int(num) for num in line] for line in puzzle_input.split("\n")]


def part1(data: List[List[int]]):
    """Solve part 1"""
    size = len(data), len(data[0])
    low_points = []
    for index_row in range(size[0]):
        for index_column in range(size[1]):
            top = data[index_row - 1][index_column] if index_row > 0 else float("inf")
            down = (
                data[index_row + 1][index_column]
                if index_row + 1 < size[0]
                else float("inf")
            )
            left = (
                data[index_row][index_column - 1] if index_column > 0 else float("inf")
            )
            right = (
                data[index_row][index_column + 1]
                if index_column < size[1] - 1
                else float("inf")
            )
            neighbours = [top, right, down, left]
            current = data[index_row][index_column]
            if current < min(neighbours):
                low_points.append(current)
    return reduce(lambda x, y: x + 1 + y, low_points) + 1


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
