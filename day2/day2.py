class UnknownDirectionError(Exception):
    pass


class Submarine:
    def __init__(self, horizontal_position=0, depth=0):
        self.horizontal_position = horizontal_position
        self.depth = depth

    def _forward(self, steps: int):
        self.horizontal_position += steps

    def _backwards(self, steps: int):
        self.horizontal_position -= steps

    def _up(self, steps: int):
        self.depth -= steps

    def _down(self, steps: int):
        self.depth += steps

    def move(self, direction: str, steps: int):
        if direction == "forward":
            self._forward(steps)
        elif direction == "backwards":
            self._backwards(steps)
        elif direction == "up":
            self._up(steps)
        elif direction == "down":
            self._down(steps)
        else:
            raise UnknownDirectionError(direction)


class SubmarineWithAim(Submarine):
    def __init__(self, horizontal_position=0, depth=0, aim=0):
        super().__init__(horizontal_position, depth)
        self.aim = aim

    def _forward(self, steps: int):
        self.horizontal_position += steps
        self.depth += self.aim * steps

    def _backwards(self, steps: int):
        self.horizontal_position -= steps
        self.depth -= self.aim * steps

    def _up(self, steps: int):
        self.aim -= steps

    def _down(self, steps: int):
        self.aim += steps


def main(file_path="input.txt"):
    with open(file_path, "r") as infile:
        submarine = SubmarineWithAim()
        for line in infile:
            movement, steps = line.strip().split(" ")
            if movement.startswith("_"):
                movement = movement[1:]
            submarine.move(movement, int(steps))
        return submarine.depth * submarine.horizontal_position


if __name__ == "__main__":
    print(main())
