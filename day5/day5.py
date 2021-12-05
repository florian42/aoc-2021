from __future__ import annotations

import collections
from typing import List, Tuple

Point = Tuple[int, int]


class CoordinateSystem:
    def __init__(self):
        self.grid = collections.defaultdict(lambda: ".")

    def mark(self, point: Point):
        if self.grid[point] == ".":
            self.grid[point] = "1"
        else:
            self.grid[point] = str(int(self.grid[point]) + 1)

    def get_points(self, start: Point, end: Point) -> List[Tuple[int, int]]:
        x, y = start
        x2, y2 = end
        x_range_start, x_range_end, x_step = self._get_x_range(start, end)
        y_range_start, y_range_end, y_step = self._get_y_range(start, end)
        x_axis = [
            num if x != x2 else x for num in range(x_range_start, x_range_end, x_step)
        ]
        y_axis = [
            num if y != y2 else y for num in range(y_range_start, y_range_end, y_step)
        ]
        return list(zip(x_axis, y_axis))

    def _get_x_range(self, start: Point, end: Point) -> Tuple[int, int, int]:
        if start[0] < end[0]:
            return start[0], end[0] + 1, 1
        if start[0] > end[0]:
            return start[0], end[0] - 1, -1
        return 0, start[0] + abs(end[1] - start[1]) + 1, 1

    def _get_y_range(self, start: Point, end: Point) -> Tuple[int, int, int]:
        if start[1] < end[1]:
            return start[1], end[1] + 1, 1
        if start[1] > end[1]:
            return start[1], end[1] - 1, -1
        return 0, abs(end[0] - start[0]) + 1, 1

    def count_at_least_two_points_overlap(self):
        return len([int(count) for count in self.grid.values() if int(count) >= 2])

    def __repr__(self):
        string = ""
        for row in range(10):
            for column in range(10):
                string += self.grid[(column, row)]
            string += "\n"
        return string


if __name__ == "__main__":
    xy = CoordinateSystem()
    line_input = open("input.txt").read().strip().split("\n")
    for start, end in (line.split(" -> ") for line in line_input):
        x, y = [int(number) for number in start.split(",")]
        x2, y2 = [int(number) for number in end.split(",")]
        for point in xy.get_points((x, y), (x2, y2)):
            # if x == x2 or y == y2: // Part 1 consider only horizontal and vertical
            xy.mark(point)
    print("Part 2:")
    print(xy.count_at_least_two_points_overlap())
