def isValid(sub):
    dict = {}
    for v in sub:
        if v in dict.keys():
            return False
        dict[v] = 1
    return True


def day6p2(file):

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            for i in range(line.__len__()):
                if i < 13:
                    continue
                sub = line[i-13:i+1]
                if isValid(sub):
                    print(i + 1)
                    return i + 1

    print(-1)
    return -1


if __name__ == '__main__':
    day6p2("day6input.txt")
