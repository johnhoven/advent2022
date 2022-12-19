
# have a grid of rocks
# Loop 2022 times calling a simulate method
# Get maximum height from grid (top row)

# simulate:
# Get next rock shape and starting positions
# do {
#   process jet flow
#   move down
# } while (!landed)
# update grid of rocks with final positions

def checkCoordsXMove(coords, xChange, grid):
    for coord in coords:
        x = coord.x
        y = coord.y
        xNew = x + xChange
        if xNew < 0:
            return False
        if xNew > 6:
            return False
        if grid.__len__() > y and \
                grid[y][xNew] == 1:
            return False
    return True


def checkCoordsYMove(coords, grid):
    for coord in coords:
        x = coord.x
        y = coord.y
        yNew = y - 1

        if grid.__len__() > yNew and \
                grid[yNew][x] == 1:
            return False
    return True


def moveCoords(coords, xChange, yChange):
    for coord in coords:
        coord.x = coord.x + xChange
        coord.y = coord.y + yChange


def updateGrid(rockGrid, coords):
    for coord in coords:
        x = coord.x
        y = coord.y

        while rockGrid.__len__() <= y:
            rockGrid.append([0] * 7)

        rockGrid[y][x] = 1


def simulate(rockGrid, jetQueue, rockQueue):
    rockShape = rockQueue.pop(0)
    rockQueue.append(rockShape)

    startingYPos = rockGrid.__len__() + 3
    if rockShape == 1:
        coords = [
            (2, startingYPos),
            (3, startingYPos),
            (4, startingYPos),
            (5, startingYPos)
        ]
    elif rockShape == 2:
        coords = [(3, startingYPos + 2),
                  (2, startingYPos + 1), (3, startingYPos + 1), (4, startingYPos + 1),
                  (3, startingYPos)
                  ]
    elif rockShape == 3:
        coords = [
            (4, startingYPos + 2),
            (4, startingYPos + 1),
            (2, startingYPos), (3, startingYPos), (4, startingYPos)
        ]
    elif rockShape == 4:
        coords = [
            (2, startingYPos + 3),
            (2, startingYPos + 2),
            (2, startingYPos + 1),
            (2, startingYPos)
        ]
    else:
        coords = [
            (2, startingYPos + 1), (3, startingYPos + 1),
            (2, startingYPos), (3, startingYPos)
        ]

    # lazy change of type for above
    coords = list(map(lambda c:  coordinate(c[0], c[1]), coords))

    landed = False
    while landed == False:
        # process jet flow
        jet = jetQueue.pop(0)
        jetQueue.append(jet)

        if (jet == "<"):
            # move left
            if (checkCoordsXMove(coords, -1, rockGrid)):
                moveCoords(coords, -1, 0)
        else:
            # move right
            if (checkCoordsXMove(coords, 1, rockGrid)):
                moveCoords(coords, 1, 0)

        # move rocks down
        if (not checkCoordsYMove(coords, rockGrid)):
            landed = True
        else:
            moveCoords(coords, 0, -1)

    # update grid
    updateGrid(rockGrid, coords)


class coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def mapForPrint(x):
    if x == 1:
        return '#'
    return '.'


def printGrid(rockGrid):
    buffer = ""
    for i in range(0, rockGrid.__len__() - 1).__reversed__():
        buffer = buffer + ','.join(map(mapForPrint, rockGrid[i])) + '\n'

    with open('day17p1.print.txt', 'w') as f:
        f.write(buffer)


def day17p1(file):

    jetQueue = []
    rockQueue = [1, 2, 3, 4, 5]
    rockGrid = []
    rockGrid.append([1] * 7)

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            for char in line:
                jetQueue.append(char)
    print(jetQueue.__len__())

    for i in range(2022):
        simulate(rockGrid, jetQueue, rockQueue)

    result = rockGrid.__len__() - 1  # remove one for rock floor
    print(result)
    printGrid(rockGrid)
    return result


if __name__ == '__main__':
    day17p1("day17input.txt")
