import sys
n, m = [int(x) for x in sys.stdin.readline().split()] #row by column
grid = []
start = None
finish = None
visited = [[float("inf") for x in range(m)] for x in range(n)]

for i in range(n):
    row = sys.stdin.readline().strip("\n")
    grid.append(row)

    if "s" in row:#found in terms of x, y
        start = ([int(row.index("s")), int(i)])
    if "e" in row:
        finish = ([int(row.index("e")), int(i)])


def bfs(start, finish):
    queue = [start]
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]] #U D L R
    visited[start[1]][start[0]] = 0

    while queue:
        curr = queue.pop(0)

        if 0 <= curr[0]+moves[0][0] < m and 0 <= curr[1]+moves[0][1] < n: #U
            if grid[curr[1]+moves[0][1]][curr[0]+moves[0][0]] != "X":
                if visited[curr[1]+moves[0][1]][curr[0]+moves[0][0]] > visited[curr[1]][curr[0]]+1:
                    visited[curr[1]+moves[0][1]][curr[0]+moves[0][0]] = visited[curr[1]][curr[0]]+1
                    queue.append([curr[0]+moves[0][0], curr[1]+moves[0][1]])


        if 0 <= curr[0]+moves[1][0] < m and 0 <= curr[1]+moves[1][1] < n: #D
            if grid[curr[1]+moves[1][1]][curr[0]+moves[1][0]] != "X":
                if visited[curr[1]+moves[1][1]][curr[0]+moves[1][0]] > visited[curr[1]][curr[0]]+1:
                    visited[curr[1]+moves[1][1]][curr[0]+moves[1][0]] = visited[curr[1]][curr[0]]+1
                    queue.append([curr[0]+moves[1][0], curr[1]+moves[1][1]])


        if 0 <= curr[0]+moves[2][0] < m and 0 <= curr[1]+moves[2][1] < n: #L
            if grid[curr[1]+moves[2][1]][curr[0]+moves[2][0]] != "X":
                if visited[curr[1]+moves[2][1]][curr[0]+moves[2][0]] > visited[curr[1]][curr[0]]+1:
                    visited[curr[1]+moves[2][1]][curr[0]+moves[2][0]] = visited[curr[1]][curr[0]]+1
                    queue.append([curr[0]+moves[2][0], curr[1]+moves[2][1]])


        if 0 <= curr[0]+moves[3][0] < m and 0 <= curr[1]+moves[3][1] < n: #R
            if grid[curr[1]+moves[3][1]][curr[0]+moves[3][0]] != "X":
                if visited[curr[1]+moves[3][1]][curr[0]+moves[3][0]] > visited[curr[1]][curr[0]]+1:
                    visited[curr[1]+moves[3][1]][curr[0]+moves[3][0]] = visited[curr[1]][curr[0]]+1
                    queue.append([curr[0]+moves[3][0], curr[1]+moves[3][1]])

        if grid[curr[1]][curr[0]] == "e":
            return


bfs(start, finish)

if visited[finish[1]][finish[0]] != float("inf"):
    print(visited[finish[1]][finish[0]]-1)
else:
    print(-1)