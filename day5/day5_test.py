from day5.day5 import CoordinateSystem


class TestCoordinateSystem:
    def test_get_points_09_59(self):
        xy = CoordinateSystem()
        result = xy.get_points((0, 9), (5, 9))

        assert result == [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]

    def test_get_points_80_08(self):
        xy = CoordinateSystem()
        result = xy.get_points((8, 0), (0, 8))

        assert result == [
            (8, 0),
            (7, 1),
            (6, 2),
            (5, 3),
            (4, 4),
            (3, 5),
            (2, 6),
            (1, 7),
            (0, 8),
        ]

    def test_get_points_94_34(self):
        xy = CoordinateSystem()
        result = xy.get_points((5, 5), (8, 2))

        assert result == [(5, 5), (6, 4), (7, 3), (8, 2)]
