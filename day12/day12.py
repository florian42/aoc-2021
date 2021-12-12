import pathlib
import sys
from collections import defaultdict
from typing import Set


def parse(puzzle_input):
    """Parse input"""
    adjacency_matrix = defaultdict(list)
    for line in puzzle_input.splitlines():
        node_a, node_b = line.split("-")
        adjacency_matrix[node_a].append(node_b)
        adjacency_matrix[node_b].append(node_a)
    return adjacency_matrix


def bfs(current: str, adjacency_matrix, visited: Set[str]):
    if current == "end":
        return 1
    if current.islower() and current in visited:
        return 0
    visited = visited | {current}  # Union both sets to create a new set for this path
    return sum(
        bfs(node, adjacency_matrix, visited) for node in adjacency_matrix[current]
    )


def part1(adjacency_matrix):
    """Solve part 1"""
    return bfs("start", adjacency_matrix, set())


def bfs_single_small_cave_twice(
    current: str, adjacency_matrix, visited: Set[str], small_cave
):
    if current == "end":
        return 1
    if current == "start" and visited:
        return 0
    if current.islower() and current in visited:
        if small_cave is None:
            small_cave = current
        else:
            return 0
    visited = visited | {current}
    return sum(
        bfs_single_small_cave_twice(node, adjacency_matrix, visited, small_cave)
        for node in adjacency_matrix[current]
    )


def part2(adjacency_matrix):
    """Solve part 2"""
    return bfs_single_small_cave_twice("start", adjacency_matrix, set(), None)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    adjacency_matrix = parse(puzzle_input)
    solution1 = part1(adjacency_matrix)
    solution2 = part2(adjacency_matrix)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
