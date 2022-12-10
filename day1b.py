def day1part2(file):

    runningSum = 0

    l = list()
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                l.append(runningSum)
                runningSum = 0
            else:
                runningSum += int(line)

    if runningSum > 0:
        l.append(runningSum)

    l.sort()
    l.reverse()

    result = l[0] + l[1] + l[2]

    print(result)
    return result


if __name__ == '__main__':
    day1part2("day1a-input.txt")
