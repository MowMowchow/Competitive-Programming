import sys
gridsize, maxheight = [int(x) for x in sys.stdin.readline().split()]
grid = []
for i in range(gridsize):
    grid.append(sys.stdin.readline().strip("\n").split())
move = [[0, -1], [0, 1], [-1, 0], [1, 0]] #U D L R
visited = [[float("inf") for x in range(gridsize)] for x in range(gridsize)]
visited[0][0] = 0

def bfs():
    queue = [[0, 0]]
    possbile = False


    while queue:
        path = queue.pop(0)


        if 0 <= path[0] + move[0][0] < gridsize and 0 <= path[1] + move[0][1] < gridsize:
            if abs(int(grid[path[1] + move[0][1]][path[0] + move[0][0]]) - int(grid[path[1]][path[0]])) <= maxheight:
                if visited[path[1]][path[0]] + 1 < visited[path[1] + move[0][1]][path[0] + move[0][0]]:
                    visited[path[1] + move[0][1]][path[0] + move[0][0]] = visited[path[1]][path[0]] + 1
                    queue.append([path[0] + move[0][0], path[1] + move[0][1]])

        if 0 <= path[0] + move[1][0] < gridsize and 0 <= path[1] + move[1][1] < gridsize:
            if abs(int(grid[path[1] + move[1][1]][path[0] + move[1][0]]) - int(grid[path[1]][path[0]])) <= maxheight:
                if visited[path[1]][path[0]] + 1 < visited[path[1] + move[1][1]][path[0] + move[1][0]]:
                    visited[path[1] + move[1][1]][path[0] + move[1][0]] = visited[path[1]][path[0]] + 1
                    queue.append([path[0] + move[1][0], path[1] + move[1][1]])


        if 0 <= path[0] + move[2][0] < gridsize and 0 <= path[1] + move[2][1] < gridsize:
            if abs(int(grid[path[1] + move[2][1]][path[0] + move[2][0]]) - int(grid[path[1]][path[0]])) <= maxheight:
                if visited[path[1]][path[0]] + 1 < visited[path[1] + move[2][1]][path[0] + move[2][0]]:
                    visited[path[1] + move[2][1]][path[0] + move[2][0]] = visited[path[1]][path[0]] + 1
                    queue.append([path[0] + move[2][0], path[1] + move[2][1]])


        if 0 <= path[0] + move[3][0] < gridsize and 0 <= path[1] + move[3][1] < gridsize:
            if abs(int(grid[path[1] + move[3][1]][path[0] + move[3][0]]) - int(grid[path[1]][path[0]])) <= maxheight:
                if visited[path[1]][path[0]] + 1 < visited[path[1] + move[3][1]][path[0] + move[3][0]]:
                    visited[path[1] + move[3][1]][path[0] + move[3][0]] = visited[path[1]][path[0]] + 1
                    queue.append([path[0] + move[3][0], path[1] + move[3][1]])

        if [path[0], path[1]] == [gridsize-1, gridsize-1]:
            possbile = True
            return possbile

possbile = bfs()

if possbile:
    print("yes")
else:
    print("no")