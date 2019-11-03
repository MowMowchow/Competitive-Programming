import sys
n, m = [int(x) for x in sys.stdin.readline().split()]
edges = [[int(x) for x in sys.stdin.readline().split()] for x in range(m)]

subsets = [[x, 0] for x in range(n+1)]  # parent and rank


def find(subsets, node):
    if subsets[node][0] != node:
        subsets[node][0] = find(subsets, subsets[node][0])
    return subsets[node][0]


def union(subsets, u, v):
    if subsets[u][1] > subsets[v][1]:
        subsets[v][0] = u
    elif subsets[v][1] > subsets[u][1]:
        subsets[u][0] = v
    else:
        subsets[v][0] = u
        subsets[u][1] += 1


counter = 0
for edge in edges:
    u, v = edge
    x, y = find(subsets, u), find(subsets, v)

    if x != y:
        union(subsets, x, y)

    else:
        counter += 1

    if counter > 1:
        break


if counter <= 1:
    print("YES")
else:
    print("NO")