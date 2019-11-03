import sys
n, m, b, q = [int(x) for x in sys.stdin.readline().split()]
roads = [[] for x in range(n+1)]
times = [[] for x in range(n+1)]
for i in range(m):
    x, y, w = [int(x) for x in sys.stdin.readline().split()]
    roads[x].append(y)
    roads[y].append(x)
    times[x].append(w)
    times[y].append(w)


def dijkstra(a):
    available = [float("inf") for x in range(n+1)]
    available[a] = 0
    housequeue = [[a, x] for x in roads[a]]  # adjacent houses to a
    timequeue = [x for x in times[a]]  # time for all adjacent houses

    while housequeue:
        x, y = housequeue.pop(0)
        t = timequeue.pop(0)  # time to get from x to y
        if available[x] + t < available[y]:
            available[y] = available[x] + t

            for house in range(len(roads[y])):
                housequeue.append([y, roads[y][house]])  # adjacent houses to y
                timequeue.append(times[y][house])  # time to get to house

    return available


result = dijkstra(b)
for i in range(q):
    d = int(sys.stdin.readline())
    if result[d] != float("inf"):
        print(result[d])
    else:
        print(-1)