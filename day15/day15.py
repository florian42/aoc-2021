import heapq
import pathlib
import sys
from collections import defaultdict
from math import inf
from colorama import init, Style, Fore
from collections import deque


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
    parents = {}

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
                parents[neighbor] = current_node
        visited.add(current_node)

    return costs[destination], parents


def part1(grid):
    """Solve part 1"""
    return dijkstra(grid)


def part2(grid):
    """Solve part 2"""
    tile_width = len(grid)
    tile_height = len(grid[0])
    for _ in range(4):
        for row in grid:
            tail = row[-tile_width:]
            row.extend((x + 1) if x < 9 else 1 for x in tail)
    for _ in range(4):
        for row in grid[-tile_height:]:
            row = [(x + 1) if x < 9 else 1 for x in row]
            grid.append(row)
    return dijkstra(grid)


def print_grid(grid, path):
    width = len(grid)
    height = len(grid[0])
    for row_index in range(height):
        row = ""
        for column in range(width):
            is_colored = (row_index, column) in path
            if is_colored:
                row += f"{Style.NORMAL}{grid[row_index][column]} {Style.DIM}"
            else:
                row += f"{Style.DIM}{grid[row_index][column]} "
        print(row)
        row = ""


def get_shortest_path(parents, grid):
    next = parents[(len(grid) - 1, len(grid[0]) - 1)]
    path = deque([])
    while next:
        path.appendleft(next)
        next = parents.get(next)
    path.append((len(grid) - 1, len(grid[0]) - 1))
    return list(path)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    grid = parse(puzzle_input)
    solution1, parents = part1(grid)
    solution2, parents = part2(grid)
    shortest_path = get_shortest_path(parents, grid)
    print_grid(grid, shortest_path)

    return solution1, solution2


if __name__ == "__main__":
    init()
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
