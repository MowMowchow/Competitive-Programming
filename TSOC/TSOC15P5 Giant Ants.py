
def do(x):
    dispdists[x] = 0
    return x


n, m = [int(x) for x in sys.stdin.readline().split()]
dispdists = [float("inf") for x in range(n+1)]
adj = [[] for x in range(n+1)]
for i in range(m):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    adj[x].append(y)
    adj[y].append(x)
w = int(sys.stdin.readline())
dispensers = [do(int(sys.stdin.readline())) for x in range(w)]


def bfs(a):
    queue = [[a, 0]]
    visited = [False for x in range(n+1)]

    while queue:
        curr = queue.pop(0)
        if not visited[curr[0]]:
            visited[curr[0]] = True
            for node in adj[curr[0]]:
                new = list(curr)
                new[0] = node
                new[1] = curr[1]+1
                dispdists[node] = min(dispdists[node], new[1])
                queue.append(new)


for dispenser in dispensers:
    bfs(dispenser)


def otherbfs(a):
    queue = [[a, 0]]
    visited = [False for x in range(n+1)]
    found = [False, 0]

    while queue:
        curr = queue.pop(0)
        if not visited[curr[0]]:
            visited[curr[0]] = True
            for node in adj[curr[0]]:
                new = list(curr)
                new[0] = node
                new[1] = curr[1]+1

                if new[1] <= 4*dispdists[node]:
                    queue.append(new)
                    if node == n:
                        found[0] = True
                        found[1] = new[1]

    return found


result = otherbfs(1)
if result[0]:
    print(result[1])
else:
    print("sacrifice bobhob314")