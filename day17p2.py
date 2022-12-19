
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

# part 2
# detect cycle with hash key if relative rock offsets for a new rock, relative jet index, and relative rock index
# cycle was so fast, didn't need the virtual size

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
    jetQueueConsumed = 0

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
        jetQueueConsumed = jetQueueConsumed + 1

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

    return jetQueueConsumed


class coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def findXPos(rockGrid, virtualSize, x):
    for i in range(rockGrid.__len__()).__reversed__():
        if (rockGrid[i][x] == 1):
            return str(rockGrid.__len__() - i)
    return None


def day17p2(file):

    jetQueue = []
    rockQueue = [1, 2, 3, 4, 5]
    rockGrid = []
    rockGrid.append([1] * 7)

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            for char in line:
                jetQueue.append(char)

    jetQueueLen = jetQueue.__len__()

    jetQueueConsumed = 0
    rocksConsumed = 0
    cycleAt = 0
    virtualSize = 0

    cycleIndexes = {}
    cycleKey = None
    cycleI = None

    for i in range(1000000000000):

        if (i % 10000) == 0:
            print(i)

        index = findXPos(rockGrid, virtualSize, 0) + "," + \
            findXPos(rockGrid, virtualSize, 1) + "," + \
            findXPos(rockGrid, virtualSize, 2) + "," + \
            findXPos(rockGrid, virtualSize, 3) + "," + \
            findXPos(rockGrid, virtualSize, 4) + "," + \
            findXPos(rockGrid, virtualSize, 5) + "," + \
            findXPos(rockGrid, virtualSize, 6) + "," + \
            str(jetQueueConsumed) + "," + str(rocksConsumed)
        if index in cycleIndexes.keys():
            cycleKey = index
            cycleI = i
            break
        else:
            cycleIndexes[index] = (rockGrid.__len__() + virtualSize, i)

        j = simulate(rockGrid, jetQueue, rockQueue)
        jetQueueConsumed = jetQueueConsumed + j
        rocksConsumed = rocksConsumed + 1
        if (rockGrid.__len__() > 100):
            virtualSize = virtualSize + 1
            rockGrid.pop(0)

        jetQueueConsumed = jetQueueConsumed % jetQueueLen
        if rocksConsumed % 5 == 0:
            rocksConsumed = 0

    currentSize = virtualSize + rockGrid.__len__() - 1
    cycleStart, cycleIStart = cycleIndexes[cycleKey]
    iterationsInCycle = cycleI - cycleIStart

    sizeOfCycle = currentSize - cycleStart + 1
    toMath = 1000000000000 - cycleI
    multipler = int(toMath / iterationsInCycle)
    remainder = toMath % iterationsInCycle

    result = currentSize + sizeOfCycle * (multipler)
    base = rockGrid.__len__()

    virtualSize3 = 0
    for i in range(remainder):
        simulate(rockGrid, jetQueue, rockQueue)
        if (rockGrid.__len__() > 100):
            virtualSize3 = virtualSize3 + 1
            rockGrid.pop(0)

    result = result + (rockGrid.__len__() + virtualSize3 - base)

    print(result)
    return result


if __name__ == '__main__':
    day17p2("day17input.txt")
