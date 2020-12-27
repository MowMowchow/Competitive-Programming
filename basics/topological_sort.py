import sys
N, M = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(N)]
for i in range(M):
  a, b = [int(x) for x in sys.stdin.readline().split()]
  adj[a].append(b)

visited = [False for x in range(N)]
stack = []

def dfs(curr):
  visited[curr] = True

  for node in adj[curr]:
    if not visited[node]:
      dfs(node)


  stack.append(curr)

for i in range(N):
  if (not visited[i]):
    dfs(i)

print(list(reversed(stack)))