import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj = [[] for x in range(n+1)]
visited = [False for x in range(n + 1)]
stack = [False for x in range(n + 1)]
cycle = []

for i in range(m):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    last = x
    adj[x].append(y)


def dfs(curr):
    visited[curr] = True
    stack[curr] = True

    for node in adj[curr]:
        if not visited[node]:
            if dfs(node):
                return True
        elif stack[node]:
            return True

    stack[curr] = False
    return False


def do():
    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i):
                return True
    return False


if do():
    print("N")
else:
    print("Y")