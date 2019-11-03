import sys
n, m, p, q = [int(x) for x in sys.stdin.readline().split()]
flights = [[int(x) for x in sys.stdin.readline().split()] + [True] for x in range(p)]
portals = [[int(x) for x in sys.stdin.readline().split()] + [False] for x in range(q)]
graph = flights+portals
graph.sort(key=lambda x: x[2])

# make sure when calculating costs, you account for planets not unioned
sum1 = [x[2] for x in flights]
sum2 = [x[2] for x in portals]
maxcost = sum(sum1)*n + sum(sum2)*m
flightsubsets = [[x, 0] for x in range(m+1)]  # parent, rank
portalsubsets = [[x, 0] for x in range(n+1)]


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


rowstobemerged = m  # keep in mind this means vertically (cities)
columnstobemerged = n  # keep in mind this means horizontally (planets)
i = 0
total = 0

while rowstobemerged > 1 or columnstobemerged > 1:
    node = graph[i]
    u, v, w, row = node

    if row:  # for rows
        x, y = find(flightsubsets, u), find(flightsubsets, v)

        if x != y:
            union(flightsubsets, x, y)
            total += w*(columnstobemerged)
            rowstobemerged -= 1

    elif not row:
        x, y = find(portalsubsets, u), find(portalsubsets, v)

        if x != y:
            union(portalsubsets, x, y)
            total += w*(rowstobemerged)
            columnstobemerged -= 1

    i += 1


print(maxcost-total)
