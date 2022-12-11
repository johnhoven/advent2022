class knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = {}

    def logVisited(self):
        self.visited[self.x.__str__() + "." + self.y.__str__()] = True


def moveHead(dir, knot):

    deltax = 0
    deltay = 0
    if dir == "L":
        deltax = -1
    elif dir == "R":
        deltax = 1
    elif dir == "U":
        deltay = 1
    else:
        deltay = -1

    knot.x = knot.x + deltax
    knot.y = knot.y + deltay


def moveTail(prevKnot, currKnot):

    if prevKnot.x == currKnot.x and prevKnot.y == currKnot.y:
        return

    deltax = 0
    deltay = 0

    # horizontal move
    if (prevKnot.y == currKnot.y):
        if abs(currKnot.x - prevKnot.x) == 2:
            if prevKnot.x > currKnot.x:
                deltax = 1
            else:
                deltax = -1

    # vertical move
    elif (prevKnot.x == currKnot.x):
        if abs(currKnot.y - prevKnot.y) == 2:
            if prevKnot.y > currKnot.y:
                deltay = 1
            else:
                deltay = -1

    # diagnonal move

    elif abs(currKnot.x - prevKnot.x) == 2 or abs(currKnot.y - prevKnot.y) == 2:
        if prevKnot.x > currKnot.x:
            deltax = 1
        else:
            deltax = -1

        if prevKnot.y > currKnot.y:
            deltay = 1
        else:
            deltay = -1

    currKnot.x = currKnot.x + deltax
    currKnot.y = currKnot.y + deltay


def day9p2(file):

    knots = []
    for i in range(10):
        knots.append(knot())

    knots[9].logVisited()

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            dir, num = line.split(' ')
            for i in range(int(num)):
                moveHead(dir, knots[0])
                for j in range(1, 10):
                    moveTail(knots[j-1], knots[j])
                knots[9].logVisited()

    result = knots[9].visited.keys().__len__()
    print(result)
    return result


if __name__ == '__main__':
    day9p2("day9input.txt")
