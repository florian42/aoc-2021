import itertools
import pathlib
import sys
from collections import defaultdict, Counter
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


def step(polymer: str, pairs: Dict[str, str], steps=1):
    pair_frequencies = Counter()
    char_frequencies = Counter()
    for pair in itertools.pairwise(polymer):
        pair_frequencies[pair[0] + pair[1]] += 1
    for _ in range(steps):
        pair_frequencies_step = Counter()
        for pair, frequency in pair_frequencies.items():
            if pair in pairs:
                pair_frequencies_step[pair[0] + pairs[pair]] += frequency
                pair_frequencies_step[pairs[pair] + pair[1]] += frequency
                char_frequencies[pairs[pair]] += frequency
        pair_frequencies = pair_frequencies_step
    ranking = char_frequencies.most_common()
    return (ranking[0][1] - ranking[-1][1]) + 1


def part1(polymer: str, pairs: Dict[str, str]):
    """Solve part 1"""
    return step(polymer, pairs, 10)


def part2(polymer: str, pairs: Dict[str, str]):
    """Solve part 2"""
    return step(polymer, pairs, 40)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(*data)
    solution2 = part2(*data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
