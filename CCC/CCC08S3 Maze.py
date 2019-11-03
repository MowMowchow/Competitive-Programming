import sys


def search(final, x, y, count):
    visited[y][x] = count
    if visited[numberOfRows-1][numberOfColumns-1] == numberOfRows+numberOfColumns-1:
        return
    if x == final[0] and y == final[1]:
        count += 1
        visited[y][x] = count
        return

    else: #going to a new interection or a stop
        if city[y][0][x] == "+":
            if 0 <= x < numberOfColumns and 0 <= y+1 < numberOfRows: #out of bounds check
                if city[y+1][0][x] != "*" and visited[y+1][x] == 0 or city[y+1][0][x] != "*" and count < visited[y+1][x]:
                    search(final, x, y + 1, count + 1) #Down
            if 0 <= x+1 < numberOfColumns and 0 <= y < numberOfRows:
                if city[y][0][x+1] != "*" and visited[y][x+1] == 0 or city[y][0][x+1] != "*" and count < visited[y][x+1]:
                    search(final, x + 1, y, count + 1) #Right
            if 0 <= x < numberOfColumns and 0 <= y-1 < numberOfRows:
                if city[y-1][0][x] != "*" and visited[y-1][x] == 0 or city[y-1][0][x] != "*" and count < visited[y-1][x]:
                    search(final, x, y - 1, count + 1) #Up
            if 0 <= x-1 < numberOfColumns and 0 <= y < numberOfRows:
                if city[y][0][x-1] != "*" and visited[y][x-1] == 0 or city[y][0][x-1] != "*" and count < visited[y][x-1]:
                    search(final, x - 1, y, count + 1) #Left

        elif city[y][0][x] == "-":
            if 0 <= x+1 < numberOfColumns and 0 <= y < numberOfRows:
                if city[y][0][x+1] != "*" and visited[y][x+1] == 0 or city[y][0][x+1] != "*" and count < visited[y][x+1]:
                    search(final, x + 1, y, count + 1) #Right
            if 0 <= x-1 < numberOfColumns and 0 <= y < numberOfRows:
                if city[y][0][x-1] != "*" and visited[y][x-1] == 0 or city[y][0][x-1] != "*" and count < visited[y][x-1]:
                    search(final, x - 1, y, count + 1) #Left

        elif city[y][0][x] == "|":
            if 0 <= x < numberOfColumns and 0 <= y+1 < numberOfRows:
                if city[y+1][0][x] != "*" and visited[y+1][x] == 0 or city[y+1][0][x] != "*" and count < visited[y+1][x]:
                    search(final, x, y + 1, count + 1) #Down
            if 0 <= x < numberOfColumns and 0 <= y-1 < numberOfRows:
                if city[y-1][0][x] != "*" and visited[y-1][x] == 0 or city[y-1][0][x] != "*" and count < visited[y-1][x]:
                    search(final, x, y - 1, count + 1) #Up


cases = int(sys.stdin.readline())
for case in range(cases):
    numberOfRows = int(sys.stdin.readline())
    numberOfColumns = int(sys.stdin.readline())
    city = []
    for i in range(numberOfRows):
        city.append(sys.stdin.readline().split())
    #^ All data processing

    visited = [[0 for x in range(numberOfColumns)] for z in range(numberOfRows)]
    search([numberOfColumns-1, numberOfRows-1], 0, 0, 0)
    if visited[numberOfRows-1][numberOfColumns-1] == 0:
        print("-1")
    else:
        print(visited[numberOfRows-1][numberOfColumns-1])