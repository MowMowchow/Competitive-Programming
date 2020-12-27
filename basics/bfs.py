import sys
N, M = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(N+1)]

for i in range(M):
  a, b = [int(x) for x in sys.stdin.readline().split()]
  adj[a].append(b)
  adj[b].append(a)


visited = [False for x in range(N+1)]
dist = [0 for x in range(N+1)]

def bfs(start):
  q = [[start, 0]]

  while q:
    curr, length = q.pop(0)
    if not visited[curr]:
      visited[curr] = True
      dist[curr] = length

      for node in adj[curr]:
        temp = list([node, length+1])
        q.append(temp)


bfs(8)
print(dist)