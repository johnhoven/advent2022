
def day16p2(file):

    TARGET_TIME = 26

    edges = []
    vertices = []
    usefulVertices = []
    flowRateDict = {}

    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')

            # Valve JT has flow rate=9; tunnels lead to valves ES, RL, BL, BN
            splits = line.split(' ')
            valve = splits[1]
            rate = int(splits[4].split('=')[1].split(';')[0])
            vertices.append(valve)
            flowRateDict[valve] = rate

            if rate > 0:
                usefulVertices.append(valve)

            for i in range(9, splits.__len__()):
                leadsTo = splits[i].split(',')[0]
                edges.append((valve, leadsTo))

    # let dist be a | V | × |V | array of minimum distances initialized to ∞ (infinity)

    # https: // en.wikipedia.org/wiki/Floyd–Warshall_algorithm
    vertices.sort()
    usefulVertices.sort()
    usefulLength = usefulVertices.__len__()
    usefulVerticesDict = {}
    for i in range(usefulLength):
        usefulVerticesDict[usefulVertices[i]] = i

    verticeToIndexDict = {}
    len = vertices.__len__()
    dist = []
    for i in range(len):
        verticeToIndexDict[vertices[i]] = i
        dist.append([float("inf")] * len)

    for edge in edges:

        uV, vV = edge
        u = verticeToIndexDict[uV]
        v = verticeToIndexDict[vV]

        dist[u][v] = 1
    for vV in vertices:
        v = verticeToIndexDict[vV]
        dist[v][v] = 0
    for k in range(len):
        for i in range(len):
            for j in range(len):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # use DP to recursively compute the maximum pressure when
    # starting at time 0 and position AA

    # state of each item:
    #   currentValve (0-1)
    #   valveState   (2, usefulVertices.length)
    #   time         ()
    #   flowRate     (usefulvertices.length + 2)

    queue = []

    valveState = [False] * usefulLength

    queue.append(("AA", "AA", valveState, 1, 1, 0))

    # recursive solution: Start at AA and time 0.
    # Add AA to queue

    maxScore = 0
    winningPath = ""
    winningFlows = ""
    winningDistances = ""
    iterations = 0
    tenthousands = 0

    dupeCheck = {}

    while (queue.__len__()):

        iterations = iterations + 1
        if (iterations == 10000):
            iterations = 0
            tenthousands = tenthousands + 1
            print(10000 * tenthousands, ": ",
                  queue.__len__(), " current max:", maxScore)

        queueItem = queue.pop()

        for i in range(usefulLength):
            valve, valve2, valveState, time, time2, score = queueItem
            if (valveState[i] == False):

                # we've got two options at every vertice - who heads there

                # Option 1
                newValveState = valveState.copy()
                newValveState[i] = True

                start = verticeToIndexDict[valve]
                targetVertice = usefulVertices[i]
                end = verticeToIndexDict[targetVertice]
                cost = dist[start][end]

                flowRate = flowRateDict[targetVertice]
                # we have to move there, then spend a turn opening, then
                # don't realize gains until next turn.  So only bother
                # if we're under 28

                # uh oh - key doesn't take into account score
                # just because we're in a flipped arrangement doesn't mean we're
                # exactly the same?
                dupeKey = valve + ":" + valve2 + ":" + \
                    str(time) + ":" + str(time2) + \
                    targetVertice + ":" + str(newValveState)
                if time + cost <= TARGET_TIME - 1 and dupeKey not in dupeCheck.keys():

                    dupeCheck[dupeKey] = True

                    myscore = score + (TARGET_TIME - time - cost) * flowRate
                    # path = path + "," + targetVertice
                    # flows = flows + ", " + str(flowRate)
                    # distances = distances + " --> " + str(cost)
                    newQueueItem = (targetVertice, valve2, newValveState,
                                    time + cost + 1,
                                    time2,
                                    myscore
                                    # ,
                                    # path, flows, distances
                                    )
                    queue.append(newQueueItem)

                    if (myscore > maxScore):
                        maxScore = myscore

                # Option 2

                newValveState = valveState.copy()
                newValveState[i] = True

                start = verticeToIndexDict[valve2]
                targetVertice = usefulVertices[i]
                end = verticeToIndexDict[targetVertice]
                cost = dist[start][end]

                flowRate = flowRateDict[targetVertice]
                # we have to move there, then spend a turn opening, then
                # don't realize gains until next turn.  So only bother
                # if we're under 28
                dupeKey = valve2 + ":" + valve + ":" + \
                    str(time2) + ":" + str(time) + \
                    targetVertice + ":" + str(newValveState)
                if time2 + cost <= TARGET_TIME - 1 and dupeKey not in dupeCheck.keys():
                    myscore = score + (TARGET_TIME - time2 - cost) * flowRate
                    dupeCheck[dupeKey] = True
                    # path = path + "," + targetVertice
                    # flows = flows + ", " + str(flowRate)
                    # distances = distances + " --> " + str(cost)
                    newQueueItem = (valve, targetVertice, newValveState,
                                    time,
                                    time2 + cost + 1,
                                    myscore
                                    # ,
                                    # path, flows, distances
                                    )
                    queue.append(newQueueItem)

                    if (myscore > maxScore):
                        maxScore = myscore
            # winningPath = path
            # winningFlows = flows
            # winningDistances = distances

            # Add 1 item to queue for each possible node to go to
            # Don't just add the target node
            # Look at usefulVertices, filter to closed
            # Get time to node from  dist dict
            # If currentTime + time < (30-1)
            #   Add to queue
            #   Set Open, increase rate

    print(maxScore)
    # print(winningPath)
    # print(winningFlows)
    # print(winningDistances)
    return maxScore

# failed runs:
# 1691 too low


if __name__ == '__main__':
    day16p2("day16input.txt")
