import heapq
import pathlib
import sys
from collections import defaultdict
from math import inf


def parse(puzzle_input):
    """Parse input"""
    return [list(map(int, row)) for row in puzzle_input.splitlines()]


def neighbors(row_index, column_index, height, width):
    for delta_row, delta_column in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        new_row, new_column = (row_index + delta_row, column_index + delta_column)
        if 0 <= new_row < width and 0 <= new_column < height:
            yield new_row, new_column


def dijkstra(grid):
    height, width = len(grid), len(grid[0])
    start = (0, 0)
    destination = (height - 1, width - 1)
    to_visit = [(0, start)]  # usually contains all the vertices
    costs = defaultdict(lambda: inf, {start: 0})
    visited = set()

    while to_visit:
        cost, current_node = heapq.heappop(
            to_visit
        )  # using priority queue to always select the node with lowest cost next
        if current_node in visited:
            continue

        for neighbor in neighbors(current_node[0], current_node[1], height, width):
            new_cost = cost + grid[neighbor[0]][neighbor[1]]
            if neighbor not in visited and new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(to_visit, (new_cost, neighbor))
        visited.add(current_node)

    return costs[destination]


def part1(grid):
    """Solve part 1"""
    return dijkstra(grid)


def part2(grid):
    """Solve part 2"""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    grid = parse(puzzle_input)
    solution1 = part1(grid)
    solution2 = part2(grid)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
