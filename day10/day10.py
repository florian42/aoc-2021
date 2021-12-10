import pathlib
import statistics
import sys
from typing import List, Deque
from collections import deque


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


def get_completion(line: Deque) -> (list[str], bool):
    expected_closing = []
    while len(line) > 0:
        character = line.popleft()
        if character in pairs.keys():
            expected_closing.append(pairs[character])
        elif expected_closing.pop() != character:
            return expected_closing, True

    return list(reversed(expected_closing)), False


def get_completions(data):
    all_lines = [deque(line) for line in data]
    completions = []
    for line in all_lines:
        completion, is_corrupted = get_completion(line)
        if not is_corrupted:
            completions.append(completion)

    return completions


completion_score_table = {")": 1, "]": 2, "}": 3, ">": 4}


def calculate_completion_score(completions: List[List[str]]):
    totals = []
    for completion in completions:
        score = 0
        for char in completion:
            score *= 5
            score += completion_score_table[char]
        totals.append(score)
    return totals


def part2(data):
    """Solve part 2"""
    completions = get_completions(data)
    scores = calculate_completion_score(completions)
    sorted_scores = sorted(scores)
    return statistics.median(sorted_scores)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    # assert solution1 == 344193
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
