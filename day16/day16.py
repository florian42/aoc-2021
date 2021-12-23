import pathlib
import sys
from math import prod

from day16.bitstream import Bitstream


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
    rawdata = bytes.fromhex(puzzle_input.splitlines()[0])
    return "".join(map("{:08b}".format, rawdata))


def part1(data):
    """Solve part 1"""
    stream = Bitstream(data)
    result = stream.decode_one_packet()
    return sum_versions(result), result


def evaluate_packet(packet):
    _, type_id, data = packet

    if type_id == 4:
        return data

    values = map(evaluate_packet, data)

    match type_id:
        case 0:
            return sum(values)
        case 1:
            return prod(values)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            return int(values[0] > values[1])
        case 6:
            return int(values[0] < values[1])
        case 7:
            return int(values[0] == values[1])
        case _:
            raise Exception("Unknown typeId", type_id)


def part2(result):
    """Solve part 2"""
    return evaluate_packet(result)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1, result = part1(data)
    solution2 = part2(result)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
