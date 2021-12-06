import pathlib
from collections import Counter


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split(",")]


def one_day(numbers):
    numbers_copy = []
    new_numbers = []
    for number in numbers:
        if number == 0:
            new_numbers.append(8)
            new_num = 6
        else:
            new_num = number - 1
        numbers_copy.append(new_num)
    return [*numbers_copy, *new_numbers]


def part1(numbers, days=80) -> int:
    """Solve part 1"""
    for _ in range(days):
        numbers = one_day(numbers)
    return len(numbers)


def part2(fishes: list[int], days):
    """Solve part 2"""
    fish_counter = Counter(fishes)
    fish_cohorts = [fish_counter[index] for index in range(9)]
    for _ in range(days):
        fish_cohorts.append(fish_cohorts.pop(0))
        fish_cohorts[6] += fish_cohorts[-1]
    return sum(fish_cohorts)


if __name__ == "__main__":
    puzzle_input = pathlib.Path("input").read_text().strip()
    numbers = parse(puzzle_input)
    print(f"Day 6 Part 1: {part1(numbers)}")
    print(f"Day 6 Part 2: {part2(numbers, 256)}")
