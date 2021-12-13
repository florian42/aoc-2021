import pathlib
import sys
import numpy as np
from parse import parse


def parse_input(puzzle_input):
    """Parse input"""
    folds = [
        parse("fold along {coor}={:d}", line)
        for line in puzzle_input.splitlines()
        if "fold" in line
    ]
    len_x = None
    len_y = None
    points = []
    for y, x in [
        line.split(",")
        for line in puzzle_input.splitlines()
        if "fold" not in line and len(line) > 1
    ]:
        x = int(x)
        y = int(y)
        if len_y is None:
            len_y = y
        if len_x is None:
            len_x = x
        len_x = max(len_x, x)
        len_y = max(len_y, y)
        points.append((x, y))

    grid = np.zeros((len_x + 1, len_y + 1))

    for x, y in points:
        if grid[x][y] == 0:
            grid[x][y] = 1

    return grid, folds


def part1(grid, folds):
    """Solve part 1"""
    fold = folds[0]
    if fold["coor"] == "x":
        back = grid[:, : fold.fixed[0]].copy()
        front = grid[:, fold.fixed[0] + 1 :].copy()
        folded: np.ndarray = np.fliplr(front) + back
        return np.count_nonzero(folded)
    if fold["coor"] == "y":
        back = grid[: fold.fixed[0], :].copy()
        front = grid[fold.fixed[0] + 1 :, :].copy()
        folded = np.flipud(front) + back
        return np.count_nonzero(folded)
    assert False


def fold_grid(grid, fold):
    if fold["coor"] == "x":
        back = grid[:, : fold.fixed[0]].copy()
        front = grid[:, fold.fixed[0] + 1 :].copy()
        folded: np.ndarray = np.fliplr(front) + back
        return folded
    if fold["coor"] == "y":
        back = grid[: fold.fixed[0], :].copy()
        front = grid[fold.fixed[0] + 1 :, :].copy()
        folded = np.flipud(front) + back
        return folded


def part2(grid, folds):
    """Solve part 2"""
    folded = grid.copy()
    for fold in folds:
        folded = fold_grid(folded, fold)
    return "\n".join(map(lambda row: "".join(row), np.where(folded == 0, " ", "#")))


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    grid, folds = parse_input(puzzle_input)
    solution1 = part1(grid, folds)
    solution2 = part2(grid, folds)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
