def contains(x1, x2, y1, y2):

    # scenario 1: pair 1 starts first, pair 1 ends after pair 2 starts
    if x1 <= y1 and x2 >= y1:
        #print(x1, x2, y1, y2)
        return True
    # scenario 2: pair 2 starts first, pair 2 ends after pair 1 starts
    if y1 <= x1 and y2 >= x1:
        return True

    return False


def day4p2(file):

    sum = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            x, y = line.split(',')
            x1, x2 = x.split('-')
            y1, y2 = y.split('-')
            if contains(int(x1), int(x2), int(y1), int(y2)):
                sum = sum + 1

    print(sum)
    return sum


if __name__ == '__main__':
    day4p2("day4input.txt")
