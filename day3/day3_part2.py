import collections


def reduce_report(diagnostic_report, maximum, pref):
    index = 0
    while len(diagnostic_report) > 1:
        transposed_diagnostic_report = list(map(list, zip(*diagnostic_report)))
        counts = tuple(
            collections.Counter(transposed_diagnostic_report[index]).most_common()
        )
        gamma = counts[0]
        epsilon = counts[-1]
        if gamma[1] == epsilon[1]:
            diagnostic_report = [
                reading for reading in diagnostic_report if reading[index] == pref
            ]
        elif maximum:
            diagnostic_report = [
                reading for reading in diagnostic_report if reading[index] == gamma[0]
            ]
        else:
            diagnostic_report = [
                reading for reading in diagnostic_report if reading[index] == epsilon[0]
            ]
        if len(diagnostic_report) == 1:
            return "".join(diagnostic_report[0])
        index += 1


def main(file_path="input.txt"):
    with open(file_path, "r") as infile:
        diagnostic_report = [list(line.strip()) for line in infile]
        ox = reduce_report(diagnostic_report[:], True, "1")
        print(ox)
        co2 = reduce_report(diagnostic_report[:], False, "0")
        print(co2)

        print(int(ox, 2) * int(co2, 2))


if __name__ == "__main__":
    print(main())
