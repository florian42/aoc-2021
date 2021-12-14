import pathlib
import sys
from collections import defaultdict
from typing import Dict


def parse(puzzle_input):
    """Parse input"""
    lines = puzzle_input.splitlines()
    polymer = lines[0]
    pairs = defaultdict(None)
    for pair in lines[2:]:
        match, char = pair.split(" -> ")
        pairs[match] = char
    return polymer, pairs


def insert_pair(polymer: str, pair: str, pairs: Dict[str, str]):
    if pair in polymer:
        index = polymer.index(pair)
        start = polymer[: index + 1]
        end = polymer[index + 1 :]
        return start + pairs[pair] + end


def part1(data):
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
