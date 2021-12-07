import pathlib
import statistics
import sys
from math import ceil, floor


def parse(puzzle_input):
    """Parse input"""
    return [int(num) for num in puzzle_input.split(",")]


def distance(crab: int, target_position: int) -> int:
    return abs(target_position - crab)


def part1(data):
    """Solve part 1"""
    cheapest_move = ceil(statistics.median(data))
    return sum(distance(crab, cheapest_move) for crab in data)


def distance_with_little_gauss(crab: int, target_position: int) -> int:
    step = abs(target_position - crab)
    return ((step ** 2) + step) / 2


def part2(data) -> int:
    """Solve part 2
    As each crab moves, moving further becomes more expensive.
    This changes the best horizontal position to align them all on.
    in the example above, this becomes 5.
    """
    cheapest_move = statistics.mean(data)
    down = sum(distance_with_little_gauss(crab, floor(cheapest_move)) for crab in data)
    up = sum(distance_with_little_gauss(crab, ceil(cheapest_move)) for crab in data)
    return min(down, up)


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
