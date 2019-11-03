import sys
sys.setrecursionlimit(100000000)
# dfs, and on the call back, compare the result to the restraints
n, c, k = [int(x) for x in sys.stdin.readline().split()]
cherries = [0]+[int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(n+1)]
weighttotals = [0 for x in range(n+1)]
for q in range(n-1):
    x, y, w = [int(x) for x in sys.stdin.readline().split()]
    adj[x].append([y, w])
    # adj[y].append([x, w])

total = 0


def dfs(curr, prev):
    global total
    for node, ww in adj[curr]:
        if node != prev:
            dfs(node, curr)
            cherries[curr] += cherries[node]
            weighttotals[curr] += ww + weighttotals[node]

            if cherries[node] >= c and ww + weighttotals[node] <= k:
                total += 1


dfs(1, 0)

print(total)