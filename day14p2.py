
def draw(map, prevx, prevy, x, y):
    # make x and y lower
    if (x > prevx):
        tmp = x
        x = prevx
        prevx = tmp

    if (y > prevy):
        tmp = y
        y = prevy
        prevy = tmp

    while x < prevx or y < prevy:
        map[str(x) + "," + str(y)] = '#'
        if x < prevx:
            x = x + 1
        if y < prevy:
            y = y + 1
    map[str(x) + "," + str(y)] = '#'


def dropSand(map, x, y, maxy):

    present = str(x) + "," + str(y) in map.keys()

    # we've reached the top
    if present and y == 0:
        return False

    if present and y < maxy:

        leftx = x - 1
        if not str(leftx) + "," + str(y + 1) in map.keys():
            return dropSand(map, leftx, y + 1, maxy)
        else:
            rightx = x + 1
            if not str(rightx) + "," + str(y + 1) in map.keys():
                return dropSand(map, rightx, y + 1, maxy)

        # can't land here, or drop left, right
        return False

    # elif y < maxy:
    #    return dropSand(map, x, y + 1, maxy)

    # current space is free, can I keep falling?
    if (y <= maxy - 2):
        if not str(x) + "," + str(y + 1) in map.keys():
            return dropSand(map, x, y + 1, maxy)
        elif not str(x-1) + "," + str(y + 1) in map.keys():
            return dropSand(map, x - 1, y + 1, maxy)
        elif not str(x+1) + "," + str(y + 1) in map.keys():
            return dropSand(map, x + 1, y + 1, maxy)
        elif y < maxy:
            map[str(x) + "," + str(y)] = "O"
            return True
    elif (y == maxy - 1):
        map[str(x) + "," + str(y)] = "O"
        return True

    return False


def day14p2(file):

    map = {}
    maxy = 0

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            prev = None
            prevx = None
            prevy = None
            splits = line.split(" -> ")
            for i in range(splits.__len__()):
                if (prev == None):
                    prev = splits[i]
                    prevx, prevy = prev.split(',')
                    prevx = int(prevx)
                    prevy = int(prevy)
                    if prevy > maxy:
                        maxy = prevy
                    map[prev] = '#'
                else:
                    new = splits[i]
                    newx, newy = new.split(',')
                    newx = int(newx)
                    newy = int(newy)
                    if newy > maxy:
                        maxy = newy
                    draw(map, prevx, prevy, newx, newy)
                    prevx = newx
                    prevy = newy
                    prev = new

    result = 0
    maxy = maxy + 2
    while dropSand(map, 500, 0, maxy):
        result = result + 1

    print(result)
    return result


if __name__ == '__main__':
    day14p2("day14input.txt")
