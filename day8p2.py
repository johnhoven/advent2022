def scenicScore(list, rowSize, lines, index):

    row = int(index / rowSize)
    col = int(index % rowSize)

    # Edges
    # if row == 0 or col == 0 or row == lines - 1 or col == rowSize - 1:
    #    return True

    height = list[index]

    # Visible from left

    scoreL = 0
    for i in range(col).__reversed__():
        scoreL = scoreL + 1
        if list[row * rowSize + i] >= height:
            break

    # Visible from right
    scoreR = 0
    for i in range(col + 1, rowSize):
        scoreR = scoreR + 1
        if list[row * rowSize + i] >= height:
            break

    # visible from top
    scoreT = 0
    for i in range(row).__reversed__():
        scoreT = scoreT + 1
        if list[i * rowSize + col] >= height:
            break

    # visible from bottom
    scoreB = 0
    for i in range(row + 1, lines):
        scoreB = scoreB + 1
        if list[i * rowSize + col] >= height:
            break

    return scoreL * scoreR * scoreT * scoreB


def day8p2(file):

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

    maxScore = 0
    for i in range(list.__len__()):
        tmp = scenicScore(list, rowSize, lines, i)
        if (tmp > maxScore):
            maxScore = tmp

    print(maxScore)
    return maxScore


if __name__ == '__main__':
    day8p2("day8input.txt")
