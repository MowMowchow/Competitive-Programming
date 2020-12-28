import sys
N, M = [int(x) for x in sys.stdin.readline().split()]
edges = [[int(x) for x in sys.stdin.readline().split()] for y in range(M)]
subsets = [[x, 0] for x in range(N+1)] # parent, rank
edges.sort(key=lambda x: x[2])  # assuming weight is at index 2

def find(node):
  if subsets[node][0] != node:
    subsets[node][0] = find(subsets[node][0])
  return subsets[node][0]


def union(u, v):
  if subsets[u][1] > subsets[v][1]:
    subsets[v][0] = subsets[u][0]
  elif subsets[u][1] < subsets[v][1]:
    subsets[u][0] = subsets[v][0]
  else:
    subsets[v][0] = subsets[u][0]
    subsets[u][1] += 1

def kruskal():
  mst_weight = 0
  c = 0

  for a, b, w in edges:
    x = find(a)
    y = find(b)
    if x != y:
      union(x, y)
      mst_weight += w
      c += 1
      if c == N-1:
        break
    
  return mst_weight


print(kruskal())