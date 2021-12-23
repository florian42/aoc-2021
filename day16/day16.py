import pathlib
import sys

from bitstream import Bitstream


def binary_format(puzzle_input, length):
    integer = int(puzzle_input, 16)
    return f"{integer:0>{length}b}"


def sum_versions(packet):
    version, type_id, data = packet

    if type_id == 4:
        return version

    return version + sum(map(sum_versions, data))


def parse(puzzle_input):
    """Parse input"""
    return binary_format(puzzle_input.splitlines()[0], 24)


def part1(data):
    """Solve part 1"""
    stream = Bitstream(data)
    result = stream.decode_one_packet()
    return sum_versions(result)


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
