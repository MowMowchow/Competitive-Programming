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
components = []


def dfs(curr):
  global time
  vis[curr] = True
  time += 1
  disc[curr] = time 
  low[curr] = time
  children = 0
  for node in adj[curr]:
    if not vis[node]:
      bi_comp.append(list([curr, node]))

      children += 1
      parent[node] = curr
      dfs(node)
      low[curr] = min(low[curr], low[node])
      if parent[curr] == -1 and children > 1:
        temp = []
        while len(bi_comp) > 0:
          if bi_comp[-1] == [curr, node]:
            temp.append(bi_comp.pop(-1))
            break
          temp.append(bi_comp.pop(-1))
        components.append(temp)
      if parent[curr] != -1 and low[node] >= disc[curr]:
        temp = []
        while len(bi_comp) > 0:
          if bi_comp[-1] == [curr, node]:
            temp.append(bi_comp.pop(-1))
            break
          temp.append(bi_comp.pop(-1))
        components.append(temp)

    elif parent[curr] != node and disc[node] < low[curr]:
      bi_comp.append(list([curr, node]))

      low[curr] = min(low[curr], disc[node])

      
for i in range(0, N):
  if not vis[i]:
    print("trying node:", i)
    bi_comp = []
    dfs(i)

for i in components:
  print(i)