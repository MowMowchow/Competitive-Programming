import sys
n = int(sys.stdin.readline())
edges = []
adj = [[] for x in range(n+1)]
direc = [False for x in range(n+2)]

for q in range(n-1):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    adj[x].append(y)
    adj[y].append(x)
    edges.append([x, y])


def dfs(curr, prev):
    direc[curr] = not direc[prev]

    for node in adj[curr]:
        if node != prev:
            dfs(node, curr)


dfs(1, n+1)
for edge in edges:
    a, b = edge
    if direc[a] and not direc[b]:
        print(1)
    else:
        print(0)