import collections


def main(file_path="input.txt"):
    with open(file_path, "r") as infile:
        diagnostic_report = [list(line.strip()) for line in infile]
        transposed_diagnostic_report = list(map(list, zip(*diagnostic_report)))
        gamma_rate, epsilon_rate = ("", "")

        for column in transposed_diagnostic_report:
            most_common, least_common = tuple(collections.Counter(column).most_common())
            gamma_rate += most_common[0]
            epsilon_rate += least_common[0]

        print(gamma_rate, epsilon_rate, int(gamma_rate, 2) * int(epsilon_rate, 2))


if __name__ == "__main__":
    print(main())
