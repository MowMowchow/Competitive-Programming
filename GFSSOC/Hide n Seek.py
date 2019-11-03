# bfs from g and to all the other h's (t-1) times
# stored the result as adj list
# dfs / spfa to find min
n, m, t = [int(x) for x in sys.stdin.readline().split()]
adj = [[float("inf") for x in range(t+1)] for x in range(t+1)]  # let griffy be 0 and hiders be 1...t+1
final = float("inf")
hiders = []
grid = []
griffy = []
for i in range(n):
    row = sys.stdin.readline().strip("\n")
    for k in range(m):
        if row[k] == "H":
            hiders.append(list([k, i]))
        elif row[k] == "G":
            griffy = list([k, i])
    grid.append(row)


def bfs(c, start):
    visited = [[False for x in range(m)] for y in range(n)]
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # U D L R
    queue = [start+[0]]

    while queue:
        curr = queue.pop(0)
        if not visited[curr[1]][curr[0]]:
            visited[curr[1]][curr[0]] = True

            for move in moves:
                cx, cy = curr[0]+move[0], curr[1]+move[1]
                if 0 <= cx < m and 0 <= cy < n:
                    if grid[cy][cx] != "X":
                        queue.append(list([cx, cy, curr[2]+1]))

                        if grid[cy][cx] == "H":
                            for j in range(1, t+1):
                                if [cx, cy] == hiders[j-1] and c != j:
                                    adj[c][j] = min(adj[c][j], curr[2]+1)


for i in range(t+1):
    if i == 0:
        bfs(i, griffy)
    else:
        bfs(i, hiders[i-1])


def dfs(curr, counter, weight, visited):
    global final
    if not visited[curr]:
        visited[curr] = True
        counter += 1

        if counter == t+1:
            final = min(final, weight)

        for i in range(1, len(adj[curr])):
            if adj[curr][i] != float("inf"):
                dfs(i, counter, weight+adj[curr][i], list(visited))


dfs(0, 0, 0, [False for x in range(t+1)])

print(final)