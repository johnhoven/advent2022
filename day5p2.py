def moveContainers(list, num, stack1, stack2):

    tmpStack = []
    for i in range(num):
        v = list[stack1-1].pop()
        tmpStack.append(v)

    for i in range(num):
        v = tmpStack.pop()
        list[stack2-1].append(v)


def day5p2(file):

    list = []

    line1 = True
    containersDone = False
    cols = 0

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            if line1:
                lng = line.__len__()
                cols = int((lng + 1) / 4)

                for i in range(cols):
                    list.append([])

                line1 = False

            if line == "":
                containersDone = True
                for i in range(cols):
                    list[i].reverse()

                continue

            if containersDone:

                _move, numContainers, _from, stack1, _to, stack2 = line.split(
                    ' ')
                moveContainers(list, int(numContainers),
                               int(stack1), int(stack2))

            else:
                if line[1] == "1":
                    continue

                # Parse containers
                for i in range(cols):
                    sub = line[i * 4:i*4+3]
                    if sub[1] != " ":
                        list[i].append(sub[1])

    msg = ""
    for i in range(cols):
        msg += list[i].pop()
    print(msg)
    return msg


if __name__ == '__main__':
    day5p2("day5input.txt")
