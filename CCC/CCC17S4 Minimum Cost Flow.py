import sys
n, m, d = [int(x) for x in sys.stdin.readline().split()]
graph = []
subsets1 = [[x, 0] for x in range(n+1)]  # parent, rank
subsets2 = [[x, 0] for x in range(n+1)]  # parent, rank
for x in range(m):
    query = [int(x) for x in sys.stdin.readline().split()]
    if x < n-1:
        query += [True]

    else:
        query += [False]

    graph.append(query)
graph.sort(key=lambda x: x[2])


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


def kruskal(currgraph):
    counter = 0
    diff = 0
    highestmst = 0

    for node in currgraph:
        u, v, w, original = node
        x, y = find(subsets1, u), find(subsets1, v)

        if x != y:
            counter += 1
            if not original:
                diff += 1
            union(subsets1, x, y)

            if counter == n-1:
                counter += 1
                highestmst = w
                break
                # return mst, diff

    # pt2
    for node in currgraph:
        u, v, w, original = node
        x, y = find(subsets2, u), find(subsets2, v)

        if x != y:
            if w < highestmst or w == highestmst and original:
                union(subsets2, x, y)

            elif original and w <= d:  # this is not working for some reason
                diff -= 1
                break

    return diff


result = kruskal(graph)

print(result)