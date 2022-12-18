# didn't finish running, but found right value from current high value
# attempt 1: effectively (2 * Qualified Vertices)!, low memory reqs.
# attempt 2: ran faster initially, found correct high value (luckily),
# but checks to avoid existing paths use to much memory
# may also be bugged as it assumes both cycles came to the same spot
# with the same score
# attempt 3 for fun - actually finishes (fast)


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

    queue = []

    valveState = [False] * usefulLength

    queue.append(("AA", valveState, 1, 0, ""))

    maxScore = 0
    visited = {}

    while (queue.__len__()):

        queueItem = queue.pop()

        for i in range(usefulLength):
            valve, valveState, time, score, path = queueItem
            if (valveState[i] == False):

                newValveState = valveState.copy()
                newValveState[i] = True

                start = verticeToIndexDict[valve]
                targetVertice = usefulVertices[i]
                end = verticeToIndexDict[targetVertice]
                cost = dist[start][end]

                flowRate = flowRateDict[targetVertice]

                if time + cost <= TARGET_TIME - 1:

                    myscore = score + (TARGET_TIME - time - cost) * flowRate
                    splitPath = [targetVertice]
                    if (path != ""):
                        splitPath = path.split(',')
                        splitPath.append(targetVertice)
                        splitPath.sort()
                    path = ','.join(splitPath)
                    newQueueItem = (targetVertice, newValveState,
                                    time + cost + 1,
                                    myscore, path
                                    # ,
                                    # path, flows, distances
                                    )
                    queue.append(newQueueItem)

                    if path in visited.keys():
                        if myscore > visited[path]:
                            visited[path] = myscore
                    else:
                        visited[path] = myscore

    maxScore = 0
    keys = list(visited.keys())
    len = keys.__len__()

    for i in range(len):

        for j in range(i + 1, len):
            score1 = visited[keys[i]]
            score2 = visited[keys[j]]
            if (score1 + score2 <= maxScore):
                continue
            path1 = keys[i]
            path2 = keys[j]
            arr1 = path1.split(',')
            arr2 = path2.split(',')
            disqualify = False
            for v1 in arr1:
                for v2 in arr2:
                    if (v1 == v2):
                        disqualify = True
                        break
                if (disqualify):
                    break
            if disqualify != True:
                maxScore = score1 + score2

    print(maxScore)
    return maxScore


if __name__ == '__main__':
    day16p2("day16input.txt")
