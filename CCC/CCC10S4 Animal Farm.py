import sys
m = int(sys.stdin.readline())
edges = []
ingraph = []
outgraph = []
insubsets = [[x, 0] for x in range(1001)]
outsubsets = [[x, 0] for x in range(1001)]
edgecount = {}
for i in range(1, m+1):
    q = [int(x) for x in sys.stdin.readline().split()]
    for j in range(1, q[0]):
        edges.append([q[j], q[j+1], q[j+q[0]]])
        try:
            edgecount[(q[j], q[j+1])].append(i)
            edgecount[(q[j+1], q[j])].append(i)
        except:
            edgecount[(q[j], q[j + 1])] = [i]
            edgecount[(q[j + 1], q[j])] = [i]


    edges.append([q[q[0]], q[1], q[q[0]*2]])
    try:
        edgecount[(q[q[0]], q[1])].append(i)
        edgecount[(q[1], q[q[0]])].append(i)
    except:
        edgecount[(q[q[0]], q[1])] = [i]
        edgecount[(q[1], q[q[0]])] = [i]


edges.sort(key=lambda x: x[2])
for edge in edges:  # don't need to filter redundant edges because Kruskal's is fast
    if len(edgecount[(edge[0], edge[1])]) == 1:
        outgraph.append([edgecount[(edge[0], edge[1])][0], 0, edge[2]])
    else:
        ingraph.append([edgecount[(edge[0], edge[1])][0], edgecount[(edge[0], edge[1])][1], edge[2]])
        outgraph.append([edgecount[(edge[0], edge[1])][0], edgecount[(edge[0], edge[1])][1], edge[2]])


def find(subsets, node):
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


def kruskal(graph, subsets, out):
    cropped = 0
    counter = 0

    for node in graph:
        u, v, w = node
        x, y, = find(subsets, u), find(subsets, v)

        if x != y:
            union(subsets, x, y)
            cropped += w
            counter += 1

            if counter == m-1 and not out:
                return cropped
            elif counter == m and out:
                return cropped

    return float("inf")


inresult = kruskal(ingraph, insubsets, False)
outresult = kruskal(outgraph, outsubsets, True)
print(min(inresult, outresult))