from typing import List


def count_increases(measurements: List[int]) -> int:
    return sum(
        previous_entry < next_entry
        for previous_entry, next_entry in zip(measurements, measurements[1:])
    )


def count_increases_with_sliding_window(measurements: List[int]) -> int:
    windows = list(zip(measurements, measurements[1:], measurements[2:]))
    return sum(
        sum(previous_entry) < sum(next_entry)
        for previous_entry, next_entry in zip(windows, windows[1:])
    )


if __name__ == "__main__":
    with open("input.txt", "r") as infile:
        print(count_increases_with_sliding_window([int(line) for line in infile]))
