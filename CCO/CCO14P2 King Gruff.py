import sys
from bisect import bisect_right
n, m, a, b = [int(x) for x in sys.stdin.readline().split()]
adj1 = [[] for x in range(n+1)]
adj2 = [[] for x in range(n+1)]
edges = []
finaledges = []
for i in range(m):
    x, y, l, c = [int(x) for x in sys.stdin.readline().split()]
    edges.append([x, y, l, c])  # x, y, dist, shutdown cost
    finaledges.append([0, c])  # final dists and shutdown cost
    adj1[x].append([y, l])  # y and the dist
    adj2[y].append([x, l])  # y and the dist


def spfa(start, adj):
    visited = [False for x in range(n+1)]
    dists = [float("inf") for x in range(n+1)]

    queue = [start]
    dists[start] = 0

    while queue:
        curr = queue.pop(0)
        visited[curr] = False

        for node in adj[curr]:
            if dists[node[0]] > dists[curr] + node[1]:
                dists[node[0]] = dists[curr] + node[1]
                if not visited[node[0]]:
                    visited[node[0]] = True
                    queue.append(node[0])

    return dists


atob = spfa(a, adj1)
btoa = spfa(b, adj2)

i = 0
for edge in edges:
    finaledges[i][0] = atob[edge[0]] + edge[2] + btoa[edge[1]]
    i += 1

finaledges.sort(key=lambda x: x[0])
finaledges = [[0, 0]] + finaledges

for i in range(1, m+1):
    finaledges[i][1] += finaledges[i-1][1]

q = int(sys.stdin.readline())
wa = [x[0] for x in finaledges]
for i in range(q):
    d = int(sys.stdin.readline())

    #first = 0
    #last = m-1

    #while first <= last:
    #    index = first + (last-first)//2

    #    if finaledges[index][0] == d:
    #        break
    #    elif finaledges[index][0] < d:
    #        first = index + 1
    #    else:
    #        last = index - 1

    #print(finaledges[last][1])
    print(finaledges[bisect_right(wa, d)-1][1])