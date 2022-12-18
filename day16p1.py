

def day16p1(file):

    TARGET_TIME = 30

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

    queue.append(("AA", valveState, 1, 0, "AA", "0", ""))

    # recursive solution: Start at AA and time 0.
    # Add AA to queue

    maxScore = 0
    winningPath = ""
    winningFlows = ""
    winningDistances = ""

    while (queue.__len__()):

        queueItem = queue.pop()

        for i in range(usefulLength):
            valve, valveState, time, score, path, flows, distances = queueItem
            if (valveState[i] == False):

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
                if time + cost <= TARGET_TIME - 1:
                    score = score + (TARGET_TIME - time - cost) * flowRate
                    path = path + "," + targetVertice
                    flows = flows + ", " + str(flowRate)
                    distances = distances + " --> " + str(cost)
                    newQueueItem = (targetVertice, newValveState,
                                    time + cost + 1,
                                    score,
                                    path, flows, distances
                                    )
                    queue.append(newQueueItem)

        if (score > maxScore):
            maxScore = score
            winningPath = path
            winningFlows = flows
            winningDistances = distances

            # Add 1 item to queue for each possible node to go to
            # Don't just add the target node
            # Look at usefulVertices, filter to closed
            # Get time to node from  dist dict
            # If currentTime + time < (30-1)
            #   Add to queue
            #   Set Open, increase rate

    print(maxScore)
    print(winningPath)
    print(winningFlows)
    print(winningDistances)
    return maxScore

# failed runs:
# 1691 too low


if __name__ == '__main__':
    day16p1("day16input.txt")
