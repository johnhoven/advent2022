def day2p2(file):

    dict = {
        # rock
        "A X": 3,  # rock LOSE scissors
        "A Y": 4,  # rock draw rock
        "A Z": 8,  # rock win paper

        # paper
        "B X": 1,  # paper LOSE rock
        "B Y": 5,  # paper ties paper
        "B Z": 9,  # paper win scissors

        # scissors
        "C X": 2,  # scissors lose paper
        "C Y": 6,  # scissors draw scissors
        "C Z": 7  # scissors win rock
    }

    score = 0
    lines = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            lines = lines + 1

            if line in dict.keys():
                #print(line, dict[line])
                score += dict[line]
            else:
                print('uhoh', line)

    print(lines, score)
    return score


if __name__ == '__main__':
    day2p2("day2input.txt")
