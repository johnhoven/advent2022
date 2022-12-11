
def day10p1(file):

    regX = 1
    cycles = 0
    dict = {}

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            if line[0:4] == "addx":
                _addx, V = line.split(' ')

                cycles = cycles + 1
                dict[cycles] = regX

                regX = regX + int(V)
                cycles = cycles + 1

            else:
                cycles = cycles + 1

            dict[cycles] = regX

    result = dict[19] * 20 + dict[59] * 60 + dict[99] * 100 + \
        dict[139] * 140 + dict[179] * 180 + dict[219] * 220
    print(result)
    return result


if __name__ == '__main__':
    day10p1("day10input.txt")
