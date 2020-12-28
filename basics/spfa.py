import sys
N, M = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(N+1)]
for i in range(M):
  a, b, c = [int(x) for x in sys.stdin.readline().split()]
  adj[a].append([b, c])
  adj[b].append([a, c])

dist = [float("inf") for x in range(N+1)] 
visited = [False for x in range(N+1)] 

def spfa(start):
  q = [start]
  dist[start] = 0
  while q:
    curr = q.pop(0)
    print(q, curr)

    for node, w in adj[curr]:
      if dist[curr] + w < dist[node]:
        dist[node] = dist[curr] + w
        q.append(node)

spfa(1)
print(dist)