import sys
numberofrows, numberofcolumns = sys.stdin.readline().split()
numberofrows, numberofcolumns = int(numberofrows), int(numberofcolumns)
grid = []
cameras = []
startcoordinates = [0, 0]
for row in range(numberofrows): #creates the grid
    line = sys.stdin.readline().strip("\n")
    grid.append(line)
    if "C" in line:
        for i in range(len(line)):
            if line[i] == "C":
                camx = i
                camy = row
                cameras.append([camx, camy])
for row in range(len(grid)): #finds the starting location
    if "S" in grid[row]:
        startcoordinates[1] = row
        startcoordinates[0] = grid[row].index("S")
        break
#all of the above is processing the grid and finding the starting point
visited = [[99999999 for x in range(numberofcolumns)] for z in range(numberofrows)]
valid = [[True for x in range(numberofcolumns)] for z in range(numberofrows)]

for i in cameras:
    x, y = i[0], i[1]
    valid[y][x] = False
    for j in range(y, numberofrows):
        if grid[j][x] == 'W':
            break
        valid[j][x] = False
    for j in range(y, -1, -1):
        if grid[j][x] == 'W':
            break
        valid[j][x] = False
    for j in range(x, numberofcolumns):
        if grid[y][j] == "W":
            break
        valid[y][j] = False
    for j in range(x, -1, -1):
        if grid[y][j] == "W":
            break
        valid[y][j] = False

#for i in valid:
#    print(i)

#to traverse through the grid
def search(startx, starty):
    queue = [[startx, starty]]
    conveyers = ["L", "R", "U", "D"]
    options = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if valid[starty][startx] == False:
        return

    visited[starty][startx] = 0
    while queue:
        node = queue.pop(0)
        #if 0 < node[0] < numberofcolumns and 0 < node[1] < numberofrows:
        #fix below
        if grid[node[1]][node[0]] in conveyers:
            index = conveyers.index(grid[node[1]][node[0]])
            x, y = node[0]+options[index][0], node[1]+options[index][1]

            if grid[y][x] != "W" and visited[y][x] > visited[node[1]][node[0]]:
                if valid[y][x] or grid[y][x] in conveyers:
                    visited[y][x] = visited[node[1]][node[0]]
                    queue.append([x, y])

        else:
            #something is wrong with the cameras
            if grid[node[1]+1][node[0]] != "W" and visited[node[1]][node[0]]+1 < visited[node[1]+1][node[0]]: #down
                if valid[node[1]+1][node[0]] or grid[node[1]+1][node[0]] in conveyers:
                    visited[node[1] + 1][node[0]] = visited[node[1]][node[0]]+1
                    queue.append([node[0], node[1]+1])


            if grid[node[1]-1][node[0]] != "W" and visited[node[1]][node[0]]+1 < visited[node[1]-1][node[0]]: #up
                if valid[node[1]-1][node[0]] or grid[node[1]-1][node[0]] in conveyers:
                    visited[node[1] - 1][node[0]] = visited[node[1]][node[0]]+1
                    queue.append([node[0], node[1]-1])


            if grid[node[1]][node[0]+1] != "W" and visited[node[1]][node[0]]+1 < visited[node[1]][node[0]+1]: #right
                if valid[node[1]][node[0] + 1] or grid[node[1]][node[0] + 1] in conveyers:
                    visited[node[1]][node[0] + 1] = visited[node[1]][node[0]]+1
                    queue.append([node[0]+1, node[1]])


            if grid[node[1]][node[0]-1] != "W" and visited[node[1]][node[0]]+1 < visited[node[1]][node[0]-1]: #left
                if valid[node[1]][node[0] - 1] or grid[node[1]][node[0] - 1] in conveyers:
                    visited[node[1]][node[0] - 1] = visited[node[1]][node[0]]+1
                    queue.append([node[0]-1, node[1]])



search(startcoordinates[0], startcoordinates[1])


for row in range(len(visited)):
    for cell in range(len(grid[row])):
        if grid[row][cell] == ".":
            if visited[row][cell] == "spotted" or visited[row][cell] == 99999999:
                print("-1")
            else:
                print(visited[row][cell])
