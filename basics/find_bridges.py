import sys
N, M = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(N+1)]
for i in range(M):
  a, b = [int(x) for x in sys.stdin.readline().split()]
  adj[a].append(b)
  adj[b].append(a)

vis = [False for x in range(N+1)]
disc = [0 for x in range(N+1)]
low = [float("inf") for x in range(N+1)]
time = 0


def dfs(curr, prev):
  global time
  vis[curr] = True
  time += 1
  disc[curr] = time
  low[curr] = time
  for node in adj[curr]:
    if node != prev:
      if vis[node]:
        low[curr] = min(low[curr], disc[node])
      else:
        dfs(node, curr)
        low[curr] = min(low[curr], low[node])
        if (low[node] > disc[curr]):
          print("edge:", curr, "-", node, "is a bridge!")


for i in range(1, N+1):
  if not vis[i]:
    dfs(i, -1)

