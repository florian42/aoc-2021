from .day1 import count_increases, count_increases_with_sliding_window


class TestCountIncreases:
    def test_counts_increases(self):
        measurements = [193, 195, 204, 208, 219, 230, 231, 233, 234]
        increases_count = count_increases(measurements)

        assert increases_count == len(measurements) - 1

    def test_counts_increases_with_decreases(self):
        measurements = [2223, 2225, 2229, 2231, 2228, 2229, 2230]
        increases_count = count_increases(measurements)

        assert increases_count == 5


class TestCountIncreasesWithSlidingWindow:
    def test_counts_increases_with_decreases(self):
        measurements = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263,
        ]
        increases_count = count_increases_with_sliding_window(measurements)

        assert increases_count == 5
