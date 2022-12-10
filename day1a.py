def day1(file):

    runningSum = 0
    maxSum = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                if runningSum > maxSum:
                    maxSum = runningSum
                runningSum = 0
            else:
                runningSum += int(line)

    if runningSum > maxSum:
        maxSum = runningSum

    print(maxSum)
    return maxSum


if __name__ == '__main__':
    day1("day1a-input.txt")
