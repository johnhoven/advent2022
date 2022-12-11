def isVisible(list, rowSize, lines, index):

    row = int(index / rowSize)
    col = int(index % rowSize)

    # Edges
    if row == 0 or col == 0 or row == lines - 1 or col == rowSize - 1:
        return True

    height = list[index]

    # Visible from left
    allLower = True
    for i in range(col):
        if list[row * rowSize + i] >= height:
            allLower = False
            break

    if allLower == True:
        return True

    # Visible from right
    allLower = True
    for i in range(col + 1, rowSize):
        if list[row * rowSize + i] >= height:
            allLower = False
            break

    if allLower == True:
        return True

    # visible from top
    allLower = True
    for i in range(row):
        if list[i * rowSize + col] >= height:
            allLower = False
            break

    if allLower == True:
        return True

    # visible from bottom
    allLower = True
    for i in range(row + 1, lines):
        if list[i * rowSize + col] >= height:
            allLower = False
            break

    if allLower == True:
        return True
    return False


def day8p1(file):

    list = []
    rowSize = 0
    lines = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            rowSize = line.__len__()
            lines = lines + 1
            for c in line:
                list.append(int(c))

    total = 0
    for i in range(list.__len__()):
        if isVisible(list, rowSize, lines, i):
            total = total + 1

    print(total)
    return total


if __name__ == '__main__':
    day8p1("day8input.txt")
