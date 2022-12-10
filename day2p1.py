def day2p1(file):

    dict = {
        # rock
        "A X": 4,  # rock ties rock
        "A Y": 8,  # rock covered by paper
        "A Z": 3,  # rock smashes scissors

        # paper
        "B X": 1,  # paper covers rock
        "B Y": 5,  # paper ties paper
        "B Z": 9,  # paper cut by scissors

        # scissors
        "C X": 7,  # scissors smahsed by rock
        "C Y": 2,  # scissors cuts paper
        "C Z": 6  # scissors ties scissors
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
    day2p1("day2input.txt")
