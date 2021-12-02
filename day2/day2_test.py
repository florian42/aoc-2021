import random

from day2.day2 import Submarine, main, SubmarineWithAim


class TestSubmarine:
    def test_forward_increases_horizontal_position(self):
        initial_position = Builder.build_random_int()
        submarine = Submarine(horizontal_position=initial_position)
        steps = Builder.build_random_int()

        submarine.move("forward", steps)

        assert submarine.horizontal_position == initial_position + steps

    def test_backwards_increases_horizontal_position(self):
        initial_position = Builder.build_random_int()
        submarine = Submarine(horizontal_position=initial_position)
        steps = Builder.build_random_int()

        submarine.move("backwards", steps)

        assert submarine.horizontal_position == initial_position - steps

    def test_up_decreases_depth(self):
        initial_position = Builder.build_random_int()
        submarine = Submarine(depth=initial_position)
        steps = Builder.build_random_int()

        submarine.move("up", steps)

        assert submarine.depth == initial_position - steps

    def test_up_increases_depth(self):
        initial_position = Builder.build_random_int()
        submarine = Submarine(depth=initial_position)
        steps = Builder.build_random_int()

        submarine.move("down", steps)

        assert submarine.depth == initial_position + steps

    def test_example(self):
        assert main("test_input.txt") == 150


class TestSubmarineWithAim:
    def test_forward_increases_horizontal_position_and_depth(self):
        initial_position = Builder.build_random_int()
        initial_depth = Builder.build_random_int()
        initial_aim = Builder.build_random_int()
        submarine = SubmarineWithAim(
            depth=initial_depth, horizontal_position=initial_position, aim=initial_aim
        )
        steps = Builder.build_random_int()

        submarine.move("forward", steps)

        assert submarine.horizontal_position == initial_position + steps
        assert submarine.depth == initial_depth + (initial_aim * steps)

    def test_backwards_increases_horizontal_position(self):
        initial_position = Builder.build_random_int()
        initial_depth = Builder.build_random_int()
        initial_aim = Builder.build_random_int()
        submarine = SubmarineWithAim(
            depth=initial_depth, horizontal_position=initial_position, aim=initial_aim
        )
        steps = Builder.build_random_int()

        submarine.move("backwards", steps)

        assert submarine.horizontal_position == initial_position - steps
        assert submarine.depth == initial_depth - (initial_aim * steps)

    def test_up_decreases_aim(self):
        aim = Builder.build_random_int()
        submarine = SubmarineWithAim(aim=aim)
        steps = Builder.build_random_int()
        submarine.move("up", steps)

        assert submarine.aim == aim - steps

    def test_down_increases_aim(self):
        aim = Builder.build_random_int()
        submarine = SubmarineWithAim(aim=aim)
        steps = Builder.build_random_int()
        submarine.move("down", steps)

        assert submarine.aim == aim + steps

    def test_example(self):
        assert main("test_input.txt") == 900


class Builder:
    @classmethod
    def build_random_int(cls, minimum=0, maximum=100):
        return random.randint(minimum, maximum)
