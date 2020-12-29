import sys
N, M = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(N+1)]
for i in range(M):
  a, b = [int(x) for x in sys.stdin.readline().split()]
  adj[a].append(b)
  adj[b].append(a)

time = 0
disc = [0 for x in range(N+1)]
parent = [-1 for x in range(N+1)]
low = [float("inf") for x in range(N+1)]
ap = [False for x in range(N+1)]
vis = [False for x in range(N+1)]


def dfs(curr):
  global time
  vis[curr] = True
  time += 1
  disc[curr] = time 
  low[curr] = time
  children = 0
  for node in adj[curr]:
    if not vis[node]:
      children += 1
      parent[node] = curr
      dfs(node)
      low[curr] = min(low[curr], low[node])
      if parent[curr] == -1 and children > 1:
        ap[curr] = True
      if parent[curr] != -1 and low[node] >= disc[curr]:
        ap[curr] = True

    elif parent[curr] != node:
      low[curr] = min(low[curr], disc[node])


for i in range(1, N+1):
  if not vis[i]:
    dfs(i)

print(ap)