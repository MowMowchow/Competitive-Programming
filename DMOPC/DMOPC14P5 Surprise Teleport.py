import sys
rows, columns = [int(x) for x in sys.stdin.readline().split()]
starty, startx = [int(x) for x in sys.stdin.readline().split()]
officey, officex = [int(x) for x in sys.stdin.readline().split()]
teleporters = [[False for x in range(columns)] for z in range(rows)]

grid = []

for row in range(rows):
    grid.append(sys.stdin.readline().strip("\n"))
numberofteleports = int(sys.stdin.readline())

for porter in range(numberofteleports):
    current = [int(x) for x in sys.stdin.readline().split()]
    teleporters[current[0]][current[1]] = True

firsteleport = []
visited = [[float("inf") for x in range(columns)] for z in range(rows)]
visited[starty][startx] = 0


def traverse(startingpoint, office):
    queue = [startingpoint]
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # U D L R

    while queue:
        path = queue.pop(0)

        # indexing is switched for teleporters because I didn't want to change the input
        if teleporters[path[1]][path[0]] and not firsteleport:
            firsteleport.append([path[0], path[1]])

        if [path[0], path[1]] == office:
            return

        # up
        if 0 <= path[0]+moves[0][0] < columns and 0 <= path[1]+moves[0][1] < rows and grid[path[1]+moves[0][1]][path[0]+moves[0][0]] != "X":
            if visited[path[1]+moves[0][1]][path[0]+moves[0][0]] > visited[path[1]][path[0]]+1:
                visited[path[1] + moves[0][1]][path[0] + moves[0][0]] = visited[path[1]][path[0]]+1
                queue.append([path[0] + moves[0][0], path[1] + moves[0][1]])

        # down
        if 0 <= path[0] + moves[1][0] < columns and 0 <= path[1] + moves[1][1] < rows and grid[path[1] + moves[1][1]][path[0] + moves[1][0]] != "X":
            if visited[path[1] + moves[1][1]][path[0] + moves[1][0]] > visited[path[1]][path[0]]+1:
                visited[path[1] + moves[1][1]][path[0] + moves[1][0]] = visited[path[1]][path[0]]+1
                queue.append([path[0] + moves[1][0], path[1] + moves[1][1]])

        # left
        if 0 <= path[0] + moves[2][0] < columns and 0 <= path[1] + moves[2][1] < rows and grid[path[1] + moves[2][1]][path[0] + moves[2][0]] != "X":
            if visited[path[1] + moves[2][1]][path[0] + moves[2][0]] > visited[path[1]][path[0]]+1:
                visited[path[1] + moves[2][1]][path[0] + moves[2][0]] = visited[path[1]][path[0]]+1
                queue.append([path[0] + moves[2][0], path[1] + moves[2][1]])

        # right
        if 0 <= path[0] + moves[3][0] < columns and 0 <= path[1] + moves[3][1] < rows and grid[path[1] + moves[3][1]][path[0] + moves[3][0]] != "X":
            if visited[path[1] + moves[3][1]][path[0] + moves[3][0]] > visited[path[1]][path[0]]+1:
                visited[path[1] + moves[3][1]][path[0] + moves[3][0]] = visited[path[1]][path[0]]+1
                queue.append([path[0] + moves[3][0], path[1] + moves[3][1]])

    return


traverse([startx, starty], [officex, officey])

if visited[officey][officex] - visited[firsteleport[0][1]][firsteleport[0][0]] >= 0:
    print(visited[officey][officex] - visited[firsteleport[0][1]][firsteleport[0][0]])
else:
    print(0)