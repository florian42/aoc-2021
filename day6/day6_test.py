from day6 import part1


class TestDay1:
    def test_part1_returns_same_list_as_example(self):
        example = [
            6,
            0,
            6,
            4,
            5,
            6,
            0,
            1,
            1,
            2,
            6,
            0,
            1,
            1,
            1,
            2,
            2,
            3,
            3,
            4,
            6,
            7,
            8,
            8,
            8,
            8,
        ]

        assert part1([3, 4, 3, 1, 2]) == example
