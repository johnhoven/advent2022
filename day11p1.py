
def day11p1(file):

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

    result = 0
    print(result)
    return result


if __name__ == '__main__':
    day11p1("day11input.txt")
