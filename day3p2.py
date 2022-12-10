def day3p2(file):

    num = 0
    d = {}
    result = ""
    keys = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            locald = {}
            for c in line:
                locald[c] = 1

            for c in locald.keys():
                d[c] = d.get(c, 0) + 1
                if d[c] == 3:
                    result = c
                    keys.append(result)
                    break

            num = num + 1
            if num == 3:
                num = 0
                d = {}
                result = ""

            #print(line, halfa, halfb)
    sum = 0
    for key in keys:
        u = ord(key)
        if u < 91:
            sum = sum + u - (65-27)
        else:
            sum = sum + u - (97 - 1)

    print(sum)
    return sum


if __name__ == '__main__':
    day3p2("day3input.txt")
