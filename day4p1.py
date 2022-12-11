def contains(x1, x2, y1, y2):
    if x1 <= y1 and x2 >= y2:
        print(x1, x2, y1, y2)
        return True
    if y1 <= x1 and y2 >= x2:
        print(y1, y2, x1, x2)
        return True
    return False


def day4p1(file):

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
    day4p1("day4input.txt")
