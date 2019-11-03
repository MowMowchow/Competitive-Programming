import sys
n = int(sys.stdin.readline())
items = [0]+[int(x) for x in sys.stdin.readline().split()]
m = int(sys.stdin.readline())
adj = [[] for x in range(n+1)]
visited = [False for x in range(n+1)]
dists = [[float("inf"), 0] for x in range(n+1)]  # dist, items
for i in range(m):
    x, y, w = [int(x) for x in sys.stdin.readline().split()]
    adj[x].append([y, w])
    adj[y].append([x, w])


queue = [1]  # location, items
dists[1][0] = 0
# dists[n][1] += items[1]
# print(dists)
while queue:
    curr = queue.pop(0)
    visited[curr] = False

    for node in adj[curr]:
        if dists[node[0]][0] > dists[curr][0] + node[1]:
            dists[node[0]][0] = dists[curr][0] + node[1]
            dists[node[0]][1] = dists[curr][1] + items[node[0]]
            if not visited[node[0]]:
                # print(curr, "to", node[0], "| items:", dists[curr][1], "+", items[node[0]])
                visited[node[0]] = True
                queue.append(node[0])

        elif dists[node[0]][0] == dists[curr][0] + node[1]:
            dists[node[0]][1] = max(dists[node[0]][1], dists[curr][1] + items[node[0]])
            if not visited[node[0]]:
                # print(curr, "to", node[0], "| items:", dists[curr][1], "+", items[node[0]])
                visited[node[0]] = True
                queue.append(node[0])


# print(dists)
if dists[n][0] != float("inf"):
    print(dists[n][0], dists[n][1]+items[1])
else:
    print("impossible")
