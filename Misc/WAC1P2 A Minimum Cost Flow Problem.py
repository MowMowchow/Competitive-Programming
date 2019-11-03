import sys
n, m, k = [int(x) for x in sys.stdin.readline().split()]
subsets = [[x, 0] for x in range(n+1)]  # parent, rank
edges = [[int(x) for x in sys.stdin.readline().split()] for x in range(m)]

def find(node):
    if subsets[node][0] != node:
        return find(subsets[node][0])
    return subsets[node][0]

def union(u, v):
    if subsets[u][1] > subsets[v][1]:
        subsets[v][0] = u
    elif subsets[u][1] < subsets[v][1]:
        subsets[u][0] = v
    else:
        subsets[u][1] += 1
        subsets[v][0] = u

count = 0  # how many nodes are connected
nono = 0

for edge in edges:
    u, v = edge
    x, y, = find(u), find(v)

    if x != y:
        count += 1
        union(x, y)

    else:
        nono += 1

print(max(0, ((n-1)-(count)) - min(nono, k)))