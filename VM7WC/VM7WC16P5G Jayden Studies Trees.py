import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
edges = [[] for x in range(n+1)]
rooted = [0, 0]  # dist, node
randomstart = 0
for x in range(n-1):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    randomstart = x
    edges[x].append(y)
    edges[y].append(x)


def dfs(curr, visitedarr, length):
    global rooted
    if not visitedarr[curr]:
        visitedarr[curr] = True

        if length > rooted[0]:
            rooted = list([length, curr])

        for node in edges[curr]:
            dfs(node, visitedarr, length+1)


visited = [False for x in range(n+1)]
dfs(randomstart, visited, 0)

visited = [False for x in range(n+1)]
dfs(rooted[1], visited, 0)

print(rooted[0])