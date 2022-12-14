class linkedlistnode():
    def __init__(self, parent):
        self.parent = parent
        # self.children = []
        self.values = []

    def add(self, value):
        self.values.append(value)

    def close(self):
        # if self.values.__len__() == 1:
        #    convert = linkedlistnode(self)
        #    convert.add(self.values[0])
        #    self.values = []
        #    self.values.append(convert)
        return self.parent

    def compare(self, rightList):

        leftList = self
        rightList = rightList
        lLen = leftList.values.__len__()
        rLen = rightList.values.__len__()

        if (lLen == 0 and rLen == 0):
            return 0
        if (lLen == 0):
            return 1

        for i in range(lLen):

            # right side ran out of items, so in wrong order
            if i >= rLen:
                return -1

            x = leftList.values[i]
            y = rightList.values[i]
            if isinstance(x, int) and isinstance(y, int):
                if (x > y):
                    return -1
                elif (x < y):
                    return 1
            elif (isinstance(x, int) and not isinstance(y, int)) or (not isinstance(x, int) and isinstance(y, int)):

                if isinstance(x, int):
                    xnew = linkedlistnode(leftList)
                    xnew.add(x)
                    x = xnew
                if isinstance(y, int):
                    ynew = linkedlistnode(rightList)
                    ynew.add(y)
                    y = ynew

                c = x.compare(y)
                if c != 0:
                    return c
            else:
                c = x.compare(y)
                if c != 0:
                    return c

        # left ran out of items first, so right order
        if lLen < rLen:
            return 1

        return 0


class pair():
    def __init__(self, line):
        self.line = line
        self.parse()

    def parse(self):

        ll = None
        root = None
        num = ''

        for x in self.line:
            if x == '[':
                ll = linkedlistnode(ll)
                if root == None:
                    root = ll
                else:
                    ll.parent.add(ll)

            elif x == ']':
                if num != "":
                    ll.add(int(num))
                    num = ''
                ll = ll.close()

            elif x == ',':
                if num != "":
                    ll.add(int(num))
                    num = ''
                None
            else:
                num = num + x
                # ll.add(int(x))

        self.linkedlist = root

    def compare(self, right):

        leftList = self.linkedlist
        rightList = right.linkedlist
        return leftList.compare(rightList) >= 0


def processPairs(line1, line2):
    lpair = pair(line1)
    rpair = pair(line2)
    return lpair.compare(rpair)


def day13p2(file):

    divider1 = pair("[[2]]")
    divider2 = pair("[[6]]")
    pairs = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            if line != "":
                newPair = pair(line)
                pairs.append(newPair)

    # no reason to sort the whole list, just these two
    # O(2n)
    index1 = 1
    index2 = 2
    for p in pairs:
        if p.compare(divider1):
            index1 = index1 + 1
        if p.compare(divider2):
            index2 = index2 + 1

    print(index1, index2, index1 * index2)
    return index1 * index2


if __name__ == '__main__':
    day13p2("day13input.txt")
