import sys
N, M = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(N+1)]
for i in range(M):
  a, b = [int(x) for x in sys.stdin.readline().split()]
  adj[a].append(b)
  adj[b].append(a)


visited = [False for x in range(N+1)]
disc = [0 for x in range(N+1)]
low = [float("inf") for x in range(N+1)]
time = 0
components = []


def dfs(curr, prev):
  global time 
  visited[curr] = True
  time += 1
  disc[curr] = time
  low[curr] = time
  children = 0

  for node in adj[curr]:
    if node != prev:
      if visited[node] and low[curr] > disc[node]:
        bi_comp.append(list([curr, node]))
        low[curr] = min(low[curr], disc[node])
      elif not visited[node]:
        bi_comp.append(list([curr, node]))
        children += 1
        dfs(node, curr)
        low[curr] = min(low[curr], low[node])
        if prev == -1 and children > 1:
          temp = []
          while len(bi_comp) > 0:
            if bi_comp[-1] == [curr, node]:
              temp.append(bi_comp.pop(-1))
              break
            temp.append(bi_comp.pop(-1))
          components.append(temp)
        elif low[node] >= disc[curr]:
          temp = []
          while len(bi_comp) > 0:
            if bi_comp[-1] == [curr, node]:
              temp.append(bi_comp.pop(-1))
              break
            temp.append(bi_comp.pop(-1))
          components.append(temp)



for i in range(0, N):
  if not visited[i]:
    bi_comp = []
    dfs(i, -1)

for i in components:
  print(i)
