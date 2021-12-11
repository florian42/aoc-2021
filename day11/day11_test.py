import pathlib

from day11.day11 import parse, part1


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


class TestDumboOctopus:
    def test_step1(self):
        puzzle_input = pathlib.Path("test_input").read_text().strip()
        dumbos = parse(puzzle_input)

        flashes, actual_dumbos = part1(dumbos, steps=1)

        result = [str(value.value) for key, value in actual_dumbos.items()]

        expected_result = """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""

        assert result == flatten([list(line) for line in expected_result.splitlines()])

    def test_step2(self):
        puzzle_input = pathlib.Path("test_input").read_text().strip()
        dumbos = parse(puzzle_input)

        flashes, actual_dumbos = part1(dumbos, steps=2)

        result = [str(value.value) for key, value in actual_dumbos.items()]

        expected_result = """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""

        assert result == flatten([list(line) for line in expected_result.splitlines()])

    def test_step3(self):
        puzzle_input = pathlib.Path("test_input").read_text().strip()
        dumbos = parse(puzzle_input)

        flashes, actual_dumbos = part1(dumbos, steps=3)

        result = [str(value.value) for key, value in actual_dumbos.items()]

        expected_result = """0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000"""

        assert result == flatten([list(line) for line in expected_result.splitlines()])

    def test_step10(self):
        puzzle_input = pathlib.Path("test_input").read_text().strip()
        dumbos = parse(puzzle_input)

        flashes, actual_dumbos = part1(dumbos, steps=10)

        result = [str(value.value) for key, value in actual_dumbos.items()]

        expected_result = """0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000"""

        assert result == flatten([list(line) for line in expected_result.splitlines()])

        assert flashes == 204
