class monkey():
    def __init__(self, items, operation, test, tmonk, fmonk):
        self.items = items
        self.operation = operation
        self.test = test
        self.tmonk = tmonk
        self.fmonk = fmonk
        self.inspected = 0

    def takeTurn(self, monkeys, manage):

        for i in range(self.items.__len__()):
            item = self.items.pop(0)
            self.inspected = self.inspected + 1
            # monkey inspects
            item = self.operation(item)
            # didn't break, become less worried
            # item = int(item / 3)

            item = item % manage

            if item % self.test == 0:
                monkeys[self.tmonk].items.append(item)
            else:
                monkeys[self.fmonk].items.append(item)


def performRound(monkeys, manage):
    for monkey in monkeys:
        monkey.takeTurn(monkeys, manage)

# operation = * 2
# div by 5

# 7 * 2 = 14
# * 2 = 28 / 5 = mod 3
# * 2 = 56 / 5 = mod 1

# divide by 5 each round
# 7 * 2 = 14 % 5 = 4
#  * 2 = 8 % 5 = 3
# * 2 = 6 % 5 = 1


def day11p2(file):

    monkeys = []

    if (file == "day11input.txt"):
        monkeys.append(monkey(
            [83, 88, 96, 79, 86, 88, 70],
            lambda old: old * 5,
            11,
            2,
            3
        ))
        monkeys.append(monkey(
            [59, 63, 98, 85, 68, 72],
            lambda old: old * 11,
            5,
            4,
            0
        ))
        monkeys.append(monkey(
            [90, 79, 97, 52, 90, 94, 71, 70],
            lambda old: old + 2,
            19,
            5,
            6
        ))
        monkeys.append(monkey(
            [97, 55, 62],
            lambda old: old + 5,
            13,
            2,
            6
        ))
        monkeys.append(monkey(
            [74, 54, 94, 76],
            lambda old: old * old,
            7,
            0,
            3
        ))
        monkeys.append(monkey(
            [58],
            lambda old: old + 4,
            17,
            7,
            1
        ))
        monkeys.append(monkey(
            [66, 63],
            lambda old: old + 6,
            2,
            7,
            5
        ))
        monkeys.append(monkey(
            [56, 56, 90, 96, 68],
            lambda old: old + 7,
            3,
            4,
            1
        ))
    else:
        monkeys.append(monkey(
            [79, 98],
            lambda old: old * 19,
            23,
            2,
            3
        ))
        monkeys.append(monkey(
            [54, 65, 75, 74],
            lambda old: old + 6,
            19,
            2,
            0
        ))
        monkeys.append(monkey(
            [79, 60, 97],
            lambda old: old * old,
            13,
            1,
            3
        ))
        monkeys.append(monkey(
            [74],
            lambda old: old + 3,
            17,
            0,
            1
        ))

    # "Manage Stress" by the product of all test values,
    # which will have no mathematical difference on the
    # modulus tests
    listTests = list(map(lambda monkey: monkey.test, monkeys))
    listAmount = 0
    for listTest in listTests:
        if listAmount == 0:
            listAmount = listTest
        else:
            listAmount = listAmount * listTest

    for i in range(10000):
        performRound(monkeys, listAmount)

    result = list(map(lambda monkey: monkey.inspected, monkeys))
    result.sort()
    result.reverse()

    result = result[0] * result[1]
    print(result)
    return result


if __name__ == '__main__':
    day11p2("day11input.txt")
