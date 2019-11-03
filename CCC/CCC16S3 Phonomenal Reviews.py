import sys
sys.setrecursionlimit(100000)
n, m = [int(x) for x in sys.stdin.readline().split()]
temprestaurants = [int(x) for x in sys.stdin.readline().split()]
pho = [False for x in range(n)]
routes = [False for x in range(n)]
adjacency = [[] for x in range(n)]
totalroads = 0
for x in range(n-1):
    query = [int(x) for x in sys.stdin.readline().split()]
    adjacency[query[0]].append(query[1])
    adjacency[query[1]].append(query[0])

for x in range(len(temprestaurants)):
    pho[temprestaurants[x]] = True


def mark(curr, prev):
    global totalroads
    if not visited[curr]:
        visited[curr] = True
        if pho[curr] and not routes[curr]:  # marking phos just for simplicity
            routes[curr] = True
            totalroads += 1

        for node in adjacency[curr]:
            if not visited[node]:
                mark(node, curr)
                if routes[node] and not routes[curr]:  # necessary to visit this node in order to get to other necessary node
                    routes[curr] = True
                    totalroads += 1


def dfs(curr, prev, length, max, final):
    global maxdist1, maxdist2
    if not visited[curr]:
        visited[curr] = True
        if not final:
            if length > maxdist1[1]:
                maxdist1 = [curr, length]
        elif final:
            if length > maxdist2[1]:
                maxdist2 = [curr, length]

        for node in adjacency[curr]:
            if routes[node]:
                dfs(node, curr, length+1, max, final)

        return


maxdist1 = [0, 0]  # node, length
maxdist2 = [0, 0]
visited = [False for x in range(n)]
mark(temprestaurants[0], 0)
visited = [False for x in range(n)]
dfs(temprestaurants[0], -1, 0, [0, 0], False)
visited = [False for x in range(n)]
dfs(maxdist1[0], -1, 0, [0, 0], True)

print((2*(totalroads-maxdist2[1]-1))+maxdist2[1])