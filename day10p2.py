
def day10p2(file):

    regX = 1
    cycles = 0
    dict = {}

    output = []
    buffer = ""
    posX = 0

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            spriteLowerBounds = regX - 1
            spriteUpperBounds = regX + 1
            if (spriteLowerBounds < 0):
                spriteLowerBounds = 0
                spriteUpperBounds = 2
            if spriteUpperBounds > 39:
                spriteUpperBounds = 39
                spriteLowerBounds = 37

            if spriteLowerBounds <= posX and spriteUpperBounds >= posX:
                buffer = buffer + "#"
            else:
                buffer = buffer + "."
            posX = posX + 1
            if posX == 40:
                posX = 0
                output.append(buffer)
                buffer = ""

            if line[0:4] == "addx":
                _addx, V = line.split(' ')

                cycles = cycles + 1
                dict[cycles] = regX

                spriteLowerBounds = regX - 1
                spriteUpperBounds = regX + 1
                if (spriteLowerBounds < 0):
                    spriteLowerBounds = 0
                    spriteUpperBounds = 2
                if spriteUpperBounds > 39:
                    spriteUpperBounds = 39
                    spriteLowerBounds = 37

                if spriteLowerBounds <= posX and spriteUpperBounds >= posX:
                    buffer = buffer + "#"
                else:
                    buffer = buffer + "."
                posX = posX + 1
                if posX == 40:
                    posX = 0
                    output.append(buffer)
                    buffer = ""

                regX = regX + int(V)
                cycles = cycles + 1

            else:
                cycles = cycles + 1

            # dict[cycles] = regX
            # spriteLowerBounds = regX - 1
            # spriteUpperBounds = regX + 1
            # if (spriteLowerBounds < 0):
            #     spriteLowerBounds = 0
            #     spriteUpperBounds = 2
            # if spriteUpperBounds > 39:
            #     spriteUpperBounds = 39
            #     spriteLowerBounds = 37

            # if spriteLowerBounds <= posX and spriteUpperBounds >= posX:
            #     buffer = buffer + "#"
            # else:
            #     buffer = buffer + "."
            # posX = posX + 1
            # if posX == 40:
            #     posX = 0
            #     output.append(buffer)
            #     buffer = ""

    result = "\n".join(output)

    print(result)

    return result


if __name__ == '__main__':
    day10p2("day10input.txt")
