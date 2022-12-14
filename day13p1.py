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


def day13p1(file):

    line1 = ""
    line2 = ""
    pairNo = 0
    result = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            if line1 == "":
                line1 = line
            elif line2 == "":
                line2 = line
                pairNo = pairNo + 1
                print(pairNo)
                print(line1)
                print(line2)
                if (processPairs(line1, line2)):
                    print("YES")
                    result = result + pairNo
                else:
                    print("NO")
                print('\n')
            else:
                line1 = ""
                line2 = ""

    print(result)
    return result


if __name__ == '__main__':
    day13p1("day13input.txt")
