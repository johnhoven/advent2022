def isValid(sub):
    a = sub[0]
    b = sub[1]
    c = sub[2]
    d = sub[3]
    if a == b or a == c or a == d or b == c or b == d or c == d:
        return False
    return True


def day6p1(file):

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            for i in range(line.__len__()):
                if i < 3:
                    continue
                sub = line[i-3:i+1]
                if isValid(sub):
                    print(i + 1)
                    return i + 1

    print(-1)
    return -1


if __name__ == '__main__':
    day6p1("day6input.txt")
