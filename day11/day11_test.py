from day11.day11 import DumboOctopus
from day2.day2_test import Builder


class TestDumboOctopus:
    def test_does_not_flash_when_already_flashed(self):
        initial_value = 2
        neighbours = [
            DumboOctopus(initial_value, 0, 1, []),
            DumboOctopus(initial_value, 1, 0, []),
        ]
        octopus = DumboOctopus(1, 0, 0, neighbours)
        octopus.flashed = True

        octopus.flash()

        for neighbour in neighbours:
            assert neighbour.value == initial_value
            assert neighbour.flashed is False

    def test_step_increases_value(self):
        initial_value = 1
        octopus = DumboOctopus(initial_value, 0, 0, [])

        octopus.step()

        assert octopus.value == initial_value + 1

    def test_octopus_with_energy_level_gte_nine_flashes(self):
        octopus = DumboOctopus(Builder.build_random_int(minimum=9), 0, 0, [])

        octopus.step()

        assert octopus.flashed is True

    def test_flashing_octopus_increases_energy_level_of_adjacent_octopuses(self):
        initial_value = 2
        neighbours = [
            DumboOctopus(initial_value, 0, 1, []),
            DumboOctopus(initial_value, 1, 0, []),
        ]
        octopus = DumboOctopus(9, 0, 0, neighbours)

        octopus.flash()

        for neighbour in neighbours:
            assert neighbour.value == initial_value + 1
            assert neighbour.flashed is False

    def test_when_octopus_flashes_neighbours_can_flash_too(self):
        initial_value = 8
        neighbours = [
            DumboOctopus(initial_value, 0, 1, []),
            DumboOctopus(initial_value, 1, 0, []),
        ]
        octopus = DumboOctopus(8, 0, 0, neighbours)

        octopus.step()

        for neighbour in neighbours:
            assert neighbour.value == initial_value + 1
            assert neighbour.flashed is True
