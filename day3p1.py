def day3p1(file):

    keys = []
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            length = line.__len__()

            half = int(length/2)
            halfa = line[0:half]
            halfb = line[half:length]

            d = {}
            for c in halfa:
                d[c] = 1

            for c in halfb:
                if c in d.keys():
                    keys.append(c)
                    break

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
    day3p1("day3input.txt")
