# I think this brute force will work, but to try for a better processing time:
# keep a list of cubes (point being cubes will be much less memory intensive than having to track the fill of 4M lines and constantly merging/extending the cubes from stop explosive memory growth)
# break each scanner into a list of cubes
# merge cubes into existing cubes (extending as necessary)
# eventually left with 4 or less cubes and can find remaining point

# This solution is very wasteful on CPU to avoid needing much memory (only stores current row)

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
                if xEnd >= localHead.start - 1:
                    localHead.start = xStart
                    if (xEnd >= localHead.end):
                        localHead.end = xEnd

                        # devour
                        while (localHead.next != None and localHead.next.start <= xEnd):
                            if localHead.next.end > xEnd:
                                localHead.end = localHead.next.end
                            localHead.next = localHead.next.next
                else:
                    localHead = links(xStart, xEnd, localHead)
                    if prev != None:
                        prev.next = localHead
                    else:
                        return localHead
                break

            # we start middle of current node
            elif xStart <= localHead.end + 1:
                if xEnd > localHead.end:
                    localHead.end = xEnd

                    # devour
                    while (localHead.next != None and localHead.next.start <= xEnd):
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


def evalute(head, min, max):
    sum = 0
    original = head
    while (head != None):

        if (head.start < min):
            head.start = min
        if head.end < head.start:
            head = head.next
            continue

        if head.end > max:
            head.end = max

            if head.end < head.start:
                head = head.next
                continue

        sum = sum + (head.end - head.start + 1)

        head = head.next

    # this is our row
    if sum == max:
        if original.start == 1:
            return 0
        elif original.next == None:
            return max
        else:
            return original.end + 1
    return -1


def day15p2(file, noLargerThanValue):

    for i in range(noLargerThanValue + 1):
        head = None

        if i % 10000 == 0:
            print("Processing" + i.__str__())

        with open(file) as f:
            for line in f:
                line = line.rstrip('\n')

                _sensor, _at, _x, _y, _closest, _beacon, _is, _at, _x2, _y2 = line.split(
                    ' ')
                x1 = int(_x.split(',')[0].split('=')[1])
                y1 = int(_y.split(':')[0].split('=')[1])
                x2 = int(_x2.split(',')[0].split('=')[1])
                y2 = int(_y2.split('=')[1])

                if y2 == i:
                    head = insertInLinks(head, x2, x2)

                manDist = abs(x1 - x2) + abs(y1-y2)

                if y1 >= i - manDist and y1 <= i + manDist:
                    distFromY = abs(y1 - i)
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

        xBeaconValue = evalute(head, 0, noLargerThanValue)
        if xBeaconValue != -1:
            print(i + 4000000 * xBeaconValue)
            return i + 4000000 * xBeaconValue
    return 0


if __name__ == '__main__':
    day15p2("day15input.txt", 4000000)
