import sys
numbertestcases = int(sys.stdin.readline())


def traverse(numberofrows, numberofcolumns, startingpoint, endingpoint):
    queue = [[startingpoint[0], startingpoint[1], 0]]
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]] #U D L R
    visited = [[0 for x in range(numberofcolumns)] for x in range(numberofrows)]


    while queue:
        node = queue.pop(0)

        if 0 < visited[endingpoint[1]][endingpoint[0]] < 60:
            #print("Found:", node[2])
            return visited[endingpoint[1]][endingpoint[0]]
        if visited[endingpoint[1]][endingpoint[0]] >= 60:
            #print("peepee:", node[2])
            return visited[endingpoint[1]][endingpoint[0]]

        #up
        if 0 <= node[0]+moves[0][0] < numberofcolumns and 0 <= node[1]+moves[0][1] < numberofrows:
            if grid[node[1]+moves[0][1]][node[0]+moves[0][0]] != "X":
                if visited[node[1]+moves[0][1]][node[0]+moves[0][0]] < node[2]+1 or visited[node[1]+moves[0][1]][node[0]+moves[0][0]] == 0:
                    visited[node[1] + moves[0][1]][node[0] + moves[0][0]] += node[2] + 1
                    queue.append([node[0]+moves[0][0], node[1]+moves[0][1], node[2]+1])
        #down
        if 0 <= node[0]+moves[1][0] < numberofcolumns and 0 <= node[1]+moves[1][1] < numberofrows:
            if grid[node[1]+moves[1][1]][node[0]+moves[1][0]] != "X":
                if visited[node[1]+moves[1][1]][node[0]+moves[1][0]] < node[2]+1 or visited[node[1]+moves[1][1]][node[0]+moves[1][0]] == 0:
                    visited[node[1] + moves[1][1]][node[0] + moves[1][0]] += node[2] + 1
                    queue.append([node[0]+moves[1][0], node[1]+moves[1][1], node[2]+1])
        #left
        if 0 <= node[0]+moves[2][0] < numberofcolumns and 0 <= node[1]+moves[2][1] < numberofrows:
            if grid[node[1]+moves[2][1]][node[0]+moves[2][0]] != "X":
                if visited[node[1]+moves[2][1]][node[0]+moves[2][0]] < node[2]+1 or visited[node[1]+moves[2][1]][node[0]+moves[2][0]] == 0:
                    visited[node[1] + moves[2][1]][node[0] + moves[2][0]] += node[2] + 1
                    queue.append([node[0]+moves[2][0], node[1]+moves[2][1], node[2]+1])
        #right
        if 0 <= node[0]+moves[3][0] < numberofcolumns and 0 <= node[1]+moves[3][1] < numberofrows:
            if grid[node[1]+moves[3][1]][node[0]+moves[3][0]] != "X":
                if visited[node[1]+moves[3][1]][node[0]+moves[3][0]] < node[2]+1 or visited[node[1]+moves[3][1]][node[0]+moves[3][0]] == 0:
                    visited[node[1] + moves[3][1]][node[0] + moves[3][0]] += node[2] + 1
                    queue.append([node[0]+moves[3][0], node[1]+moves[3][1], node[2]+1])

    return visited[endingpoint[1]][endingpoint[0]]


# for each case
for case in range(numbertestcases):
    numberofcolumns, numberofrows = sys.stdin.readline().split()
    numberofcolumns, numberofrows = int(numberofcolumns), int(numberofrows)
    grid = []
    # print(numberofcolumns, numberofrows)
    for i in range(numberofrows):
        grid.append(sys.stdin.readline().strip("\n"))

    startingpoint = [0, 0]
    endingpoint = [0, 0]
    for row in range(numberofrows):
        if startingpoint[0] != 0 and startingpoint[1] != 0 and endingpoint[0] != 0 and endingpoint[1] != 0:
            break
        if "C" in grid[row]:
            startingpoint[0] = grid[row].index("C")
            startingpoint[1] = row

        if "W" in grid[row]:
            endingpoint[0] = grid[row].index("W")
            endingpoint[1] = row

    final = traverse(numberofrows, numberofcolumns, startingpoint, endingpoint)

    if 0 < final < 60:
        print(final)
    else:
        print("#notworth")