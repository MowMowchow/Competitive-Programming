import sys
numberofcities = int(sys.stdin.readline().strip("\n"))
numberofroutes = int(sys.stdin.readline().strip("\n"))
routes = [[0 for x in range(5000 + 1)] for y in range(5000 + 1)]
availablecities = [float("inf") for z in range(5000 + 1)]

for city in range(numberofroutes):
    query = [int(x) for x in sys.stdin.readline().strip("\n").split()]
    routes[query[0]][query[1]] = query[2]
    routes[query[1]][query[0]] = query[2]

numberofpencilcities = int(sys.stdin.readline().strip("\n"))
for city in range(numberofpencilcities):
    query = [int(x) for x in sys.stdin.readline().strip("\n").split()]
    availablecities[query[0]] = query[1]

destination = int(sys.stdin.readline().strip("\n"))


def dijkstra():
    visited = [False for x in range(5001)]
    done = False

    while not done:
        current = 0
        for city in range(numberofcities+1):
            if availablecities[current] > availablecities[city] and not visited[city]:
                current = city

        if current == destination:
            return availablecities[current]

        visited[current] = True

        for city in range(numberofcities+1):
            if routes[current][city] != 0:
                if routes[current][city] + availablecities[current] < availablecities[city]:
                    availablecities[city] = routes[current][city] + availablecities[current]


print(dijkstra())