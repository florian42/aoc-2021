import pathlib
import sys
from copy import deepcopy
from typing import List, Optional


def parse(puzzle_input):
    """Parse input"""
    lines = puzzle_input.split("\n")
    signal_pattern = [line.split(" | ")[0].split() for line in lines]
    output_value = [line.split(" | ")[1].split() for line in lines]
    return signal_pattern, output_value


unique_segments_numbers = [2, 4, 3, 7]  # 1,4,7,8


def part1(output_values: List[str]) -> int:
    """Solve part 1"""
    # [... for inner_list in outer_list for item in inner_list]
    return len(
        [
            output
            for outputs in output_values
            for output in outputs
            if len(output) in unique_segments_numbers
        ]
    )


def contains_only_1(one: Optional[str], pattern: str):
    if not one:
        return False
    if one[0] in pattern and one[1] in pattern:
        return False
    if one[0] in pattern:
        return one[0]
    if one[1] in pattern:
        return one[1]


def contains_both(one: Optional[str], pattern: str):
    if not one:
        return False
    return one[0] in pattern and one[1] in pattern


def contains_all_chars(pattern, other):
    if other is None:
        return False
    set_a = set(pattern)
    set_b = set(other)
    return len(set_a - set_b) == 1


def part2(list_of_signal_patterns: List[List[str]], output_value):
    """Solve part 2"""
    mapping = {}
    char_in_one = None
    search = deepcopy(list_of_signal_patterns[0])
    for _ in range(4):
        for pattern in search:
            match len(pattern):
                case 2:
                    mapping[1] = pattern
                    search.remove(pattern)
                case 4:
                    mapping[4] = pattern
                    search.remove(pattern)
                case 3:
                    mapping[7] = pattern
                    search.remove(pattern)
                case 7:
                    mapping[8] = pattern
                    search.remove(pattern)
                case 6:
                    contains_one = contains_only_1(mapping.get(1), pattern)
                    if contains_one:
                        char_in_one = contains_one
                        mapping[6] = pattern
                        search.remove(pattern)
                    elif contains_all_chars(pattern, mapping.get(5)):
                        mapping[9] = pattern
                        search.remove(pattern)
                case 5:
                    if contains_both(mapping.get(1), pattern):
                        mapping[3] = pattern
                        search.remove(pattern)
                    elif char_in_one and char_in_one in pattern:
                        mapping[5] = pattern
                        search.remove(pattern)
    for num in search:
        match len(num):
            case 5:
                mapping[2] = num
                search.remove(num)
            case 6:
                mapping[0] = num
                search.remove(num)
    print(mapping)
    numbers = []
    for num in output_value[0]:
        for item in mapping.items():
            if contains_all_chars(num, item[1]):
                numbers.append(item[0])
    print(numbers)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    signal_pattern, output_value = parse(puzzle_input)
    solution1 = part1(output_value)
    solution2 = part2(signal_pattern, output_value)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
