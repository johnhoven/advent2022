hx = 0
hy = 0
tx = 0
ty = 0
visited = {}


def logVisited():

    global hx, hy, tx, ty, visited

    visited[tx.__str__() + "." + ty.__str__()] = True


def moveHead(dir):

    global hx, hy, tx, ty, visited

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

    hx = hx + deltax
    hy = hy + deltay


def moveTail():

    global hx, hy, tx, ty, visited

    if hx == tx and hy == ty:
        return

    deltax = 0
    deltay = 0

    # horizontal move
    if (hy == ty):
        if abs(tx - hx) == 2:
            if hx > tx:
                deltax = 1
            else:
                deltax = -1

    # vertical move
    elif (hx == tx):
        if abs(ty - hy) == 2:
            if hy > ty:
                deltay = 1
            else:
                deltay = -1

    # diagnonal move

    elif abs(tx - hx) == 2 or abs(ty - hy) == 2:
        if hx > tx:
            deltax = 1
        else:
            deltax = -1

        if hy > ty:
            deltay = 1
        else:
            deltay = -1

    tx = tx + deltax
    ty = ty + deltay

    logVisited()


def day9p1(file):

    global hx, hy, tx, ty, visited

    logVisited()
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            dir, num = line.split(' ')
            for i in range(int(num)):
                moveHead(dir)
                moveTail()

    result = visited.keys().__len__()
    print(result)
    return result


if __name__ == '__main__':
    day9p1("day9input.txt")
