import sys
n = int(sys.stdin.readline())
grid = [sys.stdin.readline().strip("\n") for x in range(n)]
final = "ongoing"

for row in grid:  # horizontal
    prev = "."
    streak = 1
    for spot in row:
        if spot == prev and spot != ".":
            streak += 1
            if streak == 3:
                final = spot

        elif spot != prev or spot == ".":
            prev = spot
            streak = 1


for column in range(n):  # vertical
    prev = "."
    streak = 1
    for rowspot in range(n):
        if grid[rowspot][column] == prev and grid[rowspot][column] != ".":
            streak += 1
            if streak == 3:
                final = grid[rowspot][column]

        elif grid[rowspot][column] != prev or grid[rowspot][column] == ".":
            prev = grid[rowspot][column]
            streak = 1


for row in range(1, n-1):
    for spot in range(1, n-1):
        if grid[row-1][spot-1] == grid[row][spot] == grid[row+1][spot+1] or grid[row-1][spot+1] == grid[row][spot] == grid[row+1][spot-1]:
            if grid[row][spot] != ".":
                final = grid[row][spot]


print final