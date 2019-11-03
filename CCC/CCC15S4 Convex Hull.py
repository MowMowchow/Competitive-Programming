import sys
k, n, m = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(n+1)]
for i in range(m):
    x, y, w, b = [int(x) for x in sys.stdin.readline().split()]
    adj[x].append([y, w, b])
    adj[y].append([x, w, b])
a, b = [int(x) for x in sys.stdin.readline().split()]
dp = [[float("inf") if n != a else 0 for k in range(k+1)] for n in range(n+1)]
final = float("inf")

queue = [[a, 0]]

# spfa + dp = woah
while queue:
    curr, hull = queue.pop(0)

    if curr == b:
        final = min(final, dp[curr][hull])

    for temp in adj[curr]:
        node, weight, burn = temp
        if hull + burn < k and dp[node][hull+burn] > dp[curr][hull] + weight:
            dp[node][hull+burn] = dp[curr][hull] + weight

            if final > dp[node][hull+burn]:
                queue.append([node, hull+burn])


if final == float("inf"):
    print(-1)
else:
    print(final)