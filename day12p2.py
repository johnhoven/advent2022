class table():
    def __init__(self):
        self.data = ""
        self.size = 0
        self.rows = 0
        self.startX = 0
        self.startY = 0
        self.explored = {}
        self.adventureQueue = []

    def addRow(self, data):
        self.data = self.data + data
        self.size = data.__len__()
        self.rows = self.rows + 1

    def findStartCost(self):
        data = self.data
        index = data.index("S")
        return self.explored[index]
        #row, col = self.getPosXY(index)
        # return (row, col)

    def findEnd(self):
        data = self.data
        index = data.index("E")
        row, col = self.getPosXY(index)
        return (row, col)

    def getPosXY(self, index):
        row = int(index / self.size)
        col = index % self.size
        return (row, col)

    def getIndexForXY(self, x, y):
        return x * self.size + y

    def getValueAtXY(self, x, y):
        index = self.getIndexForXY(x, y)
        return self.data[index]

    def isPossibleValue(self, value, potValue):

        valOrd = ord(value)
        if value == "S":
            valOrd = ord('a')

        targetOrd = ord(potValue)
        if potValue == "E":
            targetOrd = ord('z')

        if (targetOrd - valOrd) <= 1:
            return True

        return False

    def getPossiblePaths(self, x, y):

        potValue = self.getValueAtXY(x, y)
        potentials = []

        # up
        if (x > 0):
            value = self.getValueAtXY(x-1, y)
            if self.isPossibleValue(value, potValue):
                potentials.append((x-1, y, value))

        # down
        if (x < self.rows - 1):
            value = self.getValueAtXY(x+1, y)
            if self.isPossibleValue(value, potValue):
                potentials.append((x+1, y, value))

        # left
        if (y > 0):
            value = self.getValueAtXY(x, y - 1)
            if self.isPossibleValue(value, potValue):
                potentials.append((x, y - 1, value))

        # right
        if (y < self.size - 1):
            value = self.getValueAtXY(x, y + 1)
            if self.isPossibleValue(value, potValue):
                potentials.append((x, y + 1, value))

        return potentials

    def runAdventure(self, x, y):
        index = self.getIndexForXY(x, y)

        self.explored[index] = 0
        self.adventureQueue.append((0, index))

        while self.adventureQueue.__len__():
            cost, nextAdventure = self.adventureQueue.pop()
            nx, ny = self.getPosXY(nextAdventure)
            self.adventure(nx, ny, cost)

    # def secondPass(self, x, y):

    def adventure(self, x, y, cost):
        potentials = self.getPossiblePaths(x, y)
        index = self.getIndexForXY(x, y)

        newCost = cost + 1
        self.explored[index] = newCost

        for potential in potentials:
            px, py, pvalue = potential
            pindex = self.getIndexForXY(px, py)
            if pindex in self.explored.keys():
                oldCost = self.explored[pindex]
                if newCost + 1 < oldCost:
                    self.adventure(px, py, newCost)
                continue

            self.adventureQueue.append((newCost, pindex))

    def printGrid(self):
        buffer = ""
        for i in range(self.data.__len__()):
            if i % self.size == 0:
                buffer = buffer + '\n'

            if self.data[i] == 'S':
                buffer = buffer + 'S'
            elif self.data[i] == 'E':
                buffer = buffer + 'E'
            elif i in self.explored.keys():
                buffer = buffer + 'X'
            else:
                buffer = buffer + ' '
        # print(buffer)

    def findShortestA(self):
        result = 9999
        for i in range(self.data.__len__()):
            x = self.data[i]
            if (x == 'S' or x == 'a') and i in self.explored.keys():
                if self.explored[i] < result:
                    result = self.explored[i]
        return result


def day12p2(file):

    data = table()

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            data.addRow(line)

    ex, ey = data.findEnd()
    data.runAdventure(ex, ey)
    #result = data.findStartCost()

    # data.printGrid()

    result = data.findShortestA()

    print(result - 1)
    return result - 1


if __name__ == '__main__':
    day12p2("day12input.txt")
