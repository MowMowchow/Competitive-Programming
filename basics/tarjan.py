import sys
N, M = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(N+1)]
for i in range(M):
  a, b = [int(x) for x in sys.stdin.readline().split()]
  adj[a].append(b)

low = [float('inf') for x in range(N+1)]
disc = [0 for x in range(N+1)]
instack = [False for x in range(N+1)]
vis = [False for x in range(N+1)]
time = 0
total_scc = []


def tarjan(curr, prev):
  global time
  instack[curr] = True
  stack.append(curr)
  vis[curr] = True
  time += 1
  disc[curr] = time
  low[curr] = time

  for node in adj[curr]:
    if not vis[node]:
      tarjan(node, curr)
    if instack[node]:
      low[curr] = min(low[curr], low[node])

  if disc[curr] == low[curr]:
    temp = []
    while len(stack) > 0:
      instack[stack[-1]] = False
      low[node] = disc[curr]
      if stack[-1] == curr:
        temp.append(stack.pop(-1))
        break
      temp.append(stack.pop(-1))
    total_scc.append(temp)


for i in range(1, N+1):
  if not vis[i]:
    stack = []
    tarjan(i, -1)

for i in total_scc:
  print(i)