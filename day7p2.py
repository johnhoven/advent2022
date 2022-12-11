class directory:

    def calcSize(self):
        self.size = 0
        for key in self.files:
            self.size += self.files[key]

        for key in self.subDirectories:
            self.subDirectories[key].calcSize()
            self.size = self.size + self.subDirectories[key].size

    def findSizesUnderGoal(self, goal):
        total = 0
        if self.size <= goal:
            total = total + self.size

        for key in self.subDirectories:
            total = total + self.subDirectories[key].findSizesUnderGoal(goal)
        return total

    def findSmallest(self, goal):
        smallest = None

        if self.size >= goal:
            smallest = self.size

        for key in self.subDirectories:
            sub = self.subDirectories[key]
            tmp = sub.findSmallest(goal)
            if tmp != None and (smallest == None or smallest > tmp):
                smallest = tmp

        return smallest

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subDirectories = {}
        self.files = {}
        self.size = 0


def day7p2(file):

    totalSpace = 70000000
    spaceNeededForUpdate = 30000000

    isFirst = True
    root = None
    cd = None
    currentLs = None

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            if isFirst:
                root = cd = directory("/", None)
                isFirst = False
            elif line == "$ cd /":
                cd = root
            elif line == "$ cd ..":
                if cd.parent != None:
                    cd = cd.parent
            elif line[0:5] == "$ cd ":
                dirName = line[5:]
                if dirName in cd.subDirectories:
                    cd = cd.subDirectories[dirName]
                else:
                    tmp = directory(dirName, cd)
                    cd.subDirectories[dirName] = tmp
                    cd = tmp
            elif line[0:4] == "$ ls":
                continue
            elif line[0:4] == "dir ":
                dirName = line[4:]
                if dirName in cd.subDirectories:
                    None  # currentLs = cd.subDirectories[dirName]
                else:
                    currentLs = directory(dirName, cd)
                    cd.subDirectories[dirName] = currentLs
            else:
                size, name = line.split(' ')
                cd.files[name] = int(size)

    root.calcSize()

    freeSpace = totalSpace - root.size
    remainingSpaceNeeded = spaceNeededForUpdate - freeSpace

    result = root.findSmallest(remainingSpaceNeeded)
    print(result)
    return result


if __name__ == '__main__':
    day7p2("day7input.txt")
