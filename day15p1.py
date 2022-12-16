class links():
    def __init__(self, start, end, next):
        self.start = start
        self.end = end
        self.next = next

 # Store as a linked list of ranges
        # { xstart, xend, nextNode} -->  { xstart, xend, nextNode}
        # when a new link is added, merge in
        # If xstart of head is greater:
        # if xend is greater or equal to head's xstart, update head's xstart
        # if xend is greater or equal to head's xend, update head's xend
        # # otherwise Insert a new head
        # If xstart matches, update xend of existing node (if greater)
        # If xstart is greater, continue down nextNodes, evalating above.
        # If none found, add a new tail


def insertInLinks(head, xStart, xEnd):
    if head == None:
        return links(xStart, xEnd, None)
    else:
        prev = None
        localHead = head

        while (localHead != None):

            # we start earlier than current node
            if xStart <= localHead.start:
                if xEnd >= localHead.start:
                    localHead.start = xStart
                    if (xEnd >= localHead.end):
                        localHead.end = xEnd
                else:
                    localHead = links(xStart, xEnd, localHead)
                    if prev != None:
                        prev.next = localHead
                    else:
                        return localHead
                break

            # we start middle of current node
            elif xStart <= localHead.end:
                if xEnd > localHead.end:
                    localHead.end = xEnd

                    # devour
                    while (localHead.next != None and localHead.next.start < xEnd):
                        if localHead.next.end > xEnd:
                            localHead.end = localHead.next.end
                        localHead.next = localHead.next.next

                break

            # if xStart == localHead.start:
            #     if xEnd >= localHead.end:
            #         localHead.end = xEnd
            #     break

            # we are somewhere fully after.  Move to next node to see where we fall in
            prev = localHead
            localHead = localHead.next
            if localHead is None:
                localHead = links(xStart, xEnd, None)
                prev.next = localHead
                break
    return head


def sumLinks(head, beacons):

    sum = 0
    while (head != None):

        sum = sum + (head.end - head.start + 1)

        for x in beacons:
            if x >= head.start and x <= head.end:
                sum = sum - 1

        head = head.next

    return sum


def day15p1(file, targetYValue):

    head = None
    beacons = []
    beaconDup = {}

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            _sensor, _at, _x, _y, _closest, _beacon, _is, _at, _x2, _y2 = line.split(
                ' ')
            x1 = int(_x.split(',')[0].split('=')[1])
            y1 = int(_y.split(':')[0].split('=')[1])
            x2 = int(_x2.split(',')[0].split('=')[1])
            y2 = int(_y2.split('=')[1])

            if y2 == targetYValue:
                if x2 not in beaconDup.keys():
                    beacons.append(x2)
                    beaconDup[x2] = True

            manDist = abs(x1 - x2) + abs(y1-y2)

            if y1 >= targetYValue - manDist and y1 <= targetYValue + manDist:
                distFromY = abs(y1 - targetYValue)
                xdist = manDist - distFromY
                xLow = x1 - xdist
                xHigh = x1 + xdist

                head = insertInLinks(head, xLow, xHigh)

    # for each sensor, find manhattan distance between it and its sensor
        # Determine if sensor can reach target row
        # If so, determine xstart and xend that it scans, and mark known beacon
        #   remove known beacons

    # how to calculate range:
        # (range - distance aka 9-3) = 6
        # multiple x 2, plus 1 = 13 width, centered on signal's X

    # Result: Sum xend - xstart + 1 for each node in the list

    result = sumLinks(head, beacons)
    print(result)
    return result


if __name__ == '__main__':
    day15p1("day15input.txt", 2000000)
