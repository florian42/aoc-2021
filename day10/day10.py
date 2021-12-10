import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_syntax_errors(data):
    all_lines = [list(line) for line in data]
    errors = []
    expected_closing = []
    for line in all_lines:
        for character in line:
            if character in pairs.keys():
                expected_closing.append(pairs[character])
            else:
                expected_closing_char = expected_closing.pop()
                if expected_closing_char != character:
                    errors.append(character)
                    break

    return "".join(errors)


score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}


def calculate_score(syntax_errors: str):
    return sum(score_table[illegal_character] for illegal_character in syntax_errors)


def part1(data):
    """Solve part 1"""
    syntax_errors = get_syntax_errors(data)
    return calculate_score(syntax_errors)


def part2(data):
    """Solve part 2"""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    assert solution1 == 344193
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
