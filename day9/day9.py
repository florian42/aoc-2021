import pathlib
import sys
from functools import reduce
from typing import List, Dict, Tuple


def parse(puzzle_input):
    """Parse input"""
    return [[int(num) for num in line] for line in puzzle_input.split("\n")]


def part1(data: List[List[int]]):
    """Solve part 1"""
    low_points = find_local_minima(data)
    return reduce(lambda x, y: x + 1 + y, low_points) + 1


def find_local_minima(data):
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
    return low_points


def find_horizontal_gradient(
    point: Tuple[int, int], grid: Dict[Tuple[int, int], int], length: int
):
    current_point_value = grid[point]
    right = [grid[(point[0], num)] for num in range(point[1] + 1, length)]
    left = list(reversed([grid[(point[0], num)] for num in range(point[1])]))

    right_basin = []
    left_basin = []
    for _ in right:
        neighbour = right.pop(0)
        if neighbour > current_point_value and neighbour != 9:
            right_basin.append(neighbour)

    for _ in left:
        neighbour = left.pop(0)
        if neighbour > current_point_value and neighbour != 9:
            left_basin.append(neighbour)

    return [*right_basin, *left_basin]


def find_vertical_gradient(
    point: Tuple[int, int], grid: Dict[Tuple[int, int], int], height: int
):
    current_point_value = grid[point]
    down = [grid[(num, point[0])] for num in range(point[0] + 1, height)]
    top = list(reversed([grid[(num, point[0])] for num in range(point[0])]))

    down_basin = []
    top_basin = []
    for _ in down:
        neighbour = down.pop(0)
        if neighbour > current_point_value and neighbour != 9:
            down_basin.append(neighbour)

    for _ in down:
        neighbour = top.pop(0)
        if neighbour > current_point_value and neighbour != 9:
            top_basin.append(neighbour)

    return [*down_basin, *top_basin]


def convert_to_grid(data: List[List[int]]):
    grid = {}
    for index, row in enumerate(data):
        for index_column, column in enumerate(row):
            grid[(index, index_column)] = column
    return grid


def part2(data: List[List[int]]):
    """Solve part 2"""
    grid = convert_to_grid(data)
    print(grid)
    find_vertical_gradient((2, 2), grid, len(data))


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
