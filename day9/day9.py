import pathlib
import sys
from functools import reduce
from typing import List, Tuple


def parse(puzzle_input):
    """Parse input"""
    return [[int(num) for num in line] for line in puzzle_input.split("\n")]


def part1(data: List[List[int]]):
    """Solve part 1"""
    low_points, _ = find_local_minima(data)
    return reduce(lambda x, y: x + 1 + y, low_points) + 1


def find_local_minima(data):
    size = len(data), len(data[0])
    low_points = []
    low_points_pos = []
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
                low_points_pos.append((index_row, index_column))
    return low_points, low_points_pos


def find_nbrs(point, length, width):
    nbrs = []
    if point[0] > 0:
        nbrs.append((point[0] - 1, point[1]))
    if point[0] < length - 1:
        nbrs.append((point[0] + 1, point[1]))
    if point[1] > 0:
        nbrs.append((point[0], point[1] - 1))
    if point[1] < width - 1:
        nbrs.append((point[0], point[1] + 1))
    return nbrs


def dfs(grid, point: Tuple[int, int], length, width):
    gradient = 0
    value = grid[point]
    grid[point] = -1
    for row, column in find_nbrs(point, length, width):
        if grid[(row, column)] == -1:
            continue
        if grid[(row, column)] > value and grid[(row, column)] != 9:
            gradient += dfs(grid, (row, column), length, width) + 1
    return gradient


def convert_to_grid(data: List[List[int]]):
    grid = {}
    for index, row in enumerate(data):
        for index_column, column in enumerate(row):
            grid[(index, index_column)] = column
    return grid


def part2(data):
    length = len(data)
    width = len(data[0])
    basins = []
    _, low_points = find_local_minima(data)
    grid = convert_to_grid(data)
    for row, column in low_points:
        basins.append(dfs(grid, (row, column), length, width) + 1)
    mult = 1
    for basin in sorted(basins)[-3:]:
        mult *= basin
    return mult


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
