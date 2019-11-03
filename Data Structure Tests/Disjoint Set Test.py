n, m = [int(x) for x in sys.stdin.readline().split()]
graph = [[int(x) for x in sys.stdin.readline().split()]+[y] for y in range(m)]
subsets = [[x, 0] for x in range(n+1)]  # parent, rank


def find(subsets, node):  # union find with path compression
    if subsets[node][0] != node:
        subsets[node][0] = find(subsets, subsets[node][0])
    return subsets[node][0]


def union(subsets, u, v):
    if subsets[u][1] > subsets[v][1]:
        subsets[v][0] = u
    elif subsets[u][1] < subsets[v][1]:
        subsets[u][0] = v
    else:
        subsets[v][0] = u
        subsets[u][1] += 1


def kruskal():
    mst = []
    graph.sort(key=lambda x: x[2])
    counter = 0

    for node in graph:
        u, v, w, = node
        x = find(subsets, u)
        y = find(subsets, v)

        if x != y:
            counter += 1
            mst.append([u, v, w])
            union(subsets, x, y)

        if counter == n-1:
            return mst

    return None


mst = kruskal()
if mst:
    for edge in mst:
        print(edge[2]+1)
else:
    print("Disconnected Graph")